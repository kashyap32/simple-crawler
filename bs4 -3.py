from bs4 import BeautifulSoup
import requests


f=open("bs4.txt","w")

url=requests.get("http://www.justdial.com/Ahmedabad/Fast-Food/ct-4052")

soup=BeautifulSoup(url.text,"html.parser")
#print soup.prettify()
#data=soup.find_all("span",{'class':'jcn'})
data2=soup.find_all("div",{'class':"col-sm-6 col-xs-8 store-details sp-detail paddingR0"})
data3=soup.find_all("<b>")

data4=soup.find_all("span",{'span':'desk-add jaddt'})
data5=soup.find_all("h4",{'class':'store-name'})



for kr in data2:
   print kr.find_all("h4",{"class":"store-name"})[0].text
   print kr.find_all("span",{"class":"desk-add jaddt"})[0].text

#for kr in data2:
   # print kr.text
 #   for kp in data3:
 #      try:
  #          print (data3)
  #     except:
   #        print "no idea"

   
#for k in data3:
  #  print(k.text)
#for kp in data4:
  #  print(kp.text)   
#print data
#for data1 in data:   
 #   print data1.text

#for link in soup.find_all('a'):
 #   print (link.get('href'),link.text)
