from selenium import webdriver
import time
import pymouse
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
#加载选课科目
items={}
f=open('账号.txt','r')
data=[]
f.readline()

for e in f.readlines():
    print(e)
    data.append([e.split()[0], e.split()[1]])

def save(dt):
    f=open('账号.txt','a+')
    f.write(dt[0]+" "+dt[1]+'\n')
    f.close()
    
#注册
def zhuce():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.set_window_size(800,600)
    source=driver.get('https://yxgl-ncdn1.ios.shenshouwl.com/yxgl/h5/index.html?p=gk&ya_game=1113&ya_sn=shenshou_h5&ya_sv=1.0&ya_ssv=V1_0')
    # source=driver.get('https://api.sdk.shenshouwl.com/static/sdk_h5/login.html#app_id=5e3ceece79a108356588601b')
    while 1:
        try:
            driver.switch_to_frame('youai_sdk_frame')
        except:
            pass
        else:
            break

    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="login"]/div/div/form/ul/li[1]/a').click()
    time.sleep(1)
    zh=driver.find_element_by_xpath('//*[@id="register"]/div/form/div/div[1]/div[2]/input').get_attribute('value')
    mm=driver.find_element_by_xpath('//*[@id="register"]/div/form/div/div[2]/div[2]/input').get_attribute('value')
    print(zh,mm)
    driver.find_element_by_xpath('//*[@id="btn-regist"]').click()
    save([zh,mm])
    driver.quit()


def ms():
    m=pymouse.PyMouse()
    p=m.position()
    print(p)
def chucheng():
    pass

def action(t,x,y):
    time.sleep(1)
    m = pymouse.PyMouse()
    for i in range(t):
        m.click(x+3,y+3)  # 鼠标左键点击， 200为x坐标， 100为y坐标
        time.sleep(1)
def go(zh,mm):
    #启动游览器
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.set_window_size(800,600)
    source=driver.get('https://yxgl-ncdn1.ios.shenshouwl.com/yxgl/h5/index.html?p=gk&ya_game=1113&ya_sn=shenshou_h5&ya_sv=1.0&ya_ssv=V1_0')
    # source=driver.get('https://api.sdk.shenshouwl.com/static/sdk_h5/login.html#app_id=5e3ceece79a108356588601b')
    while 1:
        try:
            driver.switch_to_frame('youai_sdk_frame')
        except:
            pass
        else:
            break

