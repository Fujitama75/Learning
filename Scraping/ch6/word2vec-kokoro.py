import MeCab
from gensim.models import word2vec
import re

# テキストファイルの読み込み --- (※1)
bindata = open('kokoro.txt.sjis', 'rb').read()
text = bindata.decode('shift_jis')

# テキストの先頭にあるヘッダとフッタを削除 --- (※2)
text = re.split(r'\-{5,}', text)[2]
text = re.split(r'底本：', text)[0]
text = text.strip()

# 形態素解析 --- (※3)
mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
results = []

# テキストを一行ずつ処理する
lines = text.split("\r\n")
for line in lines:
    s = line
    s = s.replace('｜', '')
    s = re.sub(r'《.+?》', '', s)  # ルビを削除
    s = re.sub(r'［＃.+?］', '', s)  # 入力注を削除
    mecab.parse('')
    malist = mecab.parse(line).splitlines()[:-1]
    # 必要な語句だけを対象とする --- (※4)
    r = []
    for w in malist:
        (word, feature) = w.split('\t')
        part_of_speech = feature.split(",")[0]

        if part_of_speech in ['形容詞', '動詞']:
            w = feature.split(",")[6]
        else:
            w = word

        if part_of_speech in ['名詞', '形容詞', '動詞', '記号']:
            r.append(w)
    rl = (" ".join(r)).strip()
    results.append(rl)
    print(rl)  # --- 画面に分かち書きした行を表示

# 書き込み先テキストを開く --- (※5)
wakati_file = 'kokoro.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))

# Word2Vecでモデルを作成 --- (※6)
data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save('kokoro.model')
print('ok')
