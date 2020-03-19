import selenium
from selenium import webdriver
#import csv

'''
#headless browser- user cannot see browser
from selenium.webdriver.chrome.options import Options
import os
chrome_options = Options()
chrome_options.add_argument("--headless")    # 브라우저를 헤드리스로 사용할거임
chrome_options.add_argument("--window-size=1920x1080")     # 브라우저 크기
chrome_options.add_argument("disable-gpu")            
'''

#open the page
driver = webdriver.Chrome(executable_path = 'C:/Users/2017320158양혜림/Desktop/2020-1/teamproj/chromedriver_win32/chromedriver') #headless로 하려면 (chrome_options = chrome_options)
driver.get('https://store.naver.com/restaurants/list?entry=pll&filterId=s11591594&query=%EC%88%99%EB%8C%80%20%EB%A7%9B%EC%A7%91&sessionid=k9rDDZHepGQHsQP2fvq4%2BA%3D%3D')

'''
#open output file
f = open('write.txt','w', encoding = 'UTF8')
'''

#get store names (in one page)
elemlst = driver.find_elements_by_class_name("name")

#go to each store page (in one original search page)
for elem in elemlst:
    elem.click()
    driver.switch_to.window(driver.window_handles[-1])

    #get store name
    store = driver.find_element_by_class_name("name") 
    print(store.text+' : ')

    #get menu names
    menulst = driver.find_elements_by_class_name("menu")
    for menu in menulst:
        menu = menu.find_element_by_class_name("name")
        print(menu.text+', ')

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

'''
#get examples
cs = []
while cs == []:
    exs = driver.find_elements_by_class_name("text") #webelement들의 list를 뱉음
    for ex in exs:
        if ex.get_attribute('lang') == 'en':
            #print(ex.text)
            cs.append(ex.text)

#output to txt file
_ = '' if word[-1] == '\n' else '\n'
f.write('***\n'+word+_+'***\n')
for c in cs:
    f.write(c+'\n')



#close files
f.close()
'''