import requests
import os
import json
from bs4 import BeautifulSoup
from myutil import get_header

url = "https://buzzorange.com/techorange/wp-admin/admin-ajax.php"  # action=fm_ajax_load_more&nonce=d8c08f1381&page=6


def main():
    ss = requests.session()
    post_data = {"action": "fm_ajax_load_more", "nonce": "d8c08f1381", "page": 6}
    res = ss.post(url="https://buzzorange.com/techorange/wp-admin/admin-ajax.php", headers=get_header(), data=post_data)
    res_json = json.loads(res.text)
    soup = BeautifulSoup(res_json["data"], "html.parser")
    # print(soup.prettify())
    print(soup.select("a"))
    print({a.text: a["href"] for a in soup.select("a[rel]")})


if __name__ == "__main__":
    main()
