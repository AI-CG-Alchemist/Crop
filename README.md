# DataSpiders
存储了各视频网站爬取视频数据的代码以及自动截取视频中的人脸

### 配置
我使用的环境是python3.8

新开一个环境，安装所需的依赖：

`pip install -r requirements.txt`

之后安装面部识别包face_alignment：

```powershell
git clone https://github.com/1adrianb/face-alignment
cd face-alignment
pip install -r requirements.txt
python setup.py install
```

### 视频下载
批量下载脚本待补充
执行各自的爬虫代码后，下载好的视频自动存放在data里


### 执行：

`python run.py`

代码默认使用gpu版本的pytorch, 可能需要重新下载, 或者在run.py文件中修改为cpu版本：

`os.system(f'python crop-video.py --inp ./data/{i} --cpu')`

裁剪后的结果存放在output文件中

### b站的视频爬取

执行BiliBili_Spider.py
按提示输入搜索关键词/视频存储目录和抓取视频的数量并在headers中加入自己的cookie

### 抖音的视频爬取
执行Douyin_Spider.py
按提示输入搜索关键字(用空格分开)和抓取视频的数量

### YouTube视频爬取
执行YouTube_Spider.py
按提示输入搜索关键字(用空格分开)和抓取视频的数量
