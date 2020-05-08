from selenium import webdriver
import time

USERNAME = ""
PASSWORD = ""

driver = webdriver.Chrome(executable_path = 'C:\Drivers\Chrome_driver\chromedriver')
driver.get("https://www.facebook.com")

user_name_box = driver.find_element_by_id("email")
user_name_box.send_keys(USERNAME)

password_box = driver.find_element_by_id("pass")
password_box.send_keys(PASSWORD)

login_box = driver.find_element_by_id('loginbutton') 
login_box.click()
print("login successful!!!")
time.sleep(3)
right_buttons = driver.find_elements_by_xpath("//*[@class= 'cxgpxx05 sj5x9vvc']")
right_buttons[1].click()
time.sleep(1)
birthday_boxes = driver.find_elements_by_xpath("//*[contains(@aria-label, 'Birthdays')]//*[@class='_1mf _1mj']")
count = 0
for els in birthday_boxes:
    try:
        count +=1
        els.send_keys("Happy birthday!")
        els.send_keys(Keys.RETURN) 
        print("Birthday Wish posted for friend" + str(count)) 
    except:
        print("couldn't post")

print("done")
time.sleep(2)
driver.close()
