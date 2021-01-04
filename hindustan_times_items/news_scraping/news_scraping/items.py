# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

import re

from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags

# def remove_quotations(value):
#     return value.replace(u"\u201d", '').replace(u"\u201c", '')

# def remove_nt(value):
#     return value.replace("\n",' ').replace(" ", " ")

# def filter_value(value):
#     if re.sub("[^0-9]", "", value):
#         return value
#     else:
#         return None
#this is the code for removing all text


# flag = 1111111111


# def set_flag_heading(value,flag):
#     if re.match("^(?!\s*$).+", value):
#         return value
#     else:
#         flag = flag & 1111111110

# def set_flag_subheading(value,flag):
#     if re.match("^(?!\s*$).+", value):
#         return value
#     else:
#         flag = flag & 1111111101

# def set_flag_summary(value,flag):
#     if re.match("^(?!\s*$).+", value):
#         return value
#     else:
#         flag = flag & 1111111011
        
# def set_flag_imagelink(value,flag):
#     if re.match("^(?!\s*$).+", value):
#         return value
#     else:
#         flag = flag & 1111110111

# def set_flag_content(value,flag):
#     if re.match("^(?!\s*$).+", value):
#         return value
#     else:
#         flag = flag & 1111101111

# def set_flag_topic(value,flag):
#     if re.match("^(?!\s*$).+", value):
#         return value
#     else:
#         flag = flag & 1111011111


# def set_flag_date_published(value,flag):
#     if re.match("^(?!\s*$).+", value):
#         return value
#     else:
#         flag = flag & 1110111111



# def set_flag_author(value,flag):
#     if re.match("^(?!\s*$).+", value):
#         return value
#     else:
#         flag = flag & 1101111111


# def set_flag_tags(value,flag):
#     if re.match("^(?!\s*$).+", value):
#         return value
#     else:
#         flag = flag & 1011111111


# def set_flag_field_value(value,flag):
#     value = flag
#     return value

#error - set_flag_field missing one positional argument




# class set_value:

#     flag = 0b1111111111


#     def set_flag_heading(self,value):
#         if re.match("^(?!\s*$).+", value):
#             return value
#         else:
#             bin_str = bin(self.flag & 0b1111111110) #bin returns a string
#             without_0b =  re.sub('0b', '', bin_str)
#             self.flag = int(without_0b)

#     def set_flag_subheading(self,value):
#         if re.match("^(?!\s*$).+", value):
#             return value
#         else:
#             bin_str = bin(self.flag & 0b1111111101)
#             without_0b =  re.sub('0b', '', bin_str)
#             self.flag = int(without_0b)


#     def set_flag_summary(self,value):
#         if re.match("^(?!\s*$).+", value):
#             return value
#         else:
#             bin_str = bin(self.flag & 0b1111111011)
#             without_0b =  re.sub('0b', '', bin_str)
#             self.flag = int(without_0b)
           
            
#     def set_flag_imagelink(self,value):
#         if re.match("^(?!\s*$).+", value):
#             return value
#         else:
#             bin_str = bin(self.flag & 0b1111110111)
#             without_0b =  re.sub('0b', '', bin_str)
#             self.flag = int(without_0b)


#     def set_flag_content(self,value):
#         if re.match("^(?!\s*$).+", value):
#             return value
#         else:
#             bin_str = bin(self.flag & 0b1111101111)
#             without_0b =  re.sub('0b', '', bin_str)
#             self.flag = int(without_0b)


#     def set_flag_topic(self,value):
#         if re.match("^(?!\s*$).+", value):
#             return value
#         else:
#             bin_str = bin(self.flag & 0b1111011111)
#             without_0b =  re.sub('0b', '', bin_str)
#             self.flag = int(without_0b)



#     def set_flag_date_published(self,value):
#         if re.match("^(?!\s*$).+", value):
#             return value
#         else:
#             bin_str = bin(self.flag & 0b1110111111)
#             without_0b =  re.sub('0b', '', bin_str)
#             self.flag = int(without_0b)



#     def set_flag_author(self,value):
#         if re.match("^(?!\s*$).+", value):
#             return value
#         else:
#             bin_str = bin(self.flag & 0b1101111111)
#             without_0b =  re.sub('0b', '', bin_str)
#             self.flag = int(without_0b)



