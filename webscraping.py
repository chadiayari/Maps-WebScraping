from selenium import webdriver
import json
import time
from selenium.webdriver.common.keys import Keys

def writeToJSONFile(data):
	with open('./destionation.json', 'a') as fp:
		json.dump(data, fp)

#def webScraping(destination):
PATH = "C:\Program Files (x86)\chromedriver.exe" ;
driver = webdriver.Chrome(PATH) ;
destination = input("Please enter your desired Destination: ")
	
driver.get("https://www.google.com/maps/");
searchbox= driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]')
searchbox.send_keys(destination)
searchbox.send_keys(Keys.ENTER)

time.sleep(5) ; 

elements=driver.find_elements_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[5]/div');
data ={}

for i in range (1,39,2):
	try:
		data['name'] = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div['+str(i)+']/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/span').text;
	except Exception as e:			
		data['name'] = "Doesn't exist yet"
	try:
		data['rating'] = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div['+str(i)+']/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/span[2]/span[2]/span[1]').text;
	except Exception as e:
		data['rating'] = "No Rating"
	try:
		data['loc'] =  driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div['+str(i)+']/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[1]/span[2]/jsl/span[2]').text;
	except Exception as e:
		data['loc'] = "No Location Given"
	try:
		data['phone']= driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div['+str(i)+']/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[2]/span[3]/jsl/span[2]').text ;
	except Exception as e:
		data['phone']="No Phone Given"
	if (data['name']=="Doesn't exist yet"):
		driver.quit();  
	
	writeToJSONFile(data);
