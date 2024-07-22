from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import streamlit as st


#a = st.text_input("Enter the original directory path of Chrome webdriver")
fn = st.text_input("First Name")
ln = st.text_input("Last Name")
pn = st.text_input("Phone Number")
email = st.text_input("Email")
b = st.button("Enter")

def enter_text(driver, field, text):
    retries = 3
    for _ in range(retries):
        try:
            field.clear()  # 清除输入框的现有内容
            field.send_keys(text)  # 输入文本
            # 验证输入是否成功
            if field.get_attribute('value') == text:
                return True
        except Exception as e:
            print(f"Attempt failed with error: {e}")
        time.sleep(1)
    return False
def click_button_with_js(driver, button_xpath):
    # 尝试点击按钮
    button = driver.find_element(By.XPATH, button_xpath)
    
    # 使用 JavaScript 滚动到按钮并点击
    driver.execute_script("arguments[0].scrollIntoView();", button)
    driver.execute_script("arguments[0].click();", button)
if b:
    driver_path = ""  # Adjust the path to your WebDriver
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    
    
    # Open the website
    driver.get('https://msutennis.msu.edu/')  # Replace with the actual URL
    
    
    specific_link = driver.find_element(By.LINK_TEXT, 'Reserve Court Time Online')
    specific_link.click()
    
    
    
    # Locate the element containing the text "Court Reservation 1 Hour"
    wait = WebDriverWait(driver, 10)
    court_reservation_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Court Reservation 1 Hour")]')))
    court_reservation_element.click()
    
    wait = WebDriverWait(driver, 10)
    cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll")))
    cookie_button.click()
    
    wait = WebDriverWait(driver, 10)
    book_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()=" Book now "]]')))
    book_now_button.click()
    
    wait = WebDriverWait(driver, 10)
    panel_header = wait.until(EC.element_to_be_clickable((By.XPATH, '//mat-expansion-panel-header[.//span[contains(text(), "Court Reservation 1 Hour")]]')))
    panel_header.click()
    
    wait = WebDriverWait(driver, 10)
    time_slot_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[.//span[@class="timeslot-start" and contains(text(), "7:00pm")]/following-sibling::span[contains(text(), "8:00pm")]]')))
    time_slot_button.click()
    
    
    wait = WebDriverWait(driver, 20)
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Confirm")]/ancestor::button')))
    #confirm_button.click()
    click_button_with_js(driver, '//span[contains(text(), "Confirm")]/ancestor::button')
        
    
    wait = WebDriverWait(driver, 30)
    fname_field = wait.until(EC.visibility_of_element_located((By.ID, "firstnamePrimary")))
    lname_field = wait.until(EC.visibility_of_element_located((By.ID, "lastnamePrimary")))
    phone_field = wait.until(EC.visibility_of_element_located((By.ID, "phoneNumberPrimary")))
    email_field = wait.until(EC.visibility_of_element_located((By.ID, "emailAddressPrimary")))
    enter_text(driver,fname_field,fn)
    enter_text(driver,lname_field,ln)
    enter_text(driver,phone_field,pn)
    enter_text(driver,email_field,email)
