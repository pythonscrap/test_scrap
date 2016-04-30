import urllib2
from BeautifulSoup import BeautifulSoup
from datetime import datetime
import schedule
import time

nrldc_tag = 'ctl00_ContentPlaceHolder1_lblGridFreq';
other_tag = 'ctl00_ContentPlaceHolder1_Label1';

nrldc_url='http://www.nrldc.in/'
wrldc_url='http://www.wrldc.in/'
srldc_url='http://www.srldc.in/'
erldc_url='http://www.erldc.org/'
nerldc_url='http://www.nerldc.org/'

nrldc_name = 'nrldc'
wrldc_name = 'wrldc'
srldc_name = 'srldc'
erldc_name = 'erldc'
nerldc_name = 'nerldc'

def get_data_from_rldc(zone_url,zone_name,zone_tag,time_now):
	soup = BeautifulSoup(urllib2.urlopen(zone_url).read())
	freq = soup.find('span', id=zone_tag).contents[0].string
	text_file = open(zone_name+".txt", "a")
	text_file.write(freq+","+time_now)
	text_file.write('\n');
	text_file.close()

def get_data():
	time = str(datetime.now())
	get_data_from_rldc(nrldc_url,nrldc_name,nrldc_tag,time)
	get_data_from_rldc(wrldc_url,wrldc_name,other_tag,time)
	get_data_from_rldc(srldc_url,srldc_name,other_tag,time)
	get_data_from_rldc(erldc_url,erldc_name,other_tag,time)
	get_data_from_rldc(nerldc_url,nerldc_name,other_tag,time)



schedule.every(5).seconds.do(get_data)

while True:
	try:
	    schedule.run_pending()
	    time.sleep(1)
	except Exception, e:
	    time.sleep(1)
