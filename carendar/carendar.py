import random
from datetime import datetime

# 名言リスト（名言と発言者のペア）
quotes = [
    ("未来を予測する最良の方法は、それを発明することだ。", "アラン・ケイ (Alan Kay)"),
    ("人生は何が起こるかが10%、それにどう反応するかが90%だ。", "チャールズ・R・スウィンドル (Charles R. Swindoll)"),
    ("あなたの時間は限られている。他人の人生を生きることで無駄にしてはいけない。", "スティーブ・ジョブズ (Steve Jobs)"),
    ("素晴らしい仕事をする唯一の方法は、自分の仕事を愛することだ。", "スティーブ・ジョブズ (Steve Jobs)"),
    ("成功は幸福の鍵ではない。幸福が成功の鍵だ。", "アルベルト・シュバイツァー (Albert Schweitzer)"),
    ("あなたが本当にやりたいことを見つけるまで、決してあきらめないでください。", "不明 (Unknown)"),
    ("失敗は成功の母だ。", "ことわざ (Proverb)"),
    ("成功するためには、まず自分を信じることが必要だ。", "不明 (Unknown)"),
    ("夢を追いかける勇気があれば、夢は実現する。", "ウォルト・ディズニー (Walt Disney)"),
    ("人生は短い。だから、あなたの夢を追いかけてください。", "不明 (Unknown)"),
    ("あなたの未来は、あなたが今日何をするかによって決まる。", "マハトマ・ガンジー (Mahatma Gandhi)"),
    ("成功は最終的なものではない。失敗は致命的ではない。重要なのは続ける勇気だ。", "ウィンストン・チャーチル (Winston Churchill)"),
    ("自分を信じて、行動しなさい。", "不明 (Unknown)"),
    ("あなたの人生は、あなたが選ぶものだ。", "不明 (Unknown)"),
    ("他人の期待に応えるために生きるな。自分の期待に応えろ。", "不明 (Unknown)"),
    ("成功は、準備が整ったところに訪れる。", "不明 (Unknown)"),
    ("あなたができると思うこと、できないと思うこと、どちらも正しい。", "ヘンリー・フォード (Henry Ford)"),
    ("人生は自転車のようなものだ。バランスを保つためには前に進まなければならない。", "アルベルト・アインシュタイン (Albert Einstein)"),
    ("あなたができると思うことをやりなさい。そうすれば、あなたはできる。", "不明 (Unknown)"),
    ("成功するためには、まず自分を信じることが必要だ。", "不明 (Unknown)"),
    ("あなたの人生は、あなたが選ぶものだ。", "不明 (Unknown)"),
    ("他人の期待に応えるために生きるな。自分の期待に応えろ。", "不明 (Unknown)"),
    ("成功は、準備が整ったところに訪れる。", "不明 (Unknown)"),
    ("あなたができると思うこと、できないと思うこと、どちらも正しい。", "ヘンリー・フォード (Henry Ford)"),
    ("人生は自転車のようなものだ。バランスを保つためには前に進まなければならない。", "アルベルト・アインシュタイン (Albert Einstein)"),
    ("あなたができると思うことをやりなさい。そうすれば、あなたはできる。", "不明 (Unknown)"),
]

# 日本語の曜日リスト
japanese_weekdays = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

# 今日の日付を取得
today = datetime.now()
year = today.year
month = today.month
day = today.day
weekday_index = today.weekday()  # 0: 月曜日, 1: 火曜日, ..., 6: 日曜日
weekday_jp = japanese_weekdays[weekday_index]  # 日本語の曜日

# ランダムな名言を選択
quote, author = random.choice(quotes)

# 結果を表示
print(f"今日は{month}月{day}日（{weekday_jp}）です。")
print(f"今日の名言は: {quote} - {author}")