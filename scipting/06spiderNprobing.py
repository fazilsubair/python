from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
import requests
import time
import re


while( True):
    url = input("enter the Url: ")

    options = webdriver.ChromeOptions()

    try:
        driver = webdriver.Chrome(options=options)  

        driver.get(url)

        time.sleep(10)

        html_source = driver.page_source

        soup = BeautifulSoup(html_source, 'html.parser')

        # Find all anchor tags
        atags = soup.find_all("a")
        server2019 = soup.find('div' ,string="Windows Server 2019")
        server2022 = soup.find('div' ,string="Windows Server 2022")
        
        KB2019 = server2019.parent.find("a")
        # print(f"the a tag is {KB2019}")

        KB2019link = KB2019.get("href")
        print(f"the link for 2019 : {KB2019link}")

        # print(KB2019.text)

        KB2022 = server2022.parent.find("a")
        # print(f"the a tag is {KB2022}")

        KB2022link = KB2022.get("href")
        print(f"the link for 2022 :  {KB2022link}")

        # print(KB2022.text)

    # for 2019 server 
        # Parse the HTML content
        res = requests.get(KB2019link)
        if res.status_code == 200:
            kb2019soup = BeautifulSoup(res.content, 'html.parser')

            test = kb2019soup.find('p', string="Prerequisite:")
            next_sibling = test.find_next_sibling()
            ssufor2019 = next_sibling.find("a").text

            # print(f"the ssu for 2019 server is {ssufor2019}")

            lcuwithjunk = kb2019soup.find('h1')
            lcutext = lcuwithjunk.text

            kb_match = re.search(r'KB\d+', lcutext)
            # kb_number = "test"
            if kb_match:
                kb_number = kb_match.group()
                # print(kb_number)
            print(f"install the SSU {ssufor2019} then install LCU {kb_number}")
        else:
            print(res.status_code)
        
    #    for server 2022

        res = requests.get(KB2022link)
        if res.status_code == 200:
            kb2019soup = BeautifulSoup(res.content, 'html.parser')
            
            lcuwithjunk = kb2019soup.find('h1')
            lcutext = lcuwithjunk.text

            kb_match = re.search(r'KB\d+', lcutext)
            # kb_number = "test"
            if kb_match:
                kb_number = kb_match.group()
                # print(kb_number)
            print(f"install the 2022 LCU {kb_number}")
        else:
            print(res.status_code)
            
    except WebDriverException as e:
        print(f"WebDriver error: {e}")

    finally:
        # Close the browser
        if 'driver' in locals() and driver is not None:
            driver.quit()
