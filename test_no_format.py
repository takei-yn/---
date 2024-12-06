from openai import AzureOpenAI
import csv
 
# Subscription Keyを入力します。
api_key = "1adb78a6e8914f489719ef8b9e76f21d"
 
# 接続処理をしてくれるクライアントクラスを作成します
client = AzureOpenAI(
    api_version="2024-10-01-preview",
    azure_endpoint="https://ifx-apim-01.azure-api.net",
    api_key=api_key
)

content1 = "USER No. 88850555の方が総合力についてなんと答えていたか教えてください\n"

content2 = "以下のマークダウン形式のアンケート結果をもとに回答してください。\n\n"
content = content1 + content2

path = "./【正式運用版】お客様満足度アンケ.csv"

with open(path, encoding="utf-16 LE") as f:
    l = csv.reader(f, delimiter="\t")
    for index_row, row in enumerate(l):
        # 取り込む回答のレコードの数
        if (index_row > 35) : continue

        for index_item, item in enumerate(row):
            # 取り込む回答の項目の数
            # if (index_item < 21) : continue

            content = content + item + ","
            print("item: " + item)

        content = content + "\n"

print("contet:\n" + content)

# Chat Completionメソッドで問い合わせをします。
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": content,
        },
    ],
)
# print(completion.choices[0].message.content.model_dump_json(indent=2))
print("[Question]\n"+content1)
print("[Answer]\n"+completion.choices[0].message.content+"\n\n")

																			