from urllib import request, response
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    url = "https://www.ptt.cc/bbs/Baseball/index.html"
    head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/81.0.4044.138 Safari/537.36"}
    req = request.Request(url=url, headers=head)

    resp = request.urlopen(req)  # type: response
    bs = BeautifulSoup(resp.read(), "html.parser")  # type: BeautifulSoup

    title_list = [s.text for s in bs.select("div.r-ent div.title a")]
    print(title_list)


if __name__ == "__main__":
    main()
