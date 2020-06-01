from urllib import request, response
import ssl

ssl.create_default_https_context = ssl.create_default_context()


def main():
    url = "https://www.ptt.cc/bbs/Baseball/index.html"
    head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/81.0.4044.138 Safari/537.36"}
    req = request.Request(url=url, headers=head)

    resp = request.urlopen(req)  # type: response
    print(resp.read().decode("utf-8"))


if __name__ == "__main__":
    main()
