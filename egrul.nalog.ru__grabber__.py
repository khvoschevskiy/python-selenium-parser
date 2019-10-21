from selenium import webdriver
from time import sleep
element_rows=[]
string_rows=[]
number=1
driver = webdriver.Firefox()
driver.get('https://egrul.nalog.ru/index.html')
elem = driver.find_element_by_id('query')
query="КОНТРОЛЬНО-СЧЕТНАЯ ПАЛАТА".decode("utf-8")
#for i in query:
#   elem.send_keys(i)
elem.clear()
elem.send_keys(query)
driver.find_element_by_id('btnSearch').click()
#print(driver.find_elements_by_class_name('res-text').text)

#
#   print(row.text)

while number<70 :
   sleep(1)
   element_rows=driver.find_elements_by_class_name('res-text')
   print("element_rows="+str(len(element_rows)))
   print("string_rows="+str(len(string_rows)))
   for i in range(len(element_rows)):
      print("i="+str(i))
      string_rows.append(element_rows[i].text)
   sleep(2)
   try :
      driver.find_element_by_class_name('lnk-page.lnk-page-next').click()
   except :
      sleep(2)
      driver.find_element_by_class_name('lnk-page.lnk-page-next').click()
   number=number+1

with open('myfile.csv', 'w') as fd:
      writer = csv.writer(fd, delimiter=';')
      try:
         for i in range(len(element_rows)):
            writer.writerow(element_rows[i].decode("utf-8"))
      except Exception as e:
         print(e)
