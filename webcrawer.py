import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

Driver_PATH = "C:/Users/user/OneDrive - 東吳大學/python/edgedriver_win64/msedgedriver.exe"
CSV = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/Judgment_Reasoning.csv"
# # 釋字號模組
# Judgment_NO = 0
# for i in range(8,821,1):
#     Judgment_NO = i
#     Jugment_Xpath = '//*[@id="Print_area"]/div[3]/div/ul/li['+str(i)+']/a'
#     print(Judgment_NO)
#     print(Jugment_Xpath)
    
driver = webdriver.Edge(Driver_PATH)
driver.get("https://cons.judicial.gov.tw/judcurrent.aspx?fid=2195")
Judgment_Reasoning = []
Judgment_NO = 0
Judgment_Xpath = ""

Index = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="Print_area"]/div[3]/div/ul/li[820]/a'))
)

for i in range(8,821,1):
    Judgment_NO = i
    Judgment_Xpath = '//*[@id="Print_area"]/div[3]/div/ul/li['+str(i)+']/a'
    print(821-i)
    # print(Judgment_Xpath)

    In = driver.find_element_by_xpath(Judgment_Xpath)
    In.click()
    try:
        Reasoning = driver.find_element_by_xpath('//*[@id="section3"]/li[2]')
        # print(Reasoning.text)
    except Exception:
        print("不存在理由書,抓取解釋文")
        Reasoning = driver.find_element_by_xpath('//*[@id="section2"]/li[2]')
        # print(Reasoning.text)
    Judgment_Reasoning.append(Reasoning.text)    
            
    driver.back()
print("幹你娘跑完拉!")


f = open(CSV, 'w', encoding='utf-8-sig',newline=(""))
csv_writer = csv.writer(f)
for i in Judgment_Reasoning:
    csv_writer.writerow([i])
f.close()
# with open(CSV,'a',encoding='utf-8-sig',newline="") as fp:
#     for i in Judgment_Reasoning:
#         fp.write(i+ '\n')



    



