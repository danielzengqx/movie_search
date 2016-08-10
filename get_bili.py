#coding=utf-8
import requests
import json
import time
import re
from bs4 import BeautifulSoup as bs
# key_word = "mr%20robot"
key_word = "robot"
# url = "http://search.acfun.tv/search?cd=1&type=2&q=" + hex(ord(key_word)).replace('0x','%',1)


page_size = 10

url = "http://search.bilibili.com/all?keyword=%s" %key_word
url_page = "http://search.bilibili.com/ajax_api/video?keyword=%s" %key_word
page = 1

# p = "&sortType=-1&field=title&sortField=score&pageNo=1&pageSize=10&aiCount=3&spCount=3&isWeb=1&sys_name=pc"
tail = "&order=totalrank&page=%s&_=1470557637611" %page
headers = {'host': 'search.bilibili.com', 
		'referer': 'http://search.bilibili.com/all?keyword=%s' %key_word, 
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def my_attr(tag):
    return tag.has_attr('lnk-type') and  'video_title' in tag['se-linkid'] 

def bangumi(tag):
	return tag.has_attr('lnk-type') and  'bangumi_title' in tag['se-linkid']


def get_content():		
		r = requests.get(url+tail, headers=headers)

		with open("bili_new.html", "w") as f:
			f.write(r.content)	
			# print r.content
		soup = bs(r.content, "html.parser")
		print soup.title



		print 10*">" + "合集" + 10*">"

		for i in soup.find_all("li", class_="synthetical"):

			for j in i.find_all(bangumi):
				print j['title'], ":"

			for j in i.find_all("ul", class_="so-episode"):
				for k in j.find_all("a", href=True):
					print 4*" " + k['title'], k['href']

			# print 'next'



		print 10*">" + "单集" + 10*">"
		for i in soup.find_all("li", class_="video matrix "):
			for j in i.find_all(my_attr):
				print  j['title'].strip(), j['href']






get_content()






