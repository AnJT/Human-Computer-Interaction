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

### Page layout

- Three drop-down menus are placed at the top of the page. The first menu selects to display the salary by school type or region, the second menu selects to display the salary in which period, and the third menu selects the algorithm to display the salary, including min, max, avg and mid.

  ![image-20220522003530428](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/image-20220522003530428.png)

- The bar chart in the upper left corner shows the relationship between each region or school type and each period of salary. We can use it to compare the salary disparity and future development of different school types(or regions)

- The box chart in the upper right corner shows the relationship between salary and region or school type in more detail. We can see the quartile in the box chart. We can use this graph to view if this school type(or region) is equal wage distribution.

  ![QQ录屏20220522003255 00_00_00-00_00_30](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/QQ%E5%BD%95%E5%B1%8F20220522003255%2000_00_00-00_00_30.gif)

- The sunburst chart in the lower left corner shows all school types or regions in the inner ring, and the university name after salary sorting according to the algorithm selected in the third menu in the outer ring. Put the mouse into the chart, and the broken line chart in the lower right corner will show the data of a university in detail.

  ![QQ录屏20220522002812 00_00_00-00_00_30](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/QQ%E5%BD%95%E5%B1%8F20220522002812%2000_00_00-00_00_30.gif)

### ScreenShot

![image-20220522001344274](https://typora-anjt.oss-cn-shanghai.aliyuncs.com/image-20220522001344274.png)