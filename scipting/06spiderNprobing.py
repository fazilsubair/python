from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
import requests
import time
import re

url = "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24493"

# Set up a browser with Selenium
options = webdriver.ChromeOptions()
# options.add_argument('--headless')

try:
    driver = webdriver.Chrome(options=options)  # Updated line

    # Make the initial request
    driver.get(url)

    # Allow some time for JavaScript to load content
    time.sleep(10)

    # Get the page source after JavaScript execution
    html_source = driver.page_source

    # Parse the HTML content
    soup = BeautifulSoup(html_source, 'html.parser')

    # Find all anchor tags
    atags = soup.find_all("a")
    server2019 = soup.find('div' ,string="Windows Server 2019")
    # print(server2019.parent)
    
    KB2019 = server2019.parent.find("a")
    print(f"the a tag is {KB2019}")

    KB2019link = KB2019.get("href")
    print(f"the link is {KB2019link}")

    print(KB2019.text)

    # Iterate through anchor tags and print href attributes
    # for i in atags:
    #     href = i.get("href")
    #     if href is not None:
    #         if "support" in href:
    #             print(href) 

    # Print HTML source before closing the browser
    # print("HTML source before closing the browser:")
    # print(driver.page_source) 


     # Make the initial request
    # driver.get(KB2019link)

    # Allow some time for JavaScript to load content
    # time.sleep(10)

    # Get the page source after JavaScript execution
    # html_source = driver.page_source

    # Parse the HTML content
    res = requests.get(KB2019link)
    if res.status_code == 200:
        kb2019soup = BeautifulSoup(res.content, 'html.parser')
    # print(kb2019soup)

        test = kb2019soup.find('p', string="Prerequisite:")
        next_sibling = test.find_next_sibling()
    # print(next_sibling)
        ssufor2019 = next_sibling.find("a").text

        print(f"the ssu for 2019 server is {ssufor2019}")


        
        lcuwithjunk = kb2019soup.find('h1')
        lcutext = lcuwithjunk.text

        kb_match = re.search(r'KB\d+', lcutext)
        # kb_number = "test"
        if kb_match:
            kb_number = kb_match.group()
            print(kb_number)
        print(f"install the SSU {ssufor2019} then install LCU {kb_number}")




    

except WebDriverException as e:
    print(f"WebDriver error: {e}")

finally:
    # Close the browser
    if 'driver' in locals() and driver is not None:
        driver.quit()
