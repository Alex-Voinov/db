from os.path import abspath


UNKNOWN: int = -1
CODE_LANG: int = 1
SUPER_USER: int = 0
PATH: str = r'c:\proect_set\db\baza.txt'
CONST_FILE_NAME: str = "const.py"
SEPTAB: str = "\t" * 7
PASS_LEN_MIN: int = 5
MAX_RPT_CHR: int = 5
CONSTPATH: str = abspath(__file__)


POS_ANW: tuple = (
    "yes",
    "sure",
    "ye",
    "yeah",
    'y',
)

NEG_ANW: tuple = (
    "no",
    "nah"
    'nope',
    'n',
)


DB_FILE_NAME: str = r"baza.txt"


ORGPOL: tuple = (
    "ID",
    "LOGIN",
    "PASSWORD",
    "NAME",
    "SURNAME",
    "AGE",
    "NICKNAME",
    "LSO",
    "ROLE",
)


ROLES: tuple = (
    "User",
    "Admin",
)