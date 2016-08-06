#coding=utf-8
import requests
import json
import time

# key_word = "mr%20robot"
key_word = "城寨英雄"
# url = "http://search.acfun.tv/search?cd=1&type=2&q=" + hex(ord(key_word)).replace('0x','%',1)


page_size = 10

url = "http://search.acfun.tv/search?cd=1&type=2&q=" + key_word
p = "&sortType=-1&field=title&sortField=score&pageNo=1&pageSize=10&aiCount=3&spCount=3&isWeb=1&sys_name=pc"

headers = {"user-agent":r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36", 
				"host":r"search.acfun.tv", 
				"referer":r"http://www.acfun.tv/search/?"}


def get_content():
		# result_list.append(requests.get(url+p, headers=headers))
		
		r = requests.get(url+p, headers=headers)

		content_raw = json.loads(r.content.split('=')[1])
		try:
			print 10*'>' + '合辑' + 10*'<'
			for i in content_raw['data']['page']['ai']:
				print i['title'], "http://www.acfun.tv/v/" + i['contentId']
		except:
			pass

		print 

		try:
			print 10*'>' + '单集' + 10*'<'
			for j in content_raw['data']['page']['list']:
				print j['title'], "http://www.acfun.tv/v/" + j['contentId']
		except:
			pass

		print


for count in range(page_size):
	print '[Page %s]' %(count + 1)
	p = "&sortType=-1&field=title&sortField=score&pageNo=" + str(count+1) + "&pageSize" + str(page_size) + "&aiCount=3&spCount=3&isWeb=1&sys_name=pc"
	try:
		get_content()
		time.sleep(2)

	except:
		time.sleep(5)
		get_content()




