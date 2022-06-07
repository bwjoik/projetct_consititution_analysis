import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# 引擎與檔案路徑設置
Driver_PATH = "C:/Users/user/OneDrive - 東吳大學/python/edgedriver_win64/msedgedriver.exe"
CSV = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/JR_text.csv"

driver = webdriver.Edge(Driver_PATH)
driver.get("https://cons.judicial.gov.tw/judcurrent.aspx?fid=2195")
Judgment_Reasoning = []
Judgment_NO = 0
Judgment_Xpath = ""

# 爬蟲開始
# 進入司法院網站 找到813的按鈕
Index = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="Print_area"]/div[3]/div/ul/li[820]/a'))
)
#抓取回圈
for i in range(8,821,1):
    Judgment_NO = i
    Judgment_Xpath = '//*[@id="Print_area"]/div[3]/div/ul/li['+str(i)+']/a'
    print(821-i)
  
    In = driver.find_element_by_xpath(Judgment_Xpath)
    In.click()
    time.sleep(2)
    try:
        Reasoning = driver.find_element_by_xpath('//*[@id="section3"]/li[2]')
    except Exception:
        print("不存在理由書,抓取解釋文")
        Reasoning = driver.find_element_by_xpath('//*[@id="section2"]/li[2]')
    Judgment_Reasoning.append(Reasoning.text)    
    driver.back()
print("幹你娘跑完拉!")
print("開始寫入......")

#將list的資料逐行輸入CSV
f = open(CSV, 'w', encoding='utf-8-sig',newline=(""))
csv_writer = csv.writer(f)
for i in Judgment_Reasoning:
    csv_writer.writerow([i])
    time.sleep(1)
print("寫入完成！")
f.close()



    



