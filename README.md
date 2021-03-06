# Human-Computer-Interaction

## Lab1: Automatic Speech Recognition

### Installation

- install conda environment

  ```shell
  conda env create -f requirements.yaml
  conda activate asr
  ```

  If the installation fails, please use `pip` to install or download wheel file to install manually

- replace `.dict` file

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

### Function

- **Play music**
- **Open Notepad**
- **Open the Calculator**

### ScreenShot

![image-20220420234743809](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/undefinedimage-20220420234743809.png)

## Lab 2: Information Retrieval

### Installation

install conda environment

```
conda env create -f requirements.yaml
conda activate ir
```

### Run

```
cd server
curl -o database.zip https://anjt.oss-cn-shanghai.aliyuncs.com/database.zip
unzip database.zip

python image_vectorizer.py
python rest_server.py 
```

### Function

- Upload a image
- Overview the total number of the similar images
- Overview the tags of all result
- Click the button to download the image
- Click on tag button to see the images which hold this tag only
- Clear the image and choose another one

### ScreenShot

![image-20220508025540219](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/3.png)

## Lab 3: Data Visualization

### Installation

install conda environment

```
conda env create -f requirements.yaml
conda activate dv
```

### Run

```
cd src
python app.py 
```

### Analysis task

- Analyze the relationship between salary level and school type
- Analyze the relationship between salary level and geographical location
- Analyze the relationship between salary changes and school types
- Analyze the relationship between salary changes and geographical location

### ScreenShot

![image-20220522001344274](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/image-20220522001344274.png)
