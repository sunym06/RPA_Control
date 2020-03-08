import time

from selenium import webdriver

url = r'http://localhost:8000/kou.html'
driver = webdriver.Chrome()
driver.get(url)
gongsi = '//div[@class="yd-list-title"]/span'
dizhi =  '//div[@class="demo-list-price"]'
num =  '//div[@class="yd-list-other"]/div/div[2]/span'
# r = driver.find_elements_by_xpath(gongsi)
# addr = driver.find_element_by_xpath(dizhi)
# n = driver.find_element_by_xpath(num)

l = len(driver.find_elements_by_xpath(gongsi))
li = []
for i in range(1,l):
    ss = driver.find_elements_by_xpath(dizhi)[i]
    li.append(ss.get_attribute('innerHTML'))
print(li)
# print(l)
# for i in range(1, l):
#     g = driver.find_elements_by_xpath(gongsi)[i]
#     a = driver.find_elements_by_xpath(dizhi)[i]
#     n = driver.find_elements_by_xpath(num)[i]
#     print(str(i) + 'company: '+ g.get_attribute('innerHTML') + 'address: '+ a.get_attribute('innerHTML') + ' num: ' + n.get_attribute('innerHTML'))

url_g = r'https://www.amap.com/dir?from%5Bname%5D=%E6%88%91%E7%9A%84%E4%BD%8D%E7%BD%AE&from%5Bid%5D=dirmyloc-from&from%5Badcode%5D=110000&from%5Bpoitype%5D=&from%5Blnglat%5D=116.52627%2C40.08209&from%5Bmodxy%5D=116.52627%2C40.08209&to%5Badcode%5D=110108&to%5Bname%5D=%E5%AD%A6%E6%B8%85%E5%98%89%E5%88%9B%E5%A4%A7%E5%8E%A6&to%5Bid%5D=B0FFHS0VAX-to&to%5Bpoitype%5D=120201&to%5Blnglat%5D=116.35296900000003%2C40.014472&to%5Bmodxy%5D=116.352233%2C40.01524&type=walk&policy=0&dateTime=now'
driver.get(url_g)
driver.implicitly_wait(20)
time.sleep(3)
driver.find_element_by_id('dir_to_ipt').clear()
for i in li:
    driver.find_element_by_id('dir_to_ipt').send_keys(i)
    time.sleep(3)
    driver.find_element_by_class_name('dir_submit').click()
    r = driver.find_element_by_xpath('//div[@class="planTitle open"]/p').get_attribute('innerHTML')
    print(r)
# for i in com:
#     c = i
#     print(c)
# driver.find_element_by_class_name('sdf').get_attribute('innerHTML')

