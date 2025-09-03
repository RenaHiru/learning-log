from typing import Literal
import logging

# ロギング設定
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(name)s - %(message)s")
logger = logging.getLogger(__name__)

def calc_bmi(height_m: float, weight_kg: float) -> float:
    """
    身長(m)と体重(kg)からBMIを返す。入力値を検証して例外を投げる
    """
    if height_m <= 0 or weight_kg <= 0:
        raise ValueError("身長と体重は正の値を入力してください")
    return round(weight_kg / (height_m ** 2), 2)

def classify_bmi(bmi: float) -> Literal["thin", "normal", "obese"]:
    """BMIの目安区分を返す"""
    if bmi < 18.5:
        return "thin"
    elif bmi < 25:
        return "normal"
    else:
        return "obese"

def say_hello(name: str) -> str:
    """名前を受け取って挨拶を返す"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    try:
        logger.info("BMI計算を開始します")
        bmi = calc_bmi(1.53, 45.0)
        label = classify_bmi(bmi)
        print(f"BMI: {bmi}, 判定: {label}")
        logger.info("BMI計算を正常終了")
    except Exception as e:
        logger.error(f"BMI計算中にエラーが発生しました: {e}")

    # say_hello の確認
    print(say_hello("Rena"))
