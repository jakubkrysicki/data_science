import urllib
import sys
import os,io
import codecs, io
from urllib import urlopen
from bs4 import BeautifulSoup
import lxml.html as lh
import lxml.etree as et
import re
import datetime
from datetime import timedelta
import calendar
import ast


now = datetime.datetime.now()
date1 = datetime.datetime.now().date()-timedelta(days = 0)
date = (datetime.datetime.now().date()-timedelta(days = 0)).strftime('%Y-%m-%d')
miesiace = {1:"Stycznia",2:"Lutego",3:'Marca',4:'Kwietnia',5:'Maja',6:'Czerwca',7:'Lipca',8:'Sierpnia',9:"Wrzesnia",10:'Pazdziernika',11:'Listopada',12:'Grudnia'}
html = ''
bsObj = ''
backHelp = ''
while True:
	html = "http://api.nbp.pl/api/exchangerates/rates/a/eur/"+str(date)
	print html
	bsObj = BeautifulSoup(urlopen(html),'lxml')
	bsObj = re.sub('<[^<]+?>', '', str(bsObj))
	if bsObj == "404 NotFound - Not Found - Brak danych":
		date1 = date1 - timedelta(days = 1)
		date = date1.strftime('%Y-%m-%d')
		continue
	else:
		bsObj = re.sub('<[^<]+?>', '', str(bsObj))
		bsObj = ast.literal_eval(bsObj)
		rate = bsObj['rates'][0]['mid']
		print '-----------------------------------------------------------------------------'
		print "Znaleziono kurs Euro z przedostatniej publikacji z miesiaca %s - %s" % (miesiace[now.month],rate)
		print '-----------------------------------------------------------------------------'
		break
else:
	print "Brak wyszukania"


