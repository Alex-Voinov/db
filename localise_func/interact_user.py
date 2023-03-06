def get_code():
    from const import (
        CODE_LANG,
        UNKNOW,
        CONST_FILE_NAME
    )
    from main import FILEPATH
    from os.path import join, split as file_split
    CODE_RUS: int = '1'
    CODE_ENG: int = '2'
    COD_IT: int = '3'
    lang: dict = {
        CODE_RUS: 'Русский язык',
        CODE_ENG: 'Английский язык',
        COD_IT: 'Итальянсий язык',
    }
    if CODE_LANG == UNKNOW:
        main_lang: str = ''
        print('Выберете язык:')
        for code, lan in lang.items():
            print(f'{code}) {lan}')
        while main_lang not in lang.keys():
            main_lang = input('> ')
        print(f'В системе будет использоваться {lang[main_lang]}')
        DIR_NAME, _ = file_split(FILEPATH)
        CONST_PATH: str = join(DIR_NAME, CONST_FILE_NAME)
        with open(CONST_PATH, "rt", encoding="utf-8") as pathchange:
            oldfile: list = pathchange.readlines()
        for index in range(len(oldfile)):
            if "CODE_LANG: int =" in oldfile[index]:
                oldfile[index] = f"CODE_LANG: int = {main_lang}\n"
                break
        with open(CONST_PATH, "wt", encoding="utf-8") as writing:
            print(*oldfile, sep="", end="", file=writing)
        return int(main_lang)
    else:
        return CODE_LANG
    