#登录
    time.sleep(0.5)
    s1=driver.find_element_by_xpath('//*[@id="js_login_username"]')
    s1.send_keys(zh)  #
    time.sleep(0.5)
    s1=driver.find_element_by_xpath('//*[@id="js_login_password"]')
    s1.send_keys(mm)  #
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="login"]/div/div/form/ul/li[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('// *[ @ id = "home"] / div / div / div[3] / div / div[2] / a').click()
    try:
        driver.find_element_by_xpath('//*[@id="identityCard"]/div/div[2]/a/i').click()
    except:
        pass

    time.sleep(1)
    action(1,520,220)
    time.sleep(1)
    action(1, 456, 490)
    action(1, 413, 466)
    action(1, 456, 489)
    time.sleep(3)

    action(2, 384, 575)
    action(2, 501, 573)
    
    '''463 509'''

    for i in range(5):
        action(2,346+40*i,182)
        action(2, 501, 573)
        time.sleep(3)
        print('有问题加本人QQ2262193538')
        #ms()# 412 245,267 569,236 711  ,381,701 ,
    driver.quit()
    
def qa(zh,mm):
    #启动游览器
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.set_window_size(800,600)
    source=driver.get('https://yxgl-ncdn1.ios.shenshouwl.com/yxgl/h5/index.html?p=gk&ya_game=1113&ya_sn=shenshou_h5&ya_sv=1.0&ya_ssv=V1_0')
    # source=driver.get('https://api.sdk.shenshouwl.com/static/sdk_h5/login.html#app_id=5e3ceece79a108356588601b')
    while 1:
        try:
            driver.switch_to_frame('youai_sdk_frame')
        except:
            pass
        else:
            break

#登录
    time.sleep(0.5)
    s1=driver.find_element_by_xpath('//*[@id="js_login_username"]')
    s1.send_keys(zh)  #
    time.sleep(0.5)
    s1=driver.find_element_by_xpath('//*[@id="js_login_password"]')
    s1.send_keys(mm)  #
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="login"]/div/div/form/ul/li[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('// *[ @ id = "home"] / div / div / div[3] / div / div[2] / a').click()
    try:
        driver.find_element_by_xpath('//*[@id="identityCard"]/div/div[2]/a/i').click()
    except:
        pass

   
    time.sleep(1)
    action(1,520,220)
    time.sleep(1)
    action(1, 456, 490)
    action(1, 413, 466)
    action(1, 456, 489)
    time.sleep(3)
    
    action(1, 301, 210)
    time.sleep(1)
    action(1, 465, 289)
    time.sleep(1)
    action(1, 435, 317)
    time.sleep(1)
    action(1, 419, 279)
    time.sleep(1)
    action(1, 418, 576)
    driver.quit()
    
    pass
def cc(zh,mm):
    #启动游览器
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.set_window_size(800,600)
    source=driver.get('https://yxgl-ncdn1.ios.shenshouwl.com/yxgl/h5/index.html?p=gk&ya_game=1113&ya_sn=shenshou_h5&ya_sv=1.0&ya_ssv=V1_0')
    # source=driver.get('https://api.sdk.shenshouwl.com/static/sdk_h5/login.html#app_id=5e3ceece79a108356588601b')
    while 1:
        try:
            driver.switch_to_frame('youai_sdk_frame')
        except:
            pass
        else:
            break

#登录
    time.sleep(0.5)
    s1=driver.find_element_by_xpath('//*[@id="js_login_username"]')
    s1.send_keys(zh)  #
    time.sleep(0.5)
    s1=driver.find_element_by_xpath('//*[@id="js_login_password"]')
    s1.send_keys(mm)  #
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="login"]/div/div/form/ul/li[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('// *[ @ id = "home"] / div / div / div[3] / div / div[2] / a').click()
    try:
        driver.find_element_by_xpath('//*[@id="identityCard"]/div/div[2]/a/i').click()
    except:
        pass

    time.sleep(1)
    action(1,520,220)
    time.sleep(1)
    action(1, 456, 490)
    action(1, 413, 466)
    action(1, 456, 489)
    time.sleep(3)
    '''
    while 1:
    #for i in range(5):
        time.sleep(0.5)
        ms()# 412 245,267 569,236 711  ,381,701 ,'''
    action(1, 301, 210)
    time.sleep(1)
    action(1, 384, 475)
    time.sleep(1)
    action(1, 415, 495)
    time.sleep(1)
    #结束
    action(2, 408, 541)
    time.sleep(1)
    action(2, 456, 425)
    time.sleep(1)
    #
    action(2, 408, 541)
    time.sleep(1)
    action(2, 408, 505)
    time.sleep(1)
    action(2, 408, 451)
    driver.quit()
    
def ytl(zh,mm):
    #启动游览器
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.set_window_size(800,600)
    source=driver.get('https://yxgl-ncdn1.ios.shenshouwl.com/yxgl/h5/index.html?p=gk&ya_game=1113&ya_sn=shenshou_h5&ya_sv=1.0&ya_ssv=V1_0')
    # source=driver.get('https://api.sdk.shenshouwl.com/static/sdk_h5/login.html#app_id=5e3ceece79a108356588601b')
    while 1:
        try:
            driver.switch_to_frame('youai_sdk_frame')
        except:
            pass
        else:
            break

#登录
    time.sleep(0.5)
    s1=driver.find_element_by_xpath('//*[@id="js_login_username"]')
    s1.send_keys(zh)  #
    time.sleep(0.5)
    s1=driver.find_element_by_xpath('//*[@id="js_login_password"]')
    s1.send_keys(mm)  #
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="login"]/div/div/form/ul/li[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('// *[ @ id = "home"] / div / div / div[3] / div / div[2] / a').click()
    try:
        driver.find_element_by_xpath('//*[@id="identityCard"]/div/div[2]/a/i').click()
    except:
        pass

  
    time.sleep(1)
    action(1,520,220)
    time.sleep(1)
    action(1, 456, 490)
    action(1, 413, 466)
    action(1, 456, 495)
    time.sleep(3)
    '''while 1:
    #for i in range(5):
        action(2,346+40*i,182)
        action(2, 501, 573)
        time.sleep(3)
        print('有问题加本人QQ2262193538')
        ms()# 412 245,267 569,236 711  ,381,701 ,'''
    #排行榜
    action(2, 384, 575)
    action(2, 501, 573)
    
    '''463 509'''

    for i in range(5):
        action(2,346+40*i,182)
        action(2, 501, 573)
        time.sleep(3)
        print('有问题加本人QQ2262193538')
        #ms()# 412 245,267 569,236 711  ,381,701 ,
    
    #返回
    action(1, 501, 573)
    action(1,297,150)
    

    #请安
    action(1, 301, 210)
    time.sleep(1)
    action(1, 465, 289)
    time.sleep(1)
    action(1, 435, 317)
    time.sleep(1)
    action(1, 419, 279)
    time.sleep(1)
    action(1, 418, 576)
    #返回
    action(2,297,150)
    #出城
    action(1, 384, 475)
    time.sleep(1)
    action(1, 415, 500)
    time.sleep(1)
    #结束
    action(2, 408, 545)
    time.sleep(1)
    action(2, 456, 429)
    time.sleep(1)
    #

    time.sleep(1)
    action(2, 408, 505)
    time.sleep(1)
    action(2, 408, 451)

    driver.quit()
    
inpu='0'#input("一条输入0，出城输入1,排行榜输入2，请安输入3:\n")
if inpu=="0":
    for each in data:
        print(1)
        try:
            ytl(each[0],each[1])
        except:
            pass
elif inpu=="1":
    print(1)
    for each in data:
        print(1)
        try:
            cc(each[0],each[1])
        except:
            pass
elif inpu=="2":
    print(1)
    for each in data:
        print(1)
        try:
            go(each[0],each[1])
        except:
            pass
else:
    print(1)
    for each in data:
        print(1)
        try:
            qa(each[0],each[1])
        except:
            pass
    



'''for each in data:
    try:
        go(each[0],each[1])
    except:
        pass
        '''
    

print("运行完成!")
