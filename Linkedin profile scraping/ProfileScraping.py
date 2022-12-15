from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By

# Creating a webdriver instance
# This instance will be used to log into LinkedIn
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

# entering username
username  = driver.find_element(By.ID, "username")

# Enter Your Email Address
username.send_keys("khalil.hajri@aiesec.net") 
 
# entering password
pword = driver.find_element(By.ID, "password")

 
# Enter Your Password
pword.send_keys("KHenpersonne25") 

#Submit Button 
driver.find_element(By.XPATH, "//button[@type='submit']").click()

#Intializing linkedin profiles
profile_url = "https://www.linkedin.com/in/kunalshah1/"

driver.get(profile_url)


start = time.time()
initialScroll = 0
finalScroll = 1000
while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    initialScroll = finalScroll
    finalScroll += 1000
    time.sleep(3)
    end = time.time()
    if round(end - start) > 20:
        break
 



#---------------------------------Scrapping--------------------------------------------------
src = driver.page_source
soup = BeautifulSoup(src, 'lxml')
#Getting the header section
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
name_loc = intro.find("h1")
name = name_loc.get_text().strip() #Strip to remove extra spaces
works_at_loc = intro.find("div", {'class': 'text-body-medium'})
works_at = works_at_loc.get_text().strip()

location_loc = intro.find_all("span", {'class': 'text-body-small'})
location = location_loc[1].get_text().strip()
print("Name -->", name,
      "\nWorks At -->", works_at,
      "\nWorks At -->", location)

#Getting experience
experience = soup.find("section", {"id": "ember51"})
print(experience)