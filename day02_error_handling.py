import logging

# logging.basicConfig()親ロガーはロギング全体の土台を一度だけ設定する役割ロギングルール
# どこに（画面またはファイル）どのレベル　どんなFMTで
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

# logging.getLogger(__name__)子ロガーは、ルールに基づき実際にログを出力する
logger = logging.getLogger(__name__)

try:
    logger.info("計算を開始します")
    result = 10 / 0
    logger.info(f"計算成功: {result}")
except Exception as e:
    logger.error("計算に失敗しました", exc_info=e)

logger.info("プログラムは落ちずに続行できます")

# __name__と__main__について
# __name__ と __main__ は、Pythonのプログラムでよく使われる特別な名前
# __name__は、**「実行中のモジュールの名前」**が入る変数
# Pythonファイルは、モジュールとして他のファイルから読み込まれることも、直接実行されることもあります。
# __main__は、**「そのプログラムが直接実行されたとき」**に__name__に入る特別な名前です。