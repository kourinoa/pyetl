import jieba
import os
import json
from collections import defaultdict

def cut_text_file():
    file_list = [file for file in os.listdir("./test") if file.find("json") != -1]
    for file in file_list:
        file_path = "./test/" + file
        with open(file_path, "r", encoding="utf8") as text_file:
            s = json.loads(text_file.read())["content"]
            adict = defaultdict(lambda: 0)
            for v in jieba.cut(s, cut_all=True):
                if len(v) > 2:
                    adict[v] += 1
            # bdict = defaultdict(lambda: 0)
            # print(" | ".join(jieba.cut(s, cut_all=False)))
            # print(" | ".join(jieba.cut(s)))
            # print(" | ".join(jieba.cut_for_search(s)))
            # print(adict)
        alist = [(k, v) for k, v in adict.items()]
        alist.sort(key=lambda t: t[1], reverse=True)
        print(alist)
        break


def main():
    s = "大家好，我叫小賀，今天來中央大學上課，非常開心"
    jieba.load_userdict("./test/mydict.txt")
    print("|".join(jieba.cut(s)))


if __name__ == "__main__":
    main()