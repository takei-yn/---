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

# content1 = "USER No. 132280382の方が営業担当の対応についてなんと答えていたか教えてください\n"

# content1 = "USER No. 132280382の方の弊社のプロジェクトマネージャの対応についての評価を教えてください\n"
# content1 = "USER No. 132280382の方の弊社の現場でのコミュニケーションについての評価を教えてください\n"
# content1 = "USER No. 132280382の方の弊社の追加等変更への対応についての評価を教えてください\n"
# content1 = "USER No. 132280382の方が弊社の技術力についてなんと答えていたか教えてください\n"
# content1 = "USER No. 132280382の方の弊社からの報告に関して、迅速性と報告内容（速報等）についての評価を教えてください\n"
# content1 = "USER No. 132280382の方が弊社からの報告についてなんと答えていたか教えてください\n"
# content1 = "USER No. 132280382の方の弊社の総合力に関して、提案力についての評価を教えてください\n"
# content1 = "USER No. 132280382の方の弊社の総合力に関して、コストの妥当性についての評価を教えてください\n"
# content1 = "USER No. 132280382の方が弊社の総合力についてなんと答えていたか教えてください\n"
# content1 = "USER No. 132280382の方の今後の設備投資計画等に関して、新規設備、システム導入について教えてください\n"
# content1 = "USER No. 132280382の方の今後の設備投資計画等に関して、設備またはシステム改造について教えてください\n"
# content1 = "USER No. 132280382の方の今後の設備投資計画等に関して、メンテナンスまたは更新について教えてください\n"
# content1 = "USER No. 132280382の方が今後の設備投資計画等についてなんと答えていたか教えてください\n"
# content1 = "USER No. 132280382の方がその他お気付きの点、ご要望についてなんと答えていたか教えてください\n"

# content1 = "USER No. 118153162の方が営業担当の対応についてなんと答えていたか教えてください\n"

# content1 = "USER No. 118153162の方の弊社のプロジェクトマネージャの対応についての評価を教えてください\n"
# content1 = "USER No. 118153162の方の弊社の現場でのコミュニケーションについての評価を教えてください\n"
# content1 = "USER No. 118153162の方の弊社の追加等変更への対応についての評価を教えてください\n"
# content1 = "USER No. 118153162の方が弊社の技術力についてなんと答えていたか教えてください\n"
# content1 = "USER No. 118153162の方の弊社からの報告に関して、迅速性と報告内容（速報等）についての評価を教えてください\n"
# content1 = "USER No. 118153162の方が弊社からの報告についてなんと答えていたか教えてください\n"
# content1 = "USER No. 118153162の方の弊社の総合力に関して、提案力についての評価を教えてください\n"
# content1 = "USER No. 118153162の方の弊社の総合力に関して、コストの妥当性についての評価を教えてください\n"
# content1 = "USER No. 118153162の方が弊社の総合力についてなんと答えていたか教えてください\n"
# content1 = "USER No. 118153162の方の今後の設備投資計画等に関して、新規設備、システム導入について教えてください\n"
# content1 = "USER No. 118153162の方の今後の設備投資計画等に関して、設備またはシステム改造について教えてください\n"
# content1 = "USER No. 118153162の方の今後の設備投資計画等に関して、メンテナンスまたは更新について教えてください\n"
# content1 = "USER No. 118153162の方が今後の設備投資計画等についてなんと答えていたか教えてください\n"
content1 = "USER No. 118153162の方がその他お気付きの点、ご要望についてなんと答えていたか教えてください\n"


content2 = "以下のマークダウン形式のアンケート結果をもとに回答してください。\n\n"
content = content1 + content2

path = "./【正式運用版】お客様満足度アンケ.csv"

with open(path, encoding="utf-16 LE") as f:
    l = csv.reader(f, delimiter="\t")
    for index_row, row in enumerate(l):
        # 取り込む回答のレコードの数
        # if (index_row > 35) : continue

        for index_item, item in enumerate(row):
            # 取り込む回答の項目の数
            # if (index_item < 21) : continue

            content = content + item + ","

        content = content + "\n"

# print("contet:\n" + content)

# Chat Completionメソッドで問い合わせをします。
completion = client.chat.completions.create(
    model="gpt-4o",
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

																			