import MeCab

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')

malist = mecab.parse("庭には二羽鶏がいる。")
print(malist)
