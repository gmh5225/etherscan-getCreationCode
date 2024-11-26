#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://etherscan.io/address/"

def main():
    ## address = str(input("Please input an address: ").strip())
    address = "0x7a58c0be72be218b41c608b7fe7c5bb630736c71"
    url = BASE_URL + address
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    #print("456")
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    #print("123")
    creationcode_div = soup.find("div", { "id": "verifiedbytecode2" })
    if creationcode_div:
        print(creationcode_div.text)
    else:
        print("not found")

if __name__ == "__main__":
    main()
