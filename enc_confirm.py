import chardet

with open('./物件一覧_20241212133711.csv', 'rb') as f:
    result = chardet.detect(f.read())
    print(result['encoding'])
