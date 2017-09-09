# python3-auto-abstracts

## Demo

- [日本語文書の自動要約アルゴリズムを60年近く前の論文を頼りに再記述する](http://media.accel-brain.com/auto-abstractor-jp/)

## Requirement

- Python 3.x

```
$ python --version
Python 3.6.2
```

- mecab

```
$ mecab --version
mecab of 0.996
```

- libmecab-dev

```
$ apt-cache show libmecab-dev
Package: libmecab-dev
Source: mecab
Version: 0.996-1.1
Installed-Size: 2993
Maintainer: TSUCHIYA Masatoshi <tsuchiya@namazu.org>
Architecture: amd64
Depends: libmecab2 (= 0.996-1.1)
Description: Header files of Mecab
Description-md5: 87197d521c6686e342ae43fe6394b7da
Homepage: http://code.google.com/p/mecab/
Tag: devel::library, role::devel-lib
Section: libdevel
Priority: optional
Filename: pool/main/m/mecab/libmecab-dev_0.996-1.1_amd64.deb
Size: 285160
MD5sum: 4971d02da2d986c031ddbbd8c37aff27
SHA1: b4e2eb13eec4cfd3bd74a437ce6c4149b0888f9a
SHA256: a5988f3a1690ecb3b642ddd5b8ff79d3e7aeb99ec072e9dffda84986a0b3ba5c
```

- mecab-naist-jdic

```
$ apt-cache show mecab-naist-jdic
Package: mecab-naist-jdic
Version: 0.6.3.b-20111013-5
Installed-Size: 9
Maintainer: Natural Language Processing, Japanese <pkg-nlp-ja-devel@lists.alioth.debian.org>
Architecture: all
Depends: mecab-utils (>= 0.93), mecab-naist-jdic-eucjp (= 0.6.3.b-20111013-5)
Pre-Depends: dpkg (>= 1.15.6~)
Description: free Japanese Dictionaries for mecab (replacement of mecab-ipadic)
Description-md5: 1b71c3e4fbd42d5da705798b6278835f
Homepage: http://sourceforge.jp/projects/naist-jdic/
Section: misc
Priority: optional
Filename: pool/main/m/mecab-naist-jdic/mecab-naist-jdic_0.6.3.b-20111013-5_all.deb
Size: 5074
MD5sum: addac5d70b99655712857952168bf223
SHA1: 73c622e3fbdd8b095602c088b4a83ed55219ad03
SHA256: 78c7f63b02e0483df92a626b216c1dd15af14d5262652859598ef06e107b98e4
```

## Usage

```
from auto_abstracts.auto_abstractor import Scraping, AutoAbstractor, AbstractableTopNRank
scrape = Scraping()
document = scrape.scrape('http://www.natsumesoseki.com/home/kokoro') # HTML文書からテキストを取得しているだけ
abstractor = AutoAbstractor()
doc = AbstractableTopNRank()
result = abstractor.summarize(document, doc) # テキストを要約する
repr(result) # "summarize_result"に要約結果がリストで格納される
```

結果

```
"{'summarize_result': ['夏目漱石.com このサイトを検索 home 「額の男」を読む 『伝説の時代』序 『土』に就て 『心』自 序 『東洋美術図譜』 『煤煙』の序 こころ それから イズムの功過 カーライル博物館 ケーベル先生 ケーベル先生の告別 コンラッドの描きたる自然について マードック先生の『日本歴史』 一夜 三四郎 三山居士 中味と形式 予の描かんと欲する作品 二百十日 京に着ける夕 人生 余と万年筆 作物の批評 倫敦塔 倫敦消息 僕の昔 元日 入社の辞 写生文 処女作追懐談 初秋の一日 創作家の態度 博士問題とマードック先生と余 博士問題の成行 吾輩は猫である 吾輩は猫である自序 坊ちゃん 坑夫 変な音 夢 十夜 子規の画 学者と名誉 岡本一平著並画『探訪画趣』序 幻影の盾 彼岸過迄 思い出す事など 戦争からきた行き違い 手紙 教育と文芸 文壇の趨勢 文士の生活 文芸とヒロイツク 文芸と道徳 文芸の哲学的基礎 文芸は男子一生の事業とするに足らざる乎 文芸委員は何をするか 文鳥 明暗 明治座の所感を虚子君に問れて 木下杢太郎著『唐草表紙』序 模倣と独立 正岡子規 永日小品 満韓ところどころ 点頭録 無題 現代日本の開化 琴のそら音 田山花袋君に答う 硝子戸の中 私の個人主義 私の経過した学生時代 自然を写す文章 自転車日記 艇長の遺書と中佐の詩 草枕 落第 薤露行 虚子君へ 虞美人草 行人 西洋にはない 趣味の遺伝  道楽と職業 道草 野分 鈴木三重吉宛書簡-明治三十九年 長塚節氏の小説「土」 長谷川君と余 門 高浜虚子著『鶏頭』序 サイトマップ home \\u200e > \\u200e こころ 上\\u3000先生と私 一 私わたくしはその人を常に先生と呼んでいた。\\n', '先生は有難うといって、それを私の手から受け取った。\\n', ' しばらくして海の中で起き上がるように姿勢を改めた先生は、「もう帰 りませんか」といって私を促した。\\n', '奥さんは「ちょっと」と先生を次の間まへ呼んだ。\\n', '私はそれから論文の問題 を小さくした。\\n', ' 三十四 私わたくしはその夜十時過ぎに先生の家を辞した。\\n', ' 「その先生は何をしているのかい」と父が聞いた。\\n', ' 十三 「奥さんのこの態度が自然私の気分に影響して来ました。\\n', ' 二十九 「私は思い切って自分 の心をＫに打ち明けようとしました。\\n', '君の心でそれを止めるだけの覚悟がなければ。\\n'], 'scoring_data': [(0, 5.0), (88, 4.923076923076923), (99, 5.260869565217392), (591, 5.142857142857143), (981, 5.142857142857143), (1343, 5.0), (1695, 4.923076923076923), (2729, 5.0625), (3430, 5.882352941176471), (4007, 5.0)]}"
```

## Installation

依存ライブラリをインストールします。

```
$ apt-get update
$ apt-get install -y mecab libmecab-dev mecab-naist-jdic
```

auto_abstractsをpipでインストールします。

```
$ pip install git+https://github.com/u6k/python3-auto-abstracts.git
```
