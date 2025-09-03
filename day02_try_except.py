print("0で割り算をします")

try:
  result = 10 / 0
  print(f"計算成功: {result}")
except ZeroDivisionError:
  print("0で割り算はできません")
  
  print("プログラムは止まらずに続行できます")