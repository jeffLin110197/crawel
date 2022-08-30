import csv
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
title_list = []
class main:
    def __init__(self):
        self.option = Options()
        self.option.add_argument('headless')  # 啟動無頭模式
        self.option.add_argument('disable-gpu')  # windows必須加入此行
        self.driver = webdriver.Chrome(options=self.option)
        time.sleep(2)

        self.urls = ['https://www.google.com/search?q=selenium&oq=&aqs=chrome.0.35i39i362l8.4743058j0j7&sourceid=chrome&ie=UTF-8',
       'https://www.google.com/search?q=%E9%86%AC%E5%A4%AA%E9%83%8E&oq=%E9%86%AC%E5%A4%AA%E9%83%8E&aqs=chrome..69i57j46i39i175i199j35i39j0i512l2j0i30l5.9388j0j7&sourceid=chrome&ie=UTF-8']

    def title(self):
        for url in self.urls:
            self.driver.get(url) #抓 醬太郎, selenium 兩個網頁
            for j in range(0, 2): #按2次下一頁
                for i in range(1, 9):
                    soup = BeautifulSoup(self.driver.page_source, 'html.parser') # page_source 顯示網頁的原始碼
                    self.driver.implicitly_wait(1) #等待1秒
                    title_name = soup.select('div[class="yuRUbf"] h3.LC20lb')[i].text #取網頁的標題 [i]抓第 i 個標題 看每個網頁有幾個標題 i 就設幾個
                    global title
                    title = title_name.replace('|', '')
                    self.driver.implicitly_wait(1) #等待1秒
                    title_list.append(title)
                button = self.driver.find_element(By.XPATH, '//*[@id="pnnext"]/span[2]') #定位下一頁標籤的XPATH
                self.driver.implicitly_wait(1) #等待3秒
                button.click()# 按下一頁
                self.driver.implicitly_wait(1) #等待3秒
        print(title_list)
        return title_list
    
    # def openfile(self):
    #     if not os.path.exists('./google_text'):
    #         os.mkdir('./google_text')
    def getcsv(self):
        dic = {"標題": title_list}
        data = pd.DataFrame(dic)
        data.to_csv('./google.csv', encoding='utf8')
    def close(self):
        self.driver.close()


if __name__ == '__main__':
    crawel = main()
    crawel.title()
    crawel.getcsv()
    crawel.close()


