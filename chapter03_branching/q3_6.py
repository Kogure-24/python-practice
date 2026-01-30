num1 = int(input("①整数を入力してください："))
num2 = int(input("②整数を入力してください："))
num3 = int(input("③整数を入力してください："))

if num1 > num2 and num1 > num3:
    print(f"最大値は{num1}ですね")
elif num2 > num1 and num2 > num3:
    print(f"最大値は{num2}ですね")
else:
    print(f"最大値は{num3}ですね")
