

'''Includes localised function of translator function.'''

from localise_func.interact_user import get_code
from typing import Callable


def get_local_print() -> Callable[[str], None]:
    '''Generator of localisation translator function.'''
    from data.lang_pack import VOCAB
    TUPLE_NUMERATION_CONV: int = 1
    LANGUAGE_CODE: int = get_code()
    def lang_print(word: str) -> None:
        '''Prints phrase in chosen language.'''
        print(VOCAB[word][ LANGUAGE_CODE - TUPLE_NUMERATION_CONV])
    return lang_print
