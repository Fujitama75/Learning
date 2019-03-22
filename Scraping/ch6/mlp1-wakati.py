from janome.tokenizer import Tokenizer
import MeCab
import os
import glob

# Janomeを使って形態素解析を行う
# ja_tokenizer = Tokenizer()

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')


# 日本語を分かち書き
def ja_tokenize(text):
    res = []
    lines = text.split("\n")
    lines = lines[2:]  # 最初の二行はヘッダ情報なので捨てる
    for line in lines:
        # malist = ja_tokenizer.tokenize(line)
        mecab.parse('')
        # 最後はEOSなので、読み飛ばす
        malist = mecab.parse(line).splitlines()[:-1]
        for tok in malist:
            # print("***")
            # print(tok)
            if tok == "":
                continue
            (word, feature) = tok.split('\t')
            part_of_speech = feature.split(",")[0]

            if part_of_speech not in ['名詞', '動詞', '形容詞']:
                continue

            w = feature.split(",")[6]
            # w = tok.base_form
            if w == "*" or w == "":
                w = word
            if w == "" or w == "\n":
                continue
            res.append(w)
        res.append("\n")
    return res

# テストデータを読み込み
root_dir = './newstext'
for path in glob.glob(root_dir+"/*/*.txt", recursive=True):
    if path.find("LICENSE") > 0:
        continue
    # print(path)
    path_wakati = path + ".wakati"
    if os.path.exists(path_wakati):
        continue
    text = open(path, "r").read()
    words = ja_tokenize(text)
    wt = " ".join(words)
    open(path_wakati, "w", encoding="utf-8").write(wt)
