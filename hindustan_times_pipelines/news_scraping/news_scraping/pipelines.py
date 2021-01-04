# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

import re

from scrapy.exceptions import DropItem  

from itemadapter import ItemAdapter




# class flagPipelines(object):

#    def __init__(self):
#       self.flag = '123456789'

#    def process_item(self, item, spider):
      
#       if not re.match("^(?!\s*$).+", item['heading']):

#          change_flag = re.sub('2','0',self.flag)
#          self.flag = change_flag
      
#       if not re.match("^(?!\s*$).+", item['summary']):

#          change_flag = re.sub('3','0',self.flag)
#          self.flag = change_flag
      
#       if not re.match("^(?!\s*$).+", item['imagelink']):

#          change_flag = re.sub('4','0',self.flag)
#          self.flag = change_flag
      
#       if not re.match("^(?!\s*$).+", item['content']):

#          change_flag = re.sub('5','0',self.flag)
#          self.flag = change_flag
      
#       if not re.match("^(?!\s*$).+", item['date_published']):

#          change_flag = re.sub('6','0',self.flag)
#          self.flag = change_flag
      
#       if not re.match("^(?!\s*$).+", item['author']):

#          change_flag = re.sub('7','0',self.flag)
#          self.flag = change_flag
      
#       if not re.match("^(?!\s*$).+", item['topic']):

#          change_flag = re.sub('8','0',self.flag)
#          self.flag = change_flag
      
#       if not re.match("^(?!\s*$).+", item['tags']):

#          change_flag = re.sub('9','0',self.flag)
#          self.flag = change_flag
            

#       item['Flag'] = self.flag

#       self.flag = '123456789'

#       return item


class flagPipelines(object):

   def __init__(self):
      self.flag = '123456789'

   def process_item(self, item, spider):

      adapter = ItemAdapter(item)
      
      if not adapter['heading']:

         change_flag = re.sub('2','0',self.flag)
         self.flag = change_flag
      
      if not adapter['summary']:

         change_flag = re.sub('3','0',self.flag)
         self.flag = change_flag
      
      if not adapter['imagelink']:

         change_flag = re.sub('4','0',self.flag)
         self.flag = change_flag
      
      if not adapter['content']:

         change_flag = re.sub('5','0',self.flag)
         self.flag = change_flag
      
      if not adapter['date_published']:

         change_flag = re.sub('6','0',self.flag)
         self.flag = change_flag
      
      if not adapter['author']:

         change_flag = re.sub('7','0',self.flag)
         self.flag = change_flag
      
      if not adapter['topic']:

         change_flag = re.sub('8','0',self.flag)
         self.flag = change_flag
      
      if not adapter['tags']:

         change_flag = re.sub('9','0',self.flag)
         self.flag = change_flag
            

      adapter['Flag'] = self.flag

      self.flag = '123456789'

      return item



class DuplicatesPipeline(object):  
   def __init__(self): 
      self.ids_seen = set() 

   def process_item(self, item, spider): 
      if item['heading'] in self.ids_seen: 
         raise DropItem("Repeated items found: %s" % item) 
      else: 
         self.ids_seen.add(item['heading']) 
         return item



class NewsScrapingPipeline:
        
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['news_paper_new_data']
        self.collection = db['hindu_adapt_tb']
    
    def process_item(self, item, spider):
        
        self.collection.insert_one(ItemAdapter(item).asdict())
        return item

