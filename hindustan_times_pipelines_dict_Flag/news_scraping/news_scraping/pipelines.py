# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

import re

from scrapy.exceptions import DropItem  

from itemadapter import ItemAdapter




class flagPipelines(object):

   def __init__(self):
      self.flag = {'heading':True,'subheading':True, 'summary': True, 'imagelink': True, 'content':True, 'date_published': True, 'author': True, 'topic': True, 'tags': True}

   def process_item(self, item, spider):
      
      if not 'heading' in item:

         self.flag['heading'] = False
      
      if not 'subheading' in item:

         self.flag['subheading'] = False
      
      if not 'summary' in item:

         self.flag['summary'] = False
      
      if not 'imagelink' in item:

         self.flag['imagelink'] = False
      
      if not 'content' in item:

         self.flag['content'] = False
      
      if not 'date_published' in item:

         self.flag['date_published'] = False
      
      if not 'author' in item:

         self.flag['author'] = False
      
      if not 'topic' in item:

         self.flag['topic'] = False
      
      if not 'tags' in item:

         self.flag['tags'] = False
            

      item['Flag'] = self.flag

      self.flag = {'heading':True,'subheading':True, 'summary': True, 'imagelink': True, 'content':True, 'date_published': True, 'author': True, 'topic': True, 'tags': True}

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
        db = self.conn['news_paper_flag_data']
        self.collection = db['hindu_dict_tb']
    
    def process_item(self, item, spider):
        
        self.collection.insert_one(ItemAdapter(item).asdict())
        return item

