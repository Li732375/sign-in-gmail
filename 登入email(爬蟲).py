##目前確認僅能執行 yahoo 的
## gmail 請改用另一隻程式執行
#測試完成
#介面完成

from selenium import webdriver
from os import system
import time, stdiomask, copy

#帳號
account = 'lee6894661@yahoo.com.tw'#input('帳號?')
#密碼
password = 'li6894661'#stdiomask.getpass(prompt = '密碼：', mask = '密')

pointM = account.find('@')
pointC = account.find('com')
company = account[pointM + 1: pointC - 1]


if company == 'gmail' or company == 'Gmail':
    site = 'https://mail.google.com/'
elif company == 'yahoo':
    site = 'https://login.yahoo.com/?.src=ym&.lang=zh-Hant-TW&.intl=tw&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.src%3Dfp'

# 關閉通知
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument('disable-infobars')
#1背景執行
#option.add_argument('headless')

# 啟動selenium 務必確認driver 檔案跟python 檔案要在同個資料夾中
driver = webdriver.Chrome(options = options)
driver.get(site)
time.sleep(1.5)

if company == 'yahoo':
    #先點掉保持登入 
    context = driver.find_element_by_xpath('//*[@id="login-username-form"]/div[3]/div[1]/span/label')
    context.click()
    time.sleep(1.3)
    
    #輸入email
    context = driver.find_element_by_css_selector('#login-username')
    context.send_keys(account) 
    time.sleep(1.5)

    #點擊下一步
    context = driver.find_element_by_css_selector('#login-signin')
    context.click()
    time.sleep(2.5)

    #輸入password
    context = driver.find_element_by_css_selector('#login-passwd')
    context.send_keys(password)
    time.sleep(2)

    #點擊下一步
    context = driver.find_element_by_css_selector('#login-signin')
    context.click()
    time.sleep(5)
    
    #需加入點擊，關於稍後提醒的操作頁面
    #正常登入的網址:https://mail.yahoo.com/d/folders/1?.src=fp&guce_referrer=aHR0cHM6Ly9sb2dpbi55YWhvby5jb20v&guce_referrer_sig=AQAAAFjDvIBsnRdus1AqhBatfLaG2Gy55ykvb2em5TzQICaE62BCa90FUvhBUMp-pyEDuub_XAKKwAgc6cR38SLMFBATclg-yTgQVcYPLdtUGob-roCI7saDrXoBCfDH5ZQ7gw2_qRxHgME0CznS2Cgl5U4jWMUGpsg06jORqYGcQbZ2
    #提醒頁面的網址:
    
    #捕捉內容
    alldata = list()#儲存所有資料
    data = list()#儲存單筆資料
    catchMany = 10#要捕捉的筆數
    
    for i in range(3, catchMany + 3):
        try:
            try:
                try:
                    #data.extend(driver.find_element_by_xpath('目標元素的 xpath').text)
                    data.append(driver.find_element_by_xpath('//*[@id="mail-app-component"]/div[1]/div/div[2]/div/div/div[3]/div/div[1]/ul/li[' + str(i) + ']/a/div/div[1]/div[2]/span/span').text)
                except:
                    data.append(driver.find_element_by_xpath('//*[@id="mail-app-component"]/div[1]/div/div[2]/div/div/div[3]/div/div[1]/ul/li[' + str(i) + ']/a/div/div[1]/div[2]/span/strong').text)
                
                data.append(driver.find_element_by_xpath('//*[@id="mail-app-component"]/div[1]/div/div[2]/div/div/div[3]/div/div[1]/ul/li[' + str(i) + ']/a/div/div[2]/div[1]/div[1]/span[1]').text)
                data.append(driver.find_element_by_xpath('//*[@id="mail-app-component"]/div[1]/div/div[2]/div/div/div[3]/div/div[1]/ul/li[' + str(i) + ']/a/div/div[2]/div[3]/time/span').text)
                alldata.append(copy.copy(data))
                data.clear()
            
            except:
                data.append(driver.find_element_by_xpath('//*[@id="mail-app-component"]/div[1]/div/div[2]/div/div/div[3]/div/div[1]/ul/li[' + str(i) + ']/div/span').text)
                alldata.append(copy.copy(data))
                data.clear()
        except:
            data.append(driver.find_element_by_xpath('//*[@id="mail-app-component"]/div[1]/div/div[2]/div/div/div[3]/div/div[1]/ul/li[' + str(i) + ']/div').text)
            alldata.append(copy.copy(data))
            data.clear()

    datalen = len(alldata)
    
    for i in range(datalen):
        if len(alldata[i]) == 1:
            print('\n- ', end='')
            print(alldata[i])
        else:
            print(alldata[i])
          
    #點擊頭像
    context = driver.find_element_by_xpath('//*[@id="ybar-inner-wrap"]/div[2]/div/div[3]/div[1]/div/label')
    context.click()
    time.sleep(2)
    
    #登出
    context = driver.find_element_by_xpath('//*[@id="ybarAccountMenuBody"]/a[3]')
    context.click()
    time.sleep(2)
'''       
elif company == 'gmail' or company == 'Gmail':
    
    #輸入email
    context = driver.find_element_by_css_selector('#identifierId')
    context.send_keys(account) 
    time.sleep(1.8)

    #點擊繼續
    context = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
    context.click()
    time.sleep(2)

    #輸入password
    context = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    context.send_keys(password)
    time.sleep(0.5)

    #點擊繼續
    context = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
    context.click()
    time.sleep(3)
    
    #捕捉內容
    alldata = list()#儲存所有資料
    data = list()#儲存單筆資料
    catchMany = 10#要捕捉的筆數
    
    for i in range(3, catchMany + 3):
        #data.extend(driver.find_element_by_xpath('目標元素的 xpath').text)
        #
        data.append(driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[7]/div/div[1]/div[3]/div/table/tbody/tr[1]/td[5]/div[2]/span/span').text)
        data.append(driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[7]/div/div[1]/div[3]/div/table/tbody/tr[1]/td[6]/div/div/div/div/span/span').text)
        data.append(driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[7]/div/div[1]/div[3]/div/table/tbody/tr[1]/td[9]/span').get_attribute('title'))
        alldata.append(copy.copy(data))
        data.clear()
        
    datalen = len(alldata)
    
    for i in range(datalen):
        print(alldata[i])
          
    #點擊頭像
    context = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[3]/div[1]/div[2]/div/a/img')
    context.click()
    time.sleep(2)
    
    #登出
    context = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[4]/div[4]/a')
    context.click()
    time.sleep(2)
'''
#關閉瀏覽器全部標籤頁
driver.quit()

