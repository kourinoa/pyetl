import requests
from bs4 import BeautifulSoup

url = "http://ea4b5b22.ngrok.io/hello_post"
url2 = "https://mops.twse.com.tw/mops/web/index"
url3 = "https://mops.twse.com.tw/mops/web/ajax_t146sb05"

"""
encodeURIComponent: 1
step: 1
firstin: 1
off: 1
keyword4: 
code1: 
TYPEK2: 
checkbtn: 
queryName: co_id
inpuType: co_id
TYPEK: all
co_id: 2330
"""
def main():
    ss = requests.session()
    res = ss.get(url2)
    if res.status_code == 200:
        bs = BeautifulSoup(res.text, "html.parser")
        print(bs.select("form input"))
        hidden_data = {}

        for i in bs.select("form input"):
            try:
                hidden_data[i["name"]] = i["value"]
            except KeyError as err:
                print(err)
                print(i)
                continue

    print(hidden_data)
    hidden_data["co_id"] = "2330"
    res2 = ss.post(url="https://mops.twse.com.tw/mops/web/index", data=hidden_data)
    bs2 = BeautifulSoup(res2.text, "html.parser")
    print(bs2.text)

    # print(res.text)
    #
    # print("______________________")


    # post_date = {"username": "123",
    #              "step": 1,
    #              "firstin": 1,
    #              "co_id": "2330"}
    #
    # res_post = requests.post(url="https://mops.twse.com.tw/mops/web/autoAction", data=post_date)
    # print(BeautifulSoup(res_post.text, "html.parser"))


if __name__ == "__main__":
    main()