import collections
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import re

from pykakasi import kakasi

def convertToKakashi(text):
  # オブジェクトをインスタンス化
  kks = kakasi()
  # 変換して出力
  result = kks.convert(text)
  tmp = ''
  for item in result:
    tmp += item['hira']
  #   print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'],item['hepburn']))
  # return result
  return tmp


f = open('code.txt', 'r', encoding='UTF-8')
data = f.read()
f.close()
c = collections.Counter(convertToKakashi(data))
print(c.most_common(100))

# d = list(data)

# sns.set(context="talk")
# fig = plt.subplots(figsize=(8, 8))

# sns.countplot(y=d,order=[i[0] for i in c.most_common(30)])

# plt.savefig("seaborntest.png")


