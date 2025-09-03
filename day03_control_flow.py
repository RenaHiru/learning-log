# --- 条件分岐 ---
score = 75

if score >= 80:
    print("合格！よくできました 🎉")
elif score >= 60:
    print("合格！もう少しがんばろう ✨")
else:
    print("不合格 😢")


# --- forループ ---
fruits = ["りんご", "バナナ", "みかん"]

print("\nフルーツリスト:")
for fruit in fruits:
    print(fruit)


# --- whileループ ---
count = 0
print("\nwhileループの例:")
while count < 3:
    print("カウント:", count)
    count += 1
