import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import os
import json
import time

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/81.0.4044.138 Safari/537.36"}


def write_file(path, content):
    """
    寫入檔案
    :param path: 路徑目錄
    :param content: 網頁截取下來的資訊
    :return: None
    """
    write_file_time = time.time()
    file_name = path + "/" + content["metadate_map"]["標題"].replace("/", "slash") + ".json"
    print(file_name)
    if not os.path.exists(path):
        os.mkdir(path)
    with open(file_name, "w", encoding="utf8") as file:
        json.dump(content, file, ensure_ascii=False)
    write_file_time_end = time.time()
    print("write ", file_name, "time : ", write_file_time_end - write_file_time)


def get_content(url) -> dict:
    """
    :param url: 需取得內容的網址
    :return: 內容string
    """

    # print(url)
    r = requests.get(url, headers=header)
    # print(r.text)
    bss = BeautifulSoup(r.text, "html.parser").select_one("div#main-content")

    # 取得文章的標題、作者、時間
    # print(bss)
    # print(bss.prettify())
    # print(bss.select("div.article-metaline"))
    metadate_map = {s.select("span.article-meta-tag")[0].text: s.select("span.article-meta-value")[0].text for s in
                    bss.select("div.article-metaline")}
    # for s in bss[0].select("div.article-metaline"):
    #     print(s.select("span.article-meta-tag")[0].text)
    #     print()
    # print(bss[0].select("div.article-meta-value"))
    # print(metadate_map)
    content = bss.text  # .replace("\\n", "\n").replace("\\n\\n", "\n")
    content_dict = {"metadate_map": metadate_map, "content": content[0: content.index("發信站: ")],
                    "push_data": get_push_data(bss=bss)}
    return content_dict


def get_push_data(bss) -> dict:
    # print("________________________push")
    count = 0  # 推文id流水
    push_data = defaultdict(lambda: 0)  # 推文資料
    # print(bss.select("div.push"))
    push_sum = {"→": 0, "噓": 0, "推": 0}
    push_data["push_sum"] = push_sum
    for p in bss.select("div.push"):
        push_tag = p.select_one("span.push-tag").text.strip()  # 推 噓
        push_id = p.select_one("span.push-userid").text  # 推文者id
        push_content = p.select_one("span.push-content").text  # 推文內容
        push_time = p.select_one("span.push-ipdatetime").text  # 推文時間
        push_sum[push_tag] += 1  # 推文計數
        # print(push_tag, push_sum)
        push_data[count] = {"push_tag": push_tag, "push_id": push_id, "push_content": push_content,
                            "push_time": push_time}
        # push_data["push_sum"] = push_sum
        count += 1
    # print(push_data)
    return push_data




def main():
    time_index = time.time()
    url = "https://www.ptt.cc/bbs/movie/index.html"
    res = requests.get(url=url, headers=header)
    print("status code:", res.status_code)
    bs = BeautifulSoup(res.text, "html.parser")
    step1_time = time.time()
    print("index time:", step1_time - time_index)
    page_num = 2

    for i in range(0, page_num):
        # 取得文章標題

        # 取得網域
        server_name = res.url.replace("bbs/movie/index.html", "")
        # print(server_name)
        # 組合文章內容的url
        # 組合文章標題: 文章內容url
        result_map = {s.text: server_name + s["href"] for s in bs.select("div.title a")}
        # print(result_map)

        title_content_map = {}
        # 用url取得每篇文章內容
        for title, content_url in result_map.items():
            # print(title, contet_url)
            content_time = time.time()
            content = get_content(content_url)
            content_time_off = time.time()
            print(title, "spend time:", content_time_off-content_time)
            title_content_map[title] = content
            write_file("./test", content)
            # print(title_content_map)
            # print(json.dumps(title_content_map))
            # break
        # print(title_content_map)
        pre_page = bs.select("div.action-bar div.btn-group.btn-group-paging a")[1]["href"]
        pre_page_url = server_name+pre_page
        bs = BeautifulSoup(requests.get(url=pre_page_url, headers=header).text, "html.parser")


if __name__ == "__main__":
    main()