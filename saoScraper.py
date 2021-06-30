from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import threading
import os

cookies = {
	'csrftoken' : 'zY3zdLj3GHtKgaJm6e75KrbiTstO4iIc',
	'ds_user_id' : '6743084013',
	'ig_did' : 'FACF8BA2-176A-4BA4-A351-2A5EAEC18A9E',
	'mid' : 'YGXMdQALAAGgE5GaRL2TfFiKaaHi',
	'rur' : 'RVA',
	'sessionid' : '6743084013%3AprEF0eSBuixRxL%3A3',
	'shbid' : '204',
	'shbts' : '1622033448.7398653'
}

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get("https://www.instagram.com/")
[driver.add_cookie({'name':e[0], 'value':e[1]}) for e in cookies.items()]

driver.get("https://www.instagram.com/swordartonline.stream/channel/")
time.sleep(2)

threads = []

for i, link in enumerate([e.get_attribute('href') for e in driver.find_elements_by_class_name("_bz0w")]):
	driver.get(link)
	video = driver.find_element_by_tag_name('video').get_attribute('src')
	title =  driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span').text
	r = requests.get(video, stream=True)
	with open(f'{title}.mp4','wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
print('done !')
