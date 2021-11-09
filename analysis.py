import collections
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import re

from pykakasi import kakasi

def convertToKakashi(text):
  tmp = ''
  for item in kakasi().convert(text):
    tmp += item['hira']
    # print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'],item['hepburn']))
  # return result
  # print(tmp)
  return tmp


f = open('code.txt', 'r', encoding='UTF-8')
data = f.read()
f.close()
txt = convertToKakashi(data)
c = collections.Counter(txt)
print(c.most_common(100))

# d = list(data)
# sns.set(context="talk")
# fig = plt.subplots(figsize=(8, 8))
# sns.countplot(y=d,order=[i[0] for i in c.most_common(30)])
# plt.savefig("seaborntest.png")

print('----------------')

gram_2 =[]
for idx in range(len(txt) - 1):
    # print(txt[idx] + ':' + txt[idx + 1])
    gram_2.append(txt[idx] + txt[idx + 1])
c = collections.Counter(gram_2)
print(c.most_common(100))

print('----------------')

gram_3 =[]
for idx in range(len(txt) - 2):
    gram_3.append(txt[idx] + txt[idx + 1] + txt[idx + 2])
c = collections.Counter(gram_3)
print(c.most_common(100))
