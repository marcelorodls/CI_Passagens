import csv
import mechanize
import re
import time
import BeautifulSoup
import smtplib
import cookielib
import os
import inemail
import time
from datetime import date, timedelta,datetime

bestprice = ["999999","",""]

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BACK_LRED = '\033[101m' 

def checkForToA(ida,volta):
    ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cj = cookielib.LWPCookieJar()
    browser.set_cookiejar(cj)
    browser.addheaders = [('User-agent', 'Firefox')]
    start = 0
    continuar = True
    links = []

    global bestprice
    print("Connecting: ")
    #urls = "http://b2c.ci.com.br/aviao/pesquisa?TripType=RoundTrip&Origin=Aeroporto+de+Confins&Destination=Minneapolis&DepartureDate="+ida+"&DepartureTimeFrame=0&ReturnDate="+volta+"&ReturnTimeFrame=0&Pax%5B0%5D.Adults=1&Pax%5B0%5D.Children=0&Pax%5B0%5D.Infant=0&AirClass=All&IncludeStudentFares=true&Sorting.OrderBy=Quotes.QuoteTotal.BaseFare&iefix=%E2%9A%99"
    urls = "http://b2c.ci.com.br/aviao/pesquisa?TripType=RoundTrip&IncludeStudentFares=true&Origin=Aeroporto+Internacional+de+Guarulhos&OriginDestinationId=6300629&Destination=Frankfurt&DestinationDestinationId=0&DepartureDate="+ida+"&DepartureTimeFrame=0&ReturnDate="+volta+"&ReturnTimeFrame=0&Pax%5B0%5D.Adults=1&Pax%5B0%5D.Children=0&AirCompany=&AirClass=All"
    #print urls
    browser.open(urls)
    
    html = browser.response().get_data()
    #print html
    with open('gs.txt', 'a') as file:
        file.write(html)



    if "price-secondary" in html.lower():
        print("\tTest: OK") 

    pct_re = re.compile(r'class=\"price-secondary\"><span class=\"vt-currency \" data-value=\"\d+[.]\d+\"')

    aa = set(re.findall(pct_re, html))

    
    print "Prices:\n"
    for x in aa:
        x = x.replace("class=\"price-secondary\"><span class=\"vt-currency \" data-value=\"", "")[0:-1].split('.')[0]
        print x
        if(float(bestprice[0]) >= float(x)):
            print "better"
            bestprice = [str(x),ida, volta]
            with open('best.txt', 'a+') as file:
                file.write(str([str(x),ida, volta]) + "\n")
                

dateida = datetime.strptime('06 12 2015', '%m %d %Y')
d = datetime.strptime('02 01 2016', '%m %d %Y')

while True:

    #23%2F08%2F2015
    
    d = d+ timedelta(days=1)
    print (str(d.day).zfill(2)+"%2F"+
                str(d.month).zfill(2)+"%2F"+
                str(d.year).zfill(4)) 
    checkForToA(str(dateida.day).zfill(2)+"%2F"+
                str(dateida.month).zfill(2)+"%2F"+
                str(dateida.year).zfill(4)
                ,
                str(d.day).zfill(2)+"%2F"+
                str(d.month).zfill(2)+"%2F"+
                str(d.year).zfill(4))

    print("\tSleeping for 1\n\n")    
    time.sleep(1)
    
