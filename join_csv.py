import csv
import re
import pandas as pd

path = "./【正式運用版】お客様満足度アンケ.csv"
path2 = "./物件一覧_20241212133711.csv"

# with open(path, encoding="utf-16 LE") as f:
#     l = list(csv.reader(f, delimiter="\t"))
#     for index_row, row in enumerate(l):

#         for index_item, item in enumerate(row):
#             # 取り込む回答の項目の数
#             # if (index_item < 21) : continue
#             if (index_item == 2):
#               # 6桁の番号を抽出
#               l[index_row][index_item] = item[:6]

# print(l)

l = pd.read_csv(path2, encoding="CP932")

# with open(path2, encoding="shift_jis") as f:
#     # l = list(csv.reader(f, delimiter="\t"))
#     l = csv.reader(f, delimiter="\t")


print(l)