## Lab 2: Information Retrieval

### Installation

- install conda environment

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

### Project Structure

```
│  .gitignore
│  README.md
│  requirements.yaml
│  __init__.py
│          
└─server
    │  image_vectorizer.py
    │  rest_server.py
    │  search.py
    │  
    ├─database
    │  ├─dataset   
    │  └─tags
    │          
    ├─imagenet
    │      classify_image_graph_def.pb
    │      
    ├─static
    │  ├─images
    │  │      ajax-loader.gif
    │  │      download.png
    │  │      
    │  └─result
    │          
    ├─templates
    │      main.html
    │      
    └─uploads
```

### ScreenShot

#### Homepage

![image-20220508025320962](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/image-20220508025320962.png)

#### After selecting a image

![image-20220508025453097](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/image-20220508025453097.png)

#### After clicking search

![image-20220508025540219](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/1.png)

#### Show only one kind of image

![image-20220508025651142](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/2.png)
