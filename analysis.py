import collections
import csv
import pykakasi
import glob


# ファイル読み込み
dir_path = '/Users/macbookpro/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyData'
for file in glob.glob(dir_path + '/202*-*.md'):
  print(file)
  with open(file, 'r', encoding='UTF-8') as f:
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
        print(*row, sep='\t', file=f)

  # グラフ出力
  # d = list(data)
  # sns.set(context="talk")
  # fig = plt.subplots(figsize=(8, 8))
  # sns.countplot(y=d,order=[i[0] for i in c.most_common(30)])
  # plt.savefig(f'seaborntest_{i}.png')
