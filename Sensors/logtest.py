import logging

logger = logging.getLogger('__name__')



handler = logging.FileHandler(filename='logging_test.txt')
handler.setLevel(logging.DEBUG)

#フォーマットを作成
handler_format = logging.Formatter('%(asctime)s - %(name)s - %(threadNames)s - %(message)s')
#作成したフォーマットをformmterに設定
handler.setFormatter(handler_format)

#loggerに追加
logger.addHandler(handler)

logger.debug("hello")