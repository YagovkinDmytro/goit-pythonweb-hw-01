import logging

def main():
    # logging.basicConfig(
    #     format='%(asctime)s %(message)s',
    #     level=logging.NOTSET,
    #         handlers=[
    #         logging.FileHandler("solid.log"),
    #         logging.StreamHandler()
    #     ])
    # logging.critical('An example critical.')
    # logging.error('An example error.')
    # logging.warning('Another message')
    # logging.info('An example info.')
    # logging.debug('An example debug.')

    # створюємо логер, даємо йому ім'я та встановлюємо рівень logging.DEBUG
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.NOTSET)

    # створюємо handler для виведення в консоль та встановлюємо рівень DEBUG
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # створюємо форматтер: час виведення (asctime), ім'я модуля (name), рівень (levelname) та саме повідомлення (message)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # додаємо зазначений форматтер до handler ch
    ch.setFormatter(formatter)

    # додаємо handler ch до логера
    logger.addHandler(ch)

    # Створюємо файловий handler для логера:
    fh = logging.FileHandler("app.log")
    fh.setLevel(logging.ERROR)
    fh.setFormatter(formatter)

    # додаємо файловий handler fh до логера
    logger.addHandler(fh)

    # приклад виконання коду
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

if __name__ == "__main__":
    main()