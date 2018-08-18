#! /usr/bin/env python
# _*_  coding:utf-8 _*_

import requests
import urlparse
from bs4 import BeautifulSoup
import sys

def bing_search(url,page):
	Subdomain=[]
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
	for i in range(int(page)):
		try:
			url="https://cn.bing.com/search?q=site%3A"+site+"&qs=n&form=QBRE&sp=-1&pq=site%3A"+site+"&sc=2-11&sk=&cvid=C1A7FC61462345B1A71F431E60467C43&toHttps=1&redig=3FEC4F2BE86247E8AE3BB965A62CD454&pn=2&first=1&FROM=PERE" #.format(i)
			html= requests.get(url,headers=headers,timeout=3)
		except:
			pass
		soup=BeautifulSoup(html.content,'html.parser')
		job_bt=soup.findAll('h2')
		for i in job_bt:
			#print(i.a.get('href'))
			link = i.a.get('href')
			domain=str(urlparse.urlparse(link).scheme+"://"+urlparse.urlparse(link).netloc)
			Subdomain.append(domain)
		Subdomain=list(set(Subdomain))  #去重
	return Subdomain
if __name__ == '__main__':
	#site=baidu.com
	if len(sys.argv) == 3:
		site=sys.argv[1]
		page=sys.argv[2]
	else:
		print ("usage: %s baidu.com 10" % sys.argv[0])
		sys.exit(-1)
	
	Subdomain=bing_search(site,page)
	for i in Subdomain:
		print i