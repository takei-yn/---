import csv
import re

path = "./【正式運用版】お客様満足度アンケ.csv"

with open(path, encoding="utf-16 LE") as f:
    l = list(csv.reader(f, delimiter="\t"))
    for index_row, row in enumerate(l):

        for index_item, item in enumerate(row):
            # 取り込む回答の項目の数
            # if (index_item < 21) : continue
            if (index_item == 2):
              # 6桁の番号を抽出
              l[index_row][index_item] = item[:6]

print(l)