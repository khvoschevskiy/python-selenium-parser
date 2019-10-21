from selenium import webdriver
from time import sleep
element_rows=[]
string_rows=[]
number=1
driver = webdriver.Firefox()
driver.get('https://egrul.nalog.ru/index.html')
elem = driver.find_element_by_id('query')
query="КОНТРОЛЬНО-СЧЕТНАЯ ПАЛАТА"
elem.clear()
elem.send_keys(query)
driver.find_element_by_id('btnSearch').click()

while number<70 :
   sleep(1)
   try:
      element_rows=driver.find_elements_by_class_name('res-text')
      element_title=driver.find_elements_by_class_name('op-excerpt')
      #n=len(element_rows)//2
      element_title_index=list(range(0,len(element_rows)*2,2))
      print("len(element_rows)="+str(len(element_rows)))
      print("len(string_rows)="+str(len(string_rows)))
      print("len(element_title_index)="+str(len(element_title_index))+":"+str(element_title_index))
      for i in range(len(element_rows)):
         print("i="+str(i))
         string_rows.append(element_title[element_title_index[i]].text+";"+element_rows[i].text)
      sleep(3)
      driver.find_element_by_class_name('lnk-page.lnk-page-next').click()
      number=number+1
   except :
      sleep(3)
      element_rows=driver.find_elements_by_class_name('res-text')
      element_title=driver.find_elements_by_class_name('op-excerpt')
      element_title_index=list(range(0,len(element_rows)*2,2))
      print("exception occurred")
      print("element_rows="+str(len(element_rows)))
      print("string_rows="+str(len(string_rows)))
      print("len(element_title_index)="+str(len(element_title_index))+":"+str(element_title_index))
      for i in range(len(element_rows)):
         print("i="+str(i))
         string_rows.append(element_title[element_title_index[i]].text+";"+element_rows[i].text)
      sleep(3)
      driver.find_element_by_class_name('lnk-page.lnk-page-next').click()
      number=number+1


with open('myfile.txt', 'a') as fd:
      try:
         for i in range(len(string_rows)):
            fd.write(string_rows[i]+"\n")
      except Exception as e:
         ...

