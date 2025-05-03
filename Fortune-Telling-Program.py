# BMI Calculator / by atsushi-dayo
import random

def fortune_telling():
    fortunes = [
        "大吉: 素晴らしい一日になるでしょう！ (Great fortune: It will be a wonderful day!)",
        "中吉: 良いことが起こるかもしれません。 (Good fortune: Something good might happen.)",
        "小吉: 少しだけ幸運が訪れるでしょう。 (Small fortune: A little luck will come your way.)",
        "末吉: 小さな幸せを見つけられるかも。 (Minor fortune: You might find small happiness.)",
        "凶: 注意深く行動してください。 (Bad fortune: Be cautious in your actions.)",
        "大凶: 今日は慎重に過ごしましょう。 (Very bad fortune: Spend today carefully.)"
    ]
    print("今日の運勢を占います... (Let's see your fortune for today...)")
    print("結果は... (The result is...)")
    print(random.choice(fortunes))

if __name__ == "__main__":
    fortune_telling()