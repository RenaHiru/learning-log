import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

logger.debug("これは開発者向けの細かい情報です")
logger.info("通常処理が成功しました")
logger.warning("エラーが発生しました")
logger.critical("重大なエラー!システムが止まりそう")