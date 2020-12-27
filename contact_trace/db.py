import sqlite3 as lite
from sqlite3 import connect
import sys, os

config1 = 'ct_database\database1.db'
config2 = 'scripts.sql'
config3 = 'scripts1.sql'
config4 = 'scripts2.sql'

if getattr(sys, 'frozen', False):
    filepath = os.path.dirname(sys.executable)
elif __file__:
    filepath = os.path.dirname(__file__)
    

config_path1 = os.path.join(filepath, config1)
config_path2 = os.path.join(filepath, config2)
config_path3 = os.path.join(filepath, config3)
config_path4 = os.path.join(filepath, config4)


try:
    cxn = connect(config_path1, check_same_thread = False)
except lite.OperationalError:
    os.mkdir(filepath + '\\ct_database')
finally:
    cxn = connect(config_path1, check_same_thread = False)
cur = cxn.cursor()


# filepath = os.path.dirname(os.path.abspath(__file__))
# print(filepath)
# assert os.path.exists(filepath)
# cxn = connect(config_path1)


# filepath2 = os.path.abspath(os.path.dirname(__file__))
# assert os.path.exists(filepath2)

# try:
#     cxn = connect(f"{os.path.abspath(os.path.dirname(__file__))}\\ct_database\\database1.db", check_same_thread = False)
# except lite.OperationalError:
#     os.mkdir(f'{os.path.abspath(os.path.dirname(__file__))}\\ct_database')
# finally:
#     cxn = connect(f"ct_database\\database1.db", check_same_thread = False)
cur = cxn.cursor()

def with_commit(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        commit()
    return inner    
    
@with_commit
def build():
    scriptexec(config_path2)
    scriptexec(config_path3)
    scriptexec(config_path4)

#-------------------------------------------------------------------------------
#idk if I need any of this
   
def commit():
    cxn.commit()
    
def close():
    cxn.close()
    
def field(command, *values):
    cur.execute(command, tuple(values))
    if (fetch := cur.fetchone()) is not None:
        return fetch[0]
    
def record(command, *values):
    cur.execute(command, tuple(values))
    return cur.fetchone()

def records(command, *values):
    cur.execute(command, tuple(values))
    return cur.fetchall()

def column(command, *values):
    cur.execute(command, tuple(values))
    return [item[0] for item in cur.fetchall()]

def execute(command, *values):
    cur.execute(command, tuple(values))

def multiexec(command, valueset):
    cur.executemany(command, valueset)
    
def scriptexec(filename):
    with open(filename, "r") as script:
        cur.executescript(script.read())