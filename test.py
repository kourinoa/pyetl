import requests
from bs4 import BeautifulSoup

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/81.0.4044.138 Safari/537.36"}


def main():
    url1 = "http://e5918cb4.ngrok.io/practice/10"
    ss = requests.session()
    res1 = ss.get(url=url1, headers=header)
    bs = BeautifulSoup(res1.text, "html.parser")
    print(bs)

    hedden_date = {s["name"]: s["value"] for s in bs.select("form input") if s["type"] == "hidden"}
    print(hedden_date)

    hedden_date["pwd"] = "kkk"

    print(bs.select("form")[0]["action"])
    res2 = ss.post(url="http://e5918cb4.ngrok.io" + bs.select("form")[0]["action"], data=hedden_date)
    print(res2.text)


if __name__ == "__main__":
    main()
