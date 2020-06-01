import requests
import json
from myutil import get_header
import os

url = "https://www.dcard.tw/service/api/v2/forums/funny/posts?limit=10&before=233767256"
art_url = "https://www.dcard.tw/f/funny/p/233767255"

def get_article(aurl):
    ss = requests.session()
    req = ss.get(url=url, headers=get_header())
    return req.text

def main():
    ss = requests.session()
    req = ss.get(url=url, headers=get_header())
    json_data = json.loads(req.text)
    # print(json_data)
    for k in json_data:
        print(k["id"])
        artl_id = k["id"]
        print(k["title"])
        artl_title = k["title"]
        path = "./test/" + artl_title.replace("?", "qMark")
        if not os.path.exists(path):
            os.mkdir(path)
        for img in k["mediaMeta"]:
            img_url = img["url"]
            data_name = img_url.split("/")
            file_name = data_name[len(data_name)-1]
            print(img_url)
            # 判斷是不是圖
            if file_name.find("jpeg") != -1:
                # 寫入檔案
                res_img = ss.get(img["url"])  # 發出請求
                img_content = res_img.content  # 圖片內容
                with open(path+"/"+file_name, "wb") as img_file:
                    img_file.write(img_content)
        print("-------------------------------------")
    # article = get_article(art_url)
    # print(article)

if __name__ == "__main__":
    main()
