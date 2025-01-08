import csv
import re
import pandas as pd

path = "./joinedcsv/join_review.csv"
path2 = "./(2022年度)結果報告データ一覧_250106a.csv"
path3 = "./(2023年度)結果報告データ一覧_250106a.csv"

customer_review = pd.read_csv(path, encoding="utf-16 LE", sep="\t")

bs_list_2022 = pd.read_csv(path2, encoding="CP932")
bs_list_2023 = pd.read_csv(path3, encoding="CP932")


join_review = pd.merge(customer_review, bs_list_2022)

join_review["URL"] = "https://asahikasei-eng.svy.ooo/surveys/185371/result/panels/"

join_review['URL'] = join_review['URL'].str.cat(join_review['USER No.'].astype(str))

# print(customer_review)
# print(join_review.loc[: ,["USER No.","受注NO", "物件名"]])

join_review.to_csv('join_review.csv',encoding='utf-8')

