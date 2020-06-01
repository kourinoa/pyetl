import pandas as pd
import os
import json


def main():
    path = "./test"
    file_name_list = [file_name for file_name in os.listdir(path) if file_name.find("json") != -1]
    head_list = ["文章編號"]

    with open( path + "/" + file_name_list[0], "r", encoding="utf8" ) as temp:
        temp
        json_file = json.loads(temp.read())
        head_list.extend([k for k in json_file["metadate_map"].keys()])
        push_data = json_file["push_data"]["push_sum"]
        # print(push_data)
        head_list.extend(push_data.keys())
        # print(head_list)
    df = pd.DataFrame(columns=head_list)
    print(df)

    count=0
    for file_name in file_name_list:
        with open(path + "/" + file_name, "r", encoding="utf8") as file:
            json_file = json.loads(file.read())
            # print(json_file)
            row_list = [count]
            row_list.append(json_file["metadate_map"]["作者"])
            row_list.append(json_file["metadate_map"]["標題"])
            row_list.append(json_file["metadate_map"]["時間"])
            row_list.append(json_file["push_data"]["push_sum"]["→"])
            row_list.append(json_file["push_data"]["push_sum"]["噓"])
            row_list.append(json_file["push_data"]["push_sum"]["推"])
            df.loc[count] = row_list
            count += 1
            # break
            # for k, v in json_file.items():
            #     print(k, v)
    print(df)
    df.to_csv("./test/p.csv", index=False, encoding="utf_8_sig")


if __name__ == "__main__":
    main()
