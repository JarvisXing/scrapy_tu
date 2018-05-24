# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import codecs
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request

class TuchongPipeline(object):
    def process_item(self, item, spider):  
        return item 
class DownloadIconsPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['icon_url']:
            yield Request(image_url, meta={'userid': str(item['userid'])})

    def item_completed(self, results, item, info):
        return super(DownloadIconsPipeline, self).item_completed(results, item, info)

    def file_path(self, request, response=None, info=None):
        #f_path = super(DownloadIconsPipeline, self).file_path(request, response, info)
        #f_path = f_path.replace('full', request.meta['userid'], 1)
        icon_name=request.meta['userid']+'.jpg'
        return '%s'%(icon_name)
    
class JsonWithEncodingPipeline(object):
    def __init__(self):
        if os.path.exists("./data"):
            pass
        else:
            os.mkdir("./data")
        files=os.listdir("./data")
        num=len(files)
        json_name = './data/%d.json'%(num)
        while (json_name in files):
            num=num+1                     
        self.file = codecs.open(json_name, 'w', encoding='utf-8')
           
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    
    def spider_closed(self, spider):
        self.file.close()