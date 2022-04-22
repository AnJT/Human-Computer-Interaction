## Lab1: Automatic Speech Recognition

## Installation

- install conda environment

  ```shell
  conda env create -f requirements.yaml
  conda activate asr
  ```

- replace .dic file

  ```shell
  cp pronounciation-dictionary.dict D:\Tools\Anaconda\envs\asr\lib\site-packages\speech_recognition\pocketsphinx-data\en-US\
  ```

  tip: remember to replace it with the address of your environment

### Run

```shell
cd src
conda activate asr
python asr.py
```

## Features

- **Play music**
- **Open Notepad**
- **Open the calculator**

## The modifications to GUI and the codes

- Speech Recognition

  Listen to the microphone through `pyaudio`, and call `pocketsphinx` through `recognize_sphinx` to achieve local speech recognition

  ```python
  def recognize_speech_from_mic(self, recognizer, microphone):
      if not isinstance(recognizer, sr.Recognizer):
      	raise TypeError("`recognizer` must be `Recognizer` instance")
      if not isinstance(microphone, sr.Microphone):
      	raise TypeError("`microphone` must be `Microphone` instance")
      with microphone as source:
      	recognizer.adjust_for_ambient_noise(source, 0.5)
      	audio = recognizer.listen(source)
      response = {
      	"error": None,
      	"transcription": None
      }
      try:
      	response["transcription"] = recognizer.recognize_sphinx(audio)
      except sr.RequestError:
      	# API was unreachable or unresponsive
      	response["error"] = "API unavailable"
      except sr.UnknownValueError:
      	# speech was unintelligible
      	response["error"] = "Unable to recognize speech"
      return response
  ```

- Instruction similarity matching

  Find the command that best matches the speech by calling the python standard library `difflib` for string matching

  ```python
  def string_similar(self, s1, s2):
  	return difflib.SequenceMatcher(None, s1, s2).quick_ratio()
  
  commands = ['play music', 'open notepad', 'open the calculator']
  os_commands = [r'resources\打上花火.mp3', 'notepad', 'calc']
  similar = [self.string_similar(guess["transcription"], command) for command in commands]
  idx = similar.index(max(similar))
  ```

- Execute user commands through the standard library `os`

  ```python
  os.system(os_commands[idx])
  ```

- Execute code related to speech recognition through `QThread` so that the main interface will not block

  ```python
  class WorkThread(QThread):
      trigger_show = pyqtSignal(str)
      trigger_hide = pyqtSignal()
  
      def __int__(self):
          super(WorkThread, self).__init__()
  
      def run(self):
          r = sr.Recognizer()
          mic = sr.Microphone()
          ...
  
  class myWindow(QtWidgets.QMainWindow):
  
      def __init__(self):
          super(myWindow, self).__init__()
          self.myCommand = " "
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.work = WorkThread()
      
      def rec(self):
          self.work.start()
          self.work.trigger_show.connect(self.showRecUi)
          self.work.trigger_hide.connect(self.hideRecUi)
  ```

  

- GUI

  - Improved the display of labels so that labels do not overlap each other
  - Use a more vivid gif animation

## Improve the accuracy of speech recognition

The accuracy of local speech recognition is quite outrageous. I have made the following improvements

- Small range to improve accuracy

  There are very few instructions we need to use, so we can delete the unnecessary content in the `.dic` file, leaving only the content that needs to be identified

  E.g:

  ```
  notepad N OW T P AE D
  music M Y UW Z IH K
  play P L EY
  open OW P AH N
  calculator K AE L K Y AH L EY T ER
  the DH AH
  ```

  Leaving only these words can improve the recognition rate of these words
  
  After changing this file, the accuracy can be almost 100%

## Interface

![image-20220420234743809](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/image-20220420234743809.png)
