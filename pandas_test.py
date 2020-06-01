import pandas as pd
import json



def main():
    df = pd.DataFrame(columns=["name", "age", "height"])
    df.loc[0] = ["john", 20, 178]
    df.loc[1] = ["mary", 25, 165]
    df.loc[2] = ["john", 33, 188]
    print(df)
    # df["weight"] = [66, 75, 78]
    # print(df)
    # print(df.drop("weight", axis=1))
    # df = df.drop("weight", axis=1)
    # print(df)
    # df = df.drop(2)
    # print(df)
    # df["age"][1] = 30
    # print(df)
    # df.to_csv("./test/pan.csv", index=0, encoding="utf8")
    # df = pd.read_csv("./test/pan.csv")
    # print(df)
    with open("", "r", encoding="utf8") as file:
        json_data = json.loads(file.read())
        print()




if __name__ == "__main__":
    main()
