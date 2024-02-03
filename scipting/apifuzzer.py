import requests
import sys

wordlist_file_path = r"D:\OJT\python\wordlist\test.txt"

with open(wordlist_file_path, 'r') as file:
    wordlist = [line.strip() for line in file]

for word in wordlist:
    res =  requests.get(url=f"https://dummyjson.com/{word}")
    if res.status_code == 200:
        print(res.status_code)
        print(word)
        
    # data = res.json()
    # print(data)