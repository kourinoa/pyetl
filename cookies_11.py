import requests
from bs4 import BeautifulSoup
import os

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/81.0.4044.138 Safari/537.36"}

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
cookies = {"over18": "1"}


def main():
    res = requests.get(url=url, headers=header, cookies=cookies)
    print(res.text)


if __name__ == "__main__":
    main()
