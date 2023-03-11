

'''includes functions to interract with user.'''


from interact_funcs.base import perfect_dt
from data.const import POS_ANW, NEG_ANW


def notification(flag: bool, pos: str='', neg: str ='') -> bool:
    '''prints negative or positive comment depending on statement status.'''
    if flag and pos:
        print(pos)
    elif not flag and neg:
        print(neg)
    return flag


def user_answer(
    question: str,
    posanswer: tuple=POS_ANW,
    neganswer: tuple=NEG_ANW,
    notification: str=""
) -> int:
    '''asks user a question and returns result depending on answer.'''
    from localise_func.translator import get_local_print
    answ: str = ""
    local_print = get_local_print()
    if notification:
        local_print(notification)
    while answ not in posanswer + neganswer:
        local_print(question, end ='')
        answ = perfect_dt(input())
        if answ in posanswer:
            return True
        elif answ in neganswer:
            return False
        else:
            local_print("We did not understand you")
            local_print("Please use answers presented: POSITIVES: ", end ='')
            print(', '.join(posanswer) ,end = ' ')
            local_print("or NEGATIVES: ")
            print(', '.join(neganswer))