import random
import time

def multiplication_quiz():
    # 言語選択
    while True:
        language = input("Select language: 1 for English, 2 for Japanese (言語を選択してください: 1. 英語, 2. 日本語): ")
        if language in ["1", "2"]:
            break
        else:
            print("Please enter 1 or 2. (1または2を入力してください。)")

    # 言語に応じたメッセージ
    if language == "1":
        welcome_msg = "Welcome to the Multiplication Quiz!"
        choose_difficulty_msg = "Choose your difficulty level:"
        easy_msg = "1. Easy (Numbers 1-10)"
        hard_msg = "2. Hard (Numbers 11-20)"
        enter_difficulty_msg = "Enter 1 for Easy or 2 for Hard: "
        invalid_input_msg = "Please enter a valid number."
        range_easy_msg = "\nYou selected Easy mode. Numbers will range from 1 to 10.\n"
        range_hard_msg = "\nYou selected Hard mode. Numbers will range from 11 to 20.\n"
        question_msg = "Question"
        your_answer_msg = "Your answer: "
        correct_msg = "Correct!"
        wrong_msg = "Wrong. The correct answer was"
        quiz_complete_msg = "Quiz complete! You got"
        out_of_msg = "out of"
        correct_total_msg = "correct."
        total_time_msg = "Your total time:"
        seconds_msg = "seconds."
        perfect_score_msg = "Excellent! You got a perfect score!"
        great_job_msg = "Great job! You did very well."
        good_effort_msg = "Good effort! Keep practicing."
        keep_practicing_msg = "Keep practicing and you'll get better!"
        faster_msg = "Try to be a bit faster next time!"
        thanks_msg = "Thanks for playing!"
    else:
        welcome_msg = "掛け算クイズへようこそ！"
        choose_difficulty_msg = "難易度を選択してください:"
        easy_msg = "1. 簡単 (1～10の数字)"
        hard_msg = "2. 難しい (11～20の数字)"
        enter_difficulty_msg = "簡単は1、難しいは2を入力してください: "
        invalid_input_msg = "有効な数字を入力してください。"
        range_easy_msg = "\n簡単モードを選択しました。数字は1～10の範囲です。\n"
        range_hard_msg = "\n難しいモードを選択しました。数字は11～20の範囲です。\n"
        question_msg = "問題"
        your_answer_msg = "あなたの答え: "
        correct_msg = "正解！"
        wrong_msg = "不正解。正しい答えは"
        quiz_complete_msg = "クイズ終了！あなたの正解数は"
        out_of_msg = "問中"
        correct_total_msg = "問正解です。"
        total_time_msg = "合計時間:"
        seconds_msg = "秒。"
        perfect_score_msg = "素晴らしい！満点です！"
        great_job_msg = "よくできました！とても良い結果です。"
        good_effort_msg = "良い努力です！練習を続けましょう。"
        keep_practicing_msg = "練習を続ければもっと良くなります！"
        faster_msg = "次回はもう少し早く答えましょう！"
        thanks_msg = "遊んでくれてありがとう！"

    print(welcome_msg)
    print(choose_difficulty_msg)
    print(easy_msg)
    print(hard_msg)

    # 難易度の選択
    while True:
        try:
            difficulty = int(input(enter_difficulty_msg))
            if difficulty in [1, 2]:
                break
            else:
                print("Please enter 1 or 2. (1または2を入力してください。)")
        except ValueError:
            print(invalid_input_msg)

    # 難易度に応じた範囲を設定
    if difficulty == 1:
        min_num, max_num = 1, 10
        print(range_easy_msg)
    else:
        min_num, max_num = 11, 20
        print(range_hard_msg)

    num_questions = 10
    correct_answers = 0
    start_time = time.time()

    for i in range(1, num_questions + 1):
        a = random.randint(min_num, max_num)
        b = random.randint(min_num, max_num)
        correct = a * b

        print(f"{question_msg} {i}: {a} x {b}?")
        while True:
            try:
                user_answer = int(input(your_answer_msg))
                break
            except ValueError:
                print(invalid_input_msg)

        if user_answer == correct:
            print(correct_msg + "\n")
            correct_answers += 1
        else:
            print(f"{wrong_msg} {correct}.\n")

    end_time = time.time()
    total_time = end_time - start_time

    print(f"{quiz_complete_msg} {correct_answers} {out_of_msg} {num_questions} {correct_total_msg}")
    print(f"{total_time_msg} {total_time:.2f} {seconds_msg}")

    # 得点に応じた評価メッセージ
    if correct_answers == num_questions:
        print(perfect_score_msg)
    elif correct_answers >= num_questions * 0.7:
        print(great_job_msg)
    elif correct_answers >= num_questions * 0.5:
        print(good_effort_msg)
    else:
        print(keep_practicing_msg)

    # 1分以上かかった場合のメッセージ
    if total_time > 60:
        print(faster_msg)

    print(thanks_msg)

if __name__ == "__main__":
    multiplication_quiz()