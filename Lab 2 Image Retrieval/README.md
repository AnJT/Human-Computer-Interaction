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

### Requirements

- It contains an input box to upload an image (**Formulation**);
- Users can preview the query image in the searching window (**Formulation**);
- It has a search button (**Initiation**);
- Provide an overview of the results (e.g. the total number of results) (**Review**);
- Allow changing search parameters (e.g. select certain category/tag) when reviewing results (**Refinement**);
- Users can take some actions, e.g. add selected images to a favorite list (**Use**);
- Other functions you would like to add in.

### Function

- Upload a image and display
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

![image-20220508025540219](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/3.png)

#### Show only one kind of image

![image-20220508025651142](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/2.png)

### Function Realization

#### Select file and display

There is one input box to upload an image  in the page and users can preview the query image in the searching window.

- ```html
  <input id="file1" type="file" name="file" required/>
  <img id="imgself" class="table-td-img">
  ```

- ```javascript
  $("input[type='file']").change(function () {
      const file = this.files[0];
      if (window.FileReader) {
          const reader = new FileReader();
          reader.readAsDataURL(file);
          // 监听文件读取结束后事件
          reader.onloadend = function (e) {
              document.getElementById("imgself").src = e.target.result
              document.getElementById("imgself").style.visibility = 'visible'
          };
      }
  });
  ```

#### Summary of results

Users can see the number of images in the search results

- ```html
  <td class="table-td" style="text-align: center; vertical-align: middle!important;">
  	<p id="show-p" style="color:white; font-size: large; display:none;">本次供检索到 <b style="color: red; ">9</b> 张相似图片</p>
  </td>
  ```

- ```javascript
  $('#show-p').show()
  ```

#### Show all results

Users can see all the images in the search results

- ```html
  <img id="img0" class="table-td-img">
  ```

- ```javascript
  for (var idx in response.image_list){
      document.getElementById(`img${idx}`).src = response.image_list[idx]
      document.getElementById(`img${idx}`).style.visibility = 'visible'
  }
  ```

#### Show all labels

Users can see the picture label in the search results, and can click the label to view the pictures containing only this label

- ```html
  <button id="btn-cat-0" class="btn-category">all</button>
  ```

- ```javascript
  for (var idx in response.tag_set){
      document.getElementById(`btn-cat-${idx}`).style.backgroundColor = color_list[idx]
      document.getElementById(`btn-cat-${idx}`).style.borderColor = color_list[idx]
      document.getElementById(`btn-cat-${idx}`).innerHTML = response.tag_set[idx]
      $(`#btn-cat-${idx}`).show()
  }
  
  $('.btn-category').click(function () {
      tag = this.innerHTML
      console.log(tag)
      for(var tagFloat of document.getElementsByClassName('btn-category-float')){
          if (tagFloat.innerHTML == tag || tag == 'all'){
              tagFloat.parentNode.style.visibility = 'visible'
              tagFloat.parentNode.childNodes[1].style.display = 'block'
              tagFloat.style.display = 'block'
              continue
          }
          tagFloat.parentNode.childNodes[1].style.display = 'none'
          tagFloat.style.display = 'none'
          tagFloat.parentNode.style.visibility = 'hidden'
      }
  })
  ```

#### Display the labels corresponding to all images

The upper left corner of the image shows the label of this image

- ```html
  <img id="img0" class="table-td-img">
  <img class="table-td-img-float" src="/images/download.png" alt="下载图片">
  <button id="btn-cat-float-0" class="btn-category-float">all</button>
  ```

- ```javascript
  for (var idx in response.tag_list){
      color_idx = response.tag_set.indexOf(response.tag_list[idx])
      document.getElementById(`btn-cat-float-${idx}`).style.backgroundColor = color_list[color_idx]
      document.getElementById(`btn-cat-float-${idx}`).style.borderColor = color_list[color_idx]
      document.getElementById(`btn-cat-float-${idx}`).innerHTML = response.tag_list[idx]
  }
  ```

- ```python
  tag_dict = {}
  for tag_file in os.listdir('database/tags'):
      if tag_file == 'README.txt' or tag_file.endswith('_r1.txt'):
          continue
      tag = tag_file.split('.')[0]
      tag_file_path = os.path.join('database/tags', tag_file)
      with open(tag_file_path, 'r') as f:
          for line in f.readlines():
              tag_dict[f'im{line.strip()}.jpg'] = tag
  with open('tag_dict.json','w') as f:
      json.dump(tag_dict, f, ensure_ascii=False, indent=4, separators=(',', ':'))
      
  
  tag_list = []
  with open('tag_dict.json', 'r') as f:
      tag_dict = json.load(f)
      for image in image_list:
          image_id = re.search('.*?(\d+).jpg', image).group(1)
          try:
              tag_list.append(tag_dict[f'im{image_id}.jpg'])
          except:
              tag_list.append('none')
  ```

#### Download images

Users can click the download button in the lower right corner of the image to download the image

- ```html
  <img id="img0" class="table-td-img">
  <img class="table-td-img-float" src="/images/download.png" alt="下载图片">
  ```

- ```javascript
  $('.table-td-img-float').click(function () {
      const img = this.parentNode.children[0];
      console.log(this)
      console.log(img)
      const a = document.createElement('a');
      const event = new MouseEvent('click');
      a.download = '图片'
      a.href = img.src
      a.dispatchEvent(event)
  });
  ```

#### Animation

```css
img.table-td-img-float:hover{
    transition: all 0.1s;
    transform: scale(1.2, 1.2);
}

img.table-td-img-float:active{
    transition: all 0.1s;
    transform: scale(1, 1);
}

button.btn-category:hover{
    transition: all 0.1s;
    transform: scale(1.1, 1.1);
}

button.btn-category:active{
    transition: all 0.1s;
    transform: scale(1, 1);
}
```

