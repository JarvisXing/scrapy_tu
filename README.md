# scrapy_tu
![](https://img.shields.io/badge/python-3.6-blue.svg)
![](https://img.shields.io/badge/build-passing-brightgreen.svg)  
![](https://img.shields.io/badge/scrapy-1.5.0-orange.svg)  
this project can spider user infomation saved as .json file,  
and download their avatar icon as .jpg files.  
As a photographer, I choose [tuchong](https://tuchong.com) as target,  
there are nearly 2 million users on this site, if you want to spider all of them,  
I suggest use this spider with proxy and set spider time.

As a result,user data will be like this,saved in `data` folder.   
![](https://github.com/JarvisXing/scrapy_tu/blob/master/image/spider_data.png)  
their avator will be saved in `icon` folder. avator file named with the user's id.  
![](https://github.com/JarvisXing/scrapy_tu/blob/master/image/spider_icon.png)
## software
before run this demo,you'd better to install these lib  
1. [Anaconda3 for windows](https://www.anaconda.com/download)  
    download [Anaconda3-5.1.0-Windows-x86_64.exe](https://repo.anaconda.com/archive/Anaconda3-5.1.0-Windows-x86_64.exe)  
    just install
2. [opencv for python](https://www.opencv.org/)   
    In cmd just run <code>conda install -c conda-forge opencv</code>
    It's necessary for scrapy to spider image with PIL,   
    opencv is a good choice instead of PIL,but pillow not work.
3. [scrapy](https://scrapy.org/)
    run <code>conda install scrapy</code>
4. recommand [chrome](https://www.google.com/chrome/) as debug tool
    you may frequently operate `ctrl+shift+i`,`ctrl+shift+c`,`ctrl+f`,`right click->copy xpath`.
## run
In cmd run <code>scrapy crawl tuchong</code>  
welcome to leave msg at [issues](https://github.com/JarvisXing/scrapy_tu/issues) encountered error.
## File structure
>WORKSPACE_DIR(scrapy_tu)
>>scrapy.cfg  

>>data  
>>>xx.json

>>icon  
>>>xx.jpg

>>tuchong  
>>>spiders
>>>>__init__.py  
>>>>tuchong_spider.py

>>>__init__.py  
>>>items.py  
>>>middlewares.py  
>>>pipelines.py  
>>>settings.py  
