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

content1 = "営業の担当の課題について教えてください。\n"
# content = "営業の担当の課題について要約して教えてください。\n"


# content = "営業担当の満足度が高い理由を教えてください。\n"


content2 = "以下のマークダウン形式のアンケート結果をもとに回答してください。\n\n"
content = content1 + content2

# path = "./【正式運用版】お客様満足度アンケ.csv"
path = "./【正式運用版】お客様満足度アンケ (1) 1.csv"

# with open(path, encoding="utf-16 LE") as f:
#     l = f.readlines()
#     for row in l:
#         print(row)

with open(path, encoding="utf-16 LE") as f:
    l = csv.reader(f, delimiter="\t")
    for index_row, row in enumerate(l):
        if (index_row < 3) : continue
        
        content += "# アンケート結果"
        content += "\n"
        content += "## 営業担当の対応（挨拶、マナー、迅速性、丁寧さ等）はいかがでしたでしょうか。"
        content += "\n"
        content += row[21]
        content += "\n"
        content += "## 営業担当についてそのように評価された理由をお聞かせください。 "
        content += "\n"
        content += row[22]
        content += "\n"
        content += "## 弊社の技術力について回答お願い致します。"
        content += "\n"
        content += "### プロジェクトマネージャーの対応"
        content += "\n"
        content += row[23]
        content += "\n"
        content += "### 技術力・経験"
        content += "\n"
        content += row[24]
        content += "\n"
        content += "### 工程管理の対応"
        content += "\n"
        content += row[25]
        content += "\n"
        content += "### 現場でのコミュニケーション"
        content += "\n"
        content += row[26]
        content += "\n"
        content += "### 安全対策の対応"
        content += "\n"
        content += row[27]
        content += "\n"
        content += "### ベンダーの管理対応"
        content += "\n"
        content += row[28]
        content += "\n"
        content += "### 追加変更への対応"
        content += "\n"
        content += row[29]
        content += "\n"
        content += "### 成果物の品質"
        content += "\n"
        content += row[30]
        content += "\n"        
        content += "## 技術力について、そのように評価された理由をお聞かせください。 "
        content += "\n"
        content += row[31]
        content += "\n"
        # content += "## 弊社からの報告について回答お願い致します"
        # content += row[30]
        # content += "### 追加変更への対応"
        # content += row[31]        content += "### "
        # content += row[33]

        # for index_item, item in enumerate(row):
        #     if (index_item < 21) : continue
        #     content = content + item + ","
        #     print("item: " + item)
        # content = content + "\n"

        
        # with open("./abc.csv", mode="w", encoding="utf-16 LE") as w:
        #     writer = csv.writer(w)
        #     writer.writerow(row)

# print(content)

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

																			