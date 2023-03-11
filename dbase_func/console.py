def reset_settings() -> None:
    from data.const import CONSTPATH
    from os.path import join as join_path, split as split_file
    from localise_func.translator import localized_print
    DIR_COSNT: str = split_file(CONSTPATH)[0]
    CONSTPATH_BASE: str = join_path(DIR_COSNT, 'base_const.py')
    with (
        open(CONSTPATH, 'wt', encoding='utf-8') as user_settings,
        open(CONSTPATH_BASE, 'rt', encoding='utf-8') as base_settings
    ):
        data: list[str] = base_settings.readlines()
        print(*data, sep = '', end = '', file=user_settings)
    localized_print('Settings have been successfully reset to basic')
    exit()


def checking_settings(args: tuple[str]) -> None:
    from localise_func.translator import localized_print
    from main import FILEPATH
    from typing import Callable

    KEY_DESCRIPTION: int = 0
    KEY_FUNCK_ACTIVE: int = 1

    DATA_SETTINGS: dict[str,tuple[str, Callable[[], None]]]
    DATA_SETTINGS = {
        'reset': ('Reset settings to initial', reset_settings),
    }

    if args not in ([FILEPATH, ], ['main.py']):
        localized_print('Special Launch')
        for arg in map(str.lower, args):
            if arg in DATA_SETTINGS:
                localized_print(DATA_SETTINGS[arg][KEY_DESCRIPTION])
                DATA_SETTINGS[arg][KEY_FUNCK_ACTIVE]()
            elif arg not in (FILEPATH, 'main.py'):
                localized_print('Additional startup parameter', end = ' ')
                print(arg, end = ' ')
                localized_print('not found in the database')
        localized_print('Recognized settings have been applied successfully')
        localized_print('restart the application to continue')
        exit()