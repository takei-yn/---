import csv
import re
import pandas as pd

#Todo　完全外部結合ではなく、アンケートメインの結合を行う

path = "./joinedcsv/join_review.csv"
path2 = "./(2022年度)結果報告データ一覧_250106a.csv"
path3 = "./(2023年度)結果報告データ一覧_250106a.csv"

customer_review = pd.read_csv(path, encoding="utf-8",  dtype=str)

bs_list_2022 = pd.read_csv(path2, encoding="CP932", dtype=str)
bs_list_2023 = pd.read_csv(path3, encoding="CP932", dtype=str)

bs_list = pd.concat([bs_list_2022, bs_list_2023], axis=0, ignore_index=True)

# print("customer_review")
# print(customer_review.columns)
# print("bs_list_2022")
# print(bs_list_2022.columns)

join_review = pd.merge(customer_review, bs_list, how="outer", on = "物件ID")


join_review.to_csv('join_review_result_report.csv',encoding='utf-8')


a = pd.read_csv("join_review_result_report.csv", encoding="utf-8",  dtype=str)

print(a.columns)
print(a.head())
# print(a["Unnamed: 0"])