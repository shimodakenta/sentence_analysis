import collections
import csv
import pykakasi

# ファイル読み込み
with open('freewriting.txt', 'r', encoding='UTF-8') as f:
  txt = ''
  for item in pykakasi.kakasi().convert(f.read()):
    txt += item['hira']

# 単語長ごとに解析する
for i in range(1, 5):
  print('----------------')
  print(f'{i}_gram')

  # 頻度解析
  n_gram =[]
  for j in range(len(txt) - i):
    n_gram.append(txt[j : j + i])
  c = collections.Counter(n_gram)
  print(c.most_common(100))

  # CSV出力
  with open(f'{i}_gram.csv', 'w') as f:
    for row in c.most_common():
        print(*row, sep=',', file=f)

  # グラフ出力
  # d = list(data)
  # sns.set(context="talk")
  # fig = plt.subplots(figsize=(8, 8))
  # sns.countplot(y=d,order=[i[0] for i in c.most_common(30)])
  # plt.savefig(f'seaborntest_{i}.png')
