# Human-Computer-Interaction

## Lab1: Automatic Speech Recognition

## Installation

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

## Features

- **Play music**
- **Open Notepad**
- **Open the Calculator**

## Interface

![image-20220420234743809](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/undefinedimage-20220420234743809.png)
