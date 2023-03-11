from os.path import abspath
from dbase_func.creation import checkbase, load_dbase, save_dbase
from typing import Callable
from localise_func.translator import get_local_print


FILEPATH: str = abspath(__file__)
print: Callable[[str], str] = get_local_print()


def main():
    '''Main program cycle.'''
    if checkbase():
        try:
            db: list = load_dbase()
        except (ValueError, KeyError):
            checkbase(code=True)
        ...
        save_dbase(db)
    else:
        print("Programm ended sucsessfully")


if __name__ == "__main__":
    main()