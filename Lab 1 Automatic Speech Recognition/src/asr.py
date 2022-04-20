from PyQt5 import QtWidgets, QtGui, QtCore, uic

from asrInterface import Ui_MainWindow
import sys
import os
from PyQt5.QtCore import QThread, pyqtSignal
import speech_recognition as sr
import difflib
import time

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
    
    def showRecUi(self, label_6_text):
        self.ui.showRecUi(label_6_text)
    
    def hideRecUi(self):
        self.ui.hideRecUi()


class WorkThread(QThread):
    trigger_show = pyqtSignal(str)
    trigger_hide = pyqtSignal()

    def __int__(self):
        super(WorkThread, self).__init__()

    def run(self):
        r = sr.Recognizer()
        mic = sr.Microphone()
        commands = ['play music', 'open notepad', 'open the calculator']
        os_commands = [r'resources\打上花火.mp3', 'notepad', 'calc']
        while True:
            guess = self.recognize_speech_from_mic(r, mic)
            if guess["error"]:
                self.trigger_show.emit("ERROR: {}".format(guess["error"]))
                time.sleep(3)
                self.trigger_hide.emit()
                continue
            print(guess["transcription"])
            similar = [self.string_similar(guess["transcription"], command) for command in commands]
            print(similar)
            if max(similar) < 0.2:
                self.trigger_show.emit("I didn't catch that. What did you say?")
                time.sleep(3)
                self.trigger_hide.emit()
                continue
            idx = similar.index(max(similar))
            os.system(os_commands[idx])
            self.trigger_show.emit(commands[idx])
            time.sleep(3)
            self.trigger_hide.emit()
    
    def string_similar(self, s1, s2):
        return difflib.SequenceMatcher(None, s1, s2).quick_ratio()
    
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

app = QtWidgets.QApplication([])
application = myWindow()
application.show()
application.rec()
sys.exit(app.exec())

