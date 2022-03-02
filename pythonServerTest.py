from selenium import webdriver
from selenium.webdriver.common import keys


#Runs an automated test in Chrome to check the response when the form is submitted is as expected
class pythonServerTest():

	def enterName(self):
		driver = webdriver.Chrome('/usr/bin/chromedriver')
		driver.get("http://localhost:8080/")
		nameBox = driver.find_element_by_id("name")
		submitButton = driver.find_element_by_name("submit")
		nameBox.send_keys("Martha")
		submitButton.click()
		successText = driver.find_elements_by_id("success")
		assert(successText[0].text) == "Hello Martha"


test = pythonServerTest()
test.enterName()