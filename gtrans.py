import chromedriver_binary
#
from selenium import webdriver
from time     import sleep

lf = 'pt'
lt = 'en'

text = 'ola! está tudo bem?'

# open browser
driver = webdriver.Chrome()

# goto google translate
driver.get(f'http://translate.google.com/#{lf}/{lt}/')

#driver.execute_script(f"document.getElementById('source').value = '{text}'; ")

textarea = driver.find_element_by_id('source')
textarea.send_keys(text)
sleep(1)
#/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/span
result = driver.find_element_by_xpath("//span[contains(@class, 'tlid-translation')]")
for each in result.find_elements_by_xpath('./span'):
    print(each.text)

sleep(2)

textarea.clear()
sleep(2)

driver.close()



# if not brows:
#                 brows = get_chrome()
#             if part.startswith('http') and '//' in part and len(part.strip().split()) == 1:
#                 result[part] = part
#                 continue
#             url = f'http://translate.google.com/#{lf}/{lt}/'
#             brows.get(url)
#             sleep(0.5)
#             corpart = part.replace("'", "\\'")
#             brows.execute_script(f"document.getElementById('source').value = '{corpart}'; ")
#             textarea = brows.find_element_by_id('source')
#             textarea.click()
#             mobile = True
#             bottons = ['//*[@id="gt-submit"]', '//div[@class="go-wrap"]']
#             for b in bottons:
#                 try:
#                     brows.find_element_by_xpath(b).click()
#                     if b == '//*[@id="gt-submit"]':
#                         mobile = False
#                     continue
#                 except Exception:
#                     pass
#             tr_part, c = '', 0
#             while not tr_part and c < 10:
#                 sleep(0.5)
#                 if mobile:
#                     elements = html.fromstring(brows.page_source).xpath(
#                         "//span[contains(@class, 'tlid-translation')]")
#                     temp = ' '.join([html.tostring(t).decode('utf-8') for t in elements])
#                     tr_part = BeautifulSoup(temp, 'html.parser').get_text()
#                 else:
#                     elements = html.fromstring(brows.page_source).xpath(
#                         '//span[@id="result_box"]')
#                     temp = ' '.join([html.tostring(t).decode('utf-8') for t in elements])
#                     tr_part = BeautifulSoup(temp, 'html.parser').get_text()
#                 if tr_part == 'Translating...':
#                     tr_part = ''
#                 c += 1
#             result[part] = re.sub(r"(&.{2,8}?;)", " ", tr_part)
#         except Exception as e:
#             print(type(e), e)
#             result[part] = ''
#     if brows:
#         brows.stop_client()
#         brows.close()
#         brows.quit()
#         del (brows)