

'''includes functions to create database.'''


def create_db() -> None:
    '''creates database.'''
    from data.const import CONSTPATH, DB_FILE_NAME
    from os.path import join, split as splitdir
    from interact_funcs.user  import user_answer
    from main import FILEPATH
    from localise_func.translator import get_local_print
    DIRNAME = splitdir(FILEPATH)[0]
    if user_answer(
        "Would you like to create the database file in the same directory?: "
    ):
        path: str = join(DIRNAME, DB_FILE_NAME)
    else:
        path: str = join(input(
            "Where would you like to create database: "
            ), DB_FILE_NAME
        )
    with open(CONSTPATH, "rt", encoding="utf-8") as pathchange:
        oldfile: list = pathchange.readlines()
    for index in range(len(oldfile)):
        if "PATH: str = " in oldfile[index]:
            oldfile[index] = f"PATH: str = r'{path}'\n"
            break
    with open(CONSTPATH, "wt", encoding="utf-8") as writing:
        print(*oldfile, sep="", end="", file=writing)
    with open(path, "wt", encoding="utf-8") as new_file:
        print("", end="", file=new_file)
    local_print = get_local_print()
    local_print(
        "New path for your database is made, "
        "restart the application to continue"
    )


def load_dbase() -> list:
    '''loads database to the code to work with it.'''
    from interact_funcs.base import read_row
    from data.const import PATH, ROLES
    user_model: dict = {}
    db = []
    with open(PATH, "rt", encoding="utf-8") as dbase:
        db_read: tuple = read_row(dbase.readline())
        for i in db_read:
            user_model[i] = ""
        for i in dbase.readlines():
            db.append(user_model)
            db[-1] = dict(zip(db_read, read_row(i)))
            if not all((
                (len(db[-1]) == 9),
                (db[-1]["ID"].isdigit()),
                (db[-1]["ROLE"] in ROLES)
            )):
                raise ValueError("Incorrect data in the database")
    return db


def save_dbase(dbase: list) -> None:
    '''uploads database to the main file.'''
    from interact_funcs.base import list_to_strtab
    from data.const import PATH
    log_front: str = list_to_strtab(dbase[0].keys())
    with open(PATH, "wt", encoding="utf-8") as file_save:
        print(log_front, file=file_save)
        for row in dbase:
            print(list_to_strtab(row.values()), file=file_save)


def fill_db() -> None:
    '''if database is empty, it will add superviser, database ready.'''
    from time import time, ctime
    from verification_funcs.password import checkpssw
    from interact_funcs.base import list_to_strtab
    from data.const import PATH, ORGPOL
    userdata: list = [0, ]
    print("\n\n\tSuper user identification: \n\n")
    for field in ORGPOL[1:-2]:
        if field == "PASSWORD":
            userdata.append(hash(checkpssw()))
        else:
            userdata.append(input(f"Type in new <{field}>: "))
    userdata.append(ctime(time()))
    userdata.append("Admin")
    with open(PATH, "wt", encoding="utf-8") as filldb:
        print(list_to_strtab(ORGPOL), file=filldb)
        print(list_to_strtab(userdata), file=filldb)


def checkbase(code: bool=False) -> bool:
    '''checks if database is exist or damaged.'''
    from os.path import exists
    from interact_funcs.user  import user_answer
    from data.const import PATH
    from localise_func.translator import get_local_print
    print = get_local_print()
    notification: str = ""
    if not exists(PATH) or code:
        if not code:
            notification = "Database does not exist"
        else:
            notification = "Database is damaged"
        if user_answer(
            "Do you want to create a new database?: ",
            notification=notification
        ):
            create_db()
        else:
            print("Database creation declined")
        return False
    with open(PATH, "rt", encoding="utf-8") as checkfile:
        data: list = checkfile.readlines()
        if not data or len(data) <= 1:
            if user_answer(
                "Do you want to fill in the database?: ",
                notification="Databse is empty"
            ):
                fill_db()
                return True
            print("Database fill declined")
            return True
        else:
            print("Database loaded sucsessfully.")
            return True