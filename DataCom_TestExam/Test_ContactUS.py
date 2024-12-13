from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import requests


class TestContactUs:
     @pytest.fixture(scope="class")
     def setup(self):
         driver = webdriver.Chrome()
         driver.maximize_window()
         yield driver
         driver.quit()

     def test_page_title(self, setup):   #Validate page Title correctly
         driver = setup
         url = "https://datacom.com/nz/en/contact-us"

         driver.get(url)
         assert "Contact Us — Get In Touch" in driver.title, f"Unexpected page title: {driver.title}"
         print(driver.title)

     def test_page_controls(self, setup):  #Validate controls of buttons, links and functionality
       driver = setup
       driver.get("https://datacom.com/nz/en/contact-us")


       button = driver.find_element(By.ID, "cmp-mrkto-modal-thank-you")
       assert button.is_displayed() and button.is_enabled(), "Contact button not working"
       print(" Contact button is working")

       button.click()
       WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.XPATH, "//h3[text()='Contact us']"))
       )
       success_message = driver.find_element(By.ID, "FirstName")
       assert success_message.is_displayed(), "Contact us message not displayed"
       print("Contact us message was displayed \t")

     def test_find_Bugs(self, setup): # Validate for missing images
       driver = setup
       driver.get("https://datacom.com/nz/en/contact-us")

       images = driver.find_elements(By.TAG_NAME, "img")
       for img in images:
           src = img.get_attribute("src")
           if src:
               response = requests.get(src)
               assert response.status_code == 200, f"Broken image: {src}"
               print("There is no broken images")


