import csv
import re
import pandas as pd

path = "./【正式運用版】お客様満足度アンケ.csv"
path2 = "./物件一覧_20241212133711.csv"

customer_review = pd.read_csv(path, encoding="utf-16 LE", sep="\t")

bs_list = pd.read_csv(path2, encoding="CP932")

for index_row, row in enumerate(customer_review):
    for index_item, item in enumerate(row):
        # 取り込む回答の項目の数
        # if (index_item < 21) : continue
        if (index_item == 2):
          # 6桁の番号を抽出
          customer_review.iloc(index_row, index_item) = item[:6]

print(customer_review)
