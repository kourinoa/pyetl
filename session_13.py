import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/81.0.4044.138 Safari/537.36"}


def main():
    ss = requests.session()
    res = ss.get(url=url, headers=header)
    bs = BeautifulSoup(res.text, "html.parser")
    btn = bs.select_one("button.btn-big")
    print(btn["name"], btn["value"])
    post_data = {btn["name"]: btn["value"]}

    form = bs.select_one("form")
    print(form["action"])

    res2 = ss.post(url="https://www.ptt.cc" + form["action"], headers=header, data=post_data)
    print(res2.url, res2.status_code)
    print(res2.text)

    res3 = ss.get(url=url, headers=header)
    print(res3.url, res3.status_code)
    print(res3.text)


if __name__ == "__main__":
    main()
