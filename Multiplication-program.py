# Multiplication-program.py/atsushi-dayo

try:

    dan = int(input("何の段を表示しますか（1～50）: (Which multiplication table do you want to see? (1-50)): "))

    if 1 <= dan <= 50:
        print("=" * 40)
        print(f"【{dan}の段】 (Multiplication Table of {dan})")
        print("=" * 40)
        for i in range(1, 51):
            print(f"{dan:2} × {i:2} = {dan * i:4}  ({dan} times {i} equals {dan * i})")
        print("=" * 40)
    else:
        print("1～50の範囲で入力してください。 (Please enter a number between 1 and 50.)")
except ValueError:
    print("整数を入力してください。 (Please enter an integer.)")