#     def set_flag_tags(self,value):
#         if re.match("^(?!\s*$).+", value):
#             return value
#         else:
#             bin_str = bin(self.flag & 0b1011111111)
#             without_0b =  re.sub('0b', '', bin_str)
#             self.flag = int(without_0b)



#     def set_flag_field_value(self,value):
#         value = self.flag
#         self.flag = 0b1111111111
#         return value





class set_value:

    flag = '123456789'


    def set_flag_heading(self,value):
        if re.match("^(?!\s*$).+", value):
            return value
        else:
            change_flag = re.sub('2','0',self.flag)
            self.flag = change_flag
            

    # def set_flag_subheading(self,value):
    #     if re.match("^(?!\s*$).+", value):
    #         return value
    #     else:
    #         bin_str = bin(self.flag & 0b1111111101)
    #         without_0b =  re.sub('0b', '', bin_str)
    #         self.flag = int(without_0b)


    # def set_flag_summary(self,value):
    #     if re.match("^(?!\s*$).+", value):
    #         return value
    #     else:
    #         change_flag = re.sub('3','0', self.flag)
    #         self.flag = change_flag
            
           
            
    def set_flag_imagelink(self,value):
        if re.match("^(?!\s*$).+", value):
            return value
        else:
            change_flag = re.sub('4','0', self.flag)
            self.flag = change_flag
            


    def set_flag_content(self,value):
        if re.match("^(?!\s*$).+", value):
            return value
        else:
            change_flag = re.sub('5','0', self.flag)
            self.flag = change_flag
            


    def set_flag_topic(self,value):
        if re.match("^(?!\s*$).+", value):
            return value
        else:
            change_flag = re.sub('6','0',self.flag)
            self.flag = change_flag
            



    def set_flag_date_published(self,value):
        if re.match("^(?!\s*$).+", value):
            return value
        else:
            change_flag = re.sub('7','0',self.flag)
            self.flag = change_flag
            



    def set_flag_author(self,value):
        if re.match("^(?!\s*$).+", value):
            return value
        else:
            change_flag = re.sub('8','0',self.flag)
            self.flag = change_flag
            



    def set_flag_tags(self,value):
        if re.match("^(?!\s*$).+", value):
            return value
        else:
            change_flag = re.sub('9','0', self.flag)
            self.flag = change_flag
            



    def set_flag_field_value(self,value):
        value = self.flag
        self.flag = '123456789'
        return value






filter = set_value()



class NewsScrapingItem(scrapy.Item):

    Flag = scrapy.Field(
        default = '123456789',
        input_processor = MapCompose(filter.set_flag_field_value)
    )
    
    heading = scrapy.Field(
        default = "none",
        input_processor= MapCompose(filter.set_flag_heading),
        output_processor= TakeFirst()
    )
    
    # subheading = scrapy.Field(
    #     default = "none",
    #     input_processor= MapCompose(filter.set_flag_subheading),
    #     output_processor= Join(',')
    # )
    
    # summary = scrapy.Field(
    #     default = "none",
    #     input_processor= MapCompose(filter.set_flag_summary),
    #     output_processor= Join(',')
    # )

    imagelink = scrapy.Field(
        default = "none",
        input_processor= MapCompose(filter.set_flag_imagelink),
        output_processor= TakeFirst()
    )
    content = scrapy.Field(
        default = "none",
        input_processor= MapCompose(filter.set_flag_content),
        output_processor= Join(',')
    )
    date_published = scrapy.Field(
        default = "none",
        input_processor= MapCompose(filter.set_flag_date_published),
        output_processor= TakeFirst()
    )
    author = scrapy.Field(
        default = "none",
        input_processor= MapCompose(filter.set_flag_author),
        output_processor= Join(',')
    )
    
    topic = scrapy.Field(
        default = "none",
        input_processor= MapCompose(filter.set_flag_topic),
        output_processor= Join(',')
    )
    tags = scrapy.Field(
        default = "none",
        input_processor= MapCompose(filter.set_flag_tags),
        output_processor= Join(',')
    )
    