# BMI Calculator / by atsushi-dayo
def calculate_bmi(weight, height):
    """
    Function to calculate BMI
    :param weight: Weight (kg)
    :param height: Height (m)
    :return: BMI value
    """
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "身長は0より大きい値を入力してください。(Please enter a height greater than 0.)"

def main():
    print("BMI計算プログラム (BMI Calculation Program)")
    try:
        weight = float(input("体重を入力してください (kg) (Enter your weight (kg)): "))
        height_cm = float(input("身長を入力してください (cm) (Enter your height (cm)): "))
        height_m = height_cm / 100  # Convert cm to meters
        bmi = calculate_bmi(weight, height_m)
        print(f"あなたのBMIは: {bmi} (Your BMI is: {bmi})")
        
        if isinstance(bmi, float):
            if bmi < 18.5:
                print("カテゴリー: 低体重 (Category: Underweight)")
            elif 18.5 <= bmi < 25:
                print("カテゴリー: 普通体重 (Category: Normal weight)")
            elif 25 <= bmi < 30:
                print("カテゴリー: 肥満1度 (Category: Overweight (Class 1))")
            else:
                print("カテゴリー: 肥満2度以上 (Category: Obesity (Class 2 or higher))")
    except ValueError:
        print("有効な数値を入力してください。(Please enter a valid number.)")

if __name__ == "__main__":
    main()