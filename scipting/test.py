import requests
from bs4 import BeautifulSoup
import re

url = "https://support.microsoft.com/help/5012647"

res = requests.get(url)
print(res.status_code)

if res.status_code == 200:
    soup = BeautifulSoup(res.content, "html.parser")
    # print(soup)
    
    # Find a paragraph containing the term "SSU" (case-insensitive)
    test = soup.find('p', string="Prerequisite:")
    next_sibling = test.find_next_sibling()
    # print(next_sibling)
    ssufor2019 =next_sibling.find("a").text
    # print(next_sibling.find("a").text)

    lcuwithjunk = soup.find('h1')
    lcutext = lcuwithjunk.text

    kb_match = re.search(r'KB\d+', lcutext)
    if kb_match:
        kb_number = kb_match.group()
        print(kb_number)
    print(f"install the SSU {ssufor2019} then install LCU {kb_number}")
    # SSU= SSU.next_sibling

    # print(SSU)



    # for i in SSU:
    #     href = i.get("href")
    #     if href is not None:
    #         if "kb" in href:
    #             print(href) 
    
    # if SSU:
    # print(SSU)
    # else:
    #     print("Paragraph with 'SSU' not found.")
