from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

browser=webdriver.Firefox()

browser.get('https://yelpcamp-project.herokuapp.com/')
browser.find_element_by_xpath('//a[@href="/campgrounds"]').click()
browser.find_element_by_xpath('//a[@href="/login"]').click()
username = input("Enter username: ")
password = input("Enter password: ")
print('=================================================================') #separator, doesn't mean anything
browser.find_element_by_xpath('//input[@name="username"]').send_keys(username)
browser.find_element_by_xpath('//input[@name="password"]').send_keys(password)
browser.find_element_by_class_name('btn-primary').click()

def populate(name, image, description):
        browser.find_element_by_xpath('//input[@name="name"]').send_keys(name)
        browser.find_element_by_xpath('//input[@name="image"]').send_keys(image)
        browser.find_element_by_xpath('//input[@name="description"]').send_keys(description)
        browser.find_element_by_class_name('btn-primary').click()

choice = "Yes"

while True:
    if choice == 'Yes':
        name = input("Enter name: ")
        image = input("Enter image url: ")
        description = input("Enter description: ")
        browser.find_element_by_xpath('//a[@href="/campgrounds/new"]').click()
        populate(name, image, description)
    elif choice == 'No':
         browser.quit()
         break
    else:
        print('Invalid')
    choice = input('Whether continue? Yes/No')



