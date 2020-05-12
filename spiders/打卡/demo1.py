from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import re

driver = webdriver.Chrome(executable_path='D:\ChromeCoreDownloads\chromedriver.exe')

reg = re.compile('[=;]')
s = 'ASP.NET_SessionId=sh1c1eftwobqxa245oa1trn3; __RequestVerificationToken=2QVja35zdIL40lhMfA9q83LhLslfJ4SPso-P7jcCjlwlRM1RGfbm7vGfBmZ50zQTU47cYRAaZSaJz8nxU4ltaxM1qCy1bF5cA8goKzbsm8E1; .ASPXFORMSAUTHYZY=C8F14161AC03A35F0F12638E29E37C6F906B58C35A4E01BEEAECB9125AB82503EE44710CFE464EFE8AF7510AC3C0BE3F7E5536288AEEE95D0B5514C199EBEB7A53836FD462B124B0363BF0E00E4CE8B7B74FB9C7D0F44A4BA97017DBB9759C032582D94C9C0873DE20F34BA2BAAB2163'
res = re.split(reg, s)
key = []
value = []
for i in range(len(res)):
    if i % 2:
        value.append(res[i])
    else:
        key.append(res[i])

ret = [(i, j) for i, j in zip(key, value)]

ret = dict(ret)
ret['__RequestVerificationToken'] = 'P7jcCjlwlRM1RGfbm7vGfBmZ50zQTU47cYRAaZSaJz8nxU4ltaxM1qCy1bF5cA8goKzbsm8E1'





driver.add_cookie(cookie_dict=ret)
driver.get('http://39.98.190.134:81/Report/Reported')

# button_jinridaka = WebDriverWait(driver, 5, 0.5).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/p/a')))
#
# driver.execute_script('arguments[0].click();', button_jinridaka)
