# -*- coding: utf-8 -*-
import scrapy
from tuchong.items import TuchongItem
from datetime import datetime
import json
class TuChongSpider(scrapy.Spider):
    name = 'tuchong'
    #allowed_domains=["tuchong.com"]

    start_urls=[]
    
    for usrid in range(0,1000):
        start_urls.append("https://tuchong.com/"+str(usrid)+"/profile/")
    
    check_xpath="/html/body/main/div/nav"
    iconurl_xpath="//div/a/img/@src"
    userid_xpath="//div/nav/ul/li[@class='active']/a/@href"
    name_xpath="//div/span[@class='info-name']/text()"
    
 #   url_xpath="//ul[@class='site-nav']/li/a/@href"

    followingcnt_xpath="//div/ul[@class='slash-list']/li/a[contains(@href,'following')]/text()"
    followerscnt_xpath="//div/ul[@class='slash-list']/li/a[contains(@href,'followers')]/text()"
        
    basicinfo_xpath="//div/ul[@class='profile-item-block'][1]/li/div/span/text()"
    plabels_xpath="//div/ul[@class='profile-item-block'][2]/li/a/text()"
    ulabels_xpath="//div/ul[@class='profile-item-block'][3]/li/a/text()"
    equips_xpath="//div/ul[@class='profile-item-block'][4]/li/div/a[@href]/text()"
    equpic_xpath="//div/ul[@class='profile-item-block'][4]/li/div/span/text()"
    #aside_xpath="//aside/section/h3/a/text()"#aside following followers groups
    #next_url_xpath = "//div[contains(@class, 'pages')]/a/@href"
#   next_urls_xpath="//aside/section/ul[@class='tight-icons clearfix']/li/a/@href" 
 
    def parse(self, response):
#        next_pages = response.xpath(self.next_urls_xpath).extract()
#        for url in next_pages:
#            yield scrapy.Request(url+'profile')
          
        item = TuchongItem()
        check=response.xpath(self.check_xpath)
        if check:            
            item['userid'] = int(response.xpath(self.userid_xpath).re(r'[0-9]*/profile/')[0].strip('/profile/'))
            item['name'] = response.xpath(self.name_xpath).extract_first().strip()
            
            item["icon_url"] = response.xpath(self.iconurl_xpath).extract()

            item['followingcnt'] = int(response.xpath(self.followingcnt_xpath).extract_first()[4:-1])
            item['followerscnt'] = int(response.xpath(self.followerscnt_xpath).extract_first()[4:-1])
            basicinfo=response.xpath(self.basicinfo_xpath).extract()
            #item['location'] desc signtime
            if len(basicinfo)==1:
                item['location'] ="None"
                item['desc'] = "None"
            elif len(basicinfo)==2:
                item['location'] =basicinfo[0]
                item['desc'] = "None"
            else:
                item['location'] =basicinfo[0]
                item['desc'] = basicinfo[1]
            item['signtime'] =basicinfo[-1]

            plabels=response.xpath(self.plabels_xpath).extract()
            if len(plabels)==0:
                item['plabels'] = "None"
            else:
                plabels=[i.strip().strip('#') for i in plabels]
                item['plabels'] =plabels

            ulabels=response.xpath(self.ulabels_xpath).extract()
            if len(ulabels)==0:
                item['ulabels'] = "None"
            else:
                ulabels=[i.strip().strip('#') for i in ulabels]
                item['ulabels'] =ulabels

            equips= response.xpath(self.equips_xpath).extract()
            equpic = response.xpath(self.equpic_xpath).extract()
        
            if len(equips)==0:
                item['equips'] = "None"
                item['equpic'] = 0
            else:
                item['equips']= equips
                item['equpic']=[int(i.strip('（）')) for i in equpic]

            item['timestramp']= datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            yield item
        else:
            pass
