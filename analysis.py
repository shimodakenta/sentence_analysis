import collections
import pykakasi

f = open('code.txt', 'r', encoding='UTF-8')
data = f.read()
f.close()

txt = ''
for item in pykakasi.kakasi().convert(data):
  txt += item['hira']

for i in range(1, 5):
  print('----------------')
  print(f'{i}_gram')
  n_gram =[]
  for j in range(len(txt) - i):
    n_gram.append(txt[j : j + i])
  c = collections.Counter(n_gram)
  print(c.most_common(100))

  # d = list(data)
  # sns.set(context="talk")
  # fig = plt.subplots(figsize=(8, 8))
  # sns.countplot(y=d,order=[i[0] for i in c.most_common(30)])
  # plt.savefig(f'seaborntest_{i}.png')
