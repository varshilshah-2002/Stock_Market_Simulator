import sqlite3 as db
from datetime import date

cnt = db.connect('storage.db')
try:
    cnt.execute('''CREATE TABLE PERSON(
        email TEXT PRIMARY KEY,
        password TEXT,
        balance REAL,
        net_profit REAL,
        net_loss REAL);''')
except:
    print("Log/database/PERSON TABLE ALREADY EXISTS")

try:
   # cnt.execute('''DROP TABLE TRANSACTION''')
    cnt.execute('''CREATE TABLE HISTORY(
        email TEXT,
        date TEXT,
        symbol TEXT,
        transaction_type TEXT,
        unit_cost REAL,
        qty INT);''')
except:
    print("Log/database/HISTORY ALREADY EXISTS")


def authenticate(email,input_password):

#Checks if user exists with email and input_password
    cursor = cnt.execute('''SELECT * FROM PERSON WHERE email = (?)''',[email])
    for i in cursor:
        if i[1] == input_password:
            print("Log/database/fun(authenticate)/authenticated:",i[0])
            return i  #authentication success, returns a tuple object
        else:
            return '-1' #incorrect password
    return '0' #user not found in db

def registerdb(email,input_password):
#Registers a new user with email and input_password
    tup = (email,input_password,5000,0,0)
    try:
        cnt.execute('''INSERT INTO PERSON VALUES((?),(?),(?),(?),(?))''',tup)
        print("Log/database/fun(authenticate)/registered:", email)
        cnt.commit()
        return True #registration success
    except:
        print("Log/database/fun(authenticate)/already-registered:", email)
        return False #registration fail, user already exists


# print(registerdb('sanat@123.com','12345'))
# print(authenticate('sanat@123.com','12345'))

#Operations related to PERSON table
def person_operations(email,op_type,op_parameter = None):
    if op_type == 0: #set_balance
        tup = (op_parameter,email)
        cnt.execute('''UPDATE PERSON SET balance = (?) WHERE email = (?)''', tup)
        print("Log/database/fun(authenticate)/updated balance for:", email)
        cnt.commit()
    elif op_type == 1: #get_balance
        cursor = cnt.execute('''SELECT balance FROM PERSON WHERE email = (?)''', [email])
        for i in cursor:
            return i[0]
    elif op_type == 2: #set net profit
        tup = (op_parameter,email)
        cnt.execute('''UPDATE PERSON SET net_profit = (?) WHERE email = (?)''', tup)
        print("Log/database/fun(authenticate)/net_profit updated for:", email)
        cnt.commit()
    elif op_type == 3: #get net profit
        cursor = cnt.execute('''SELECT net_profit FROM PERSON WHERE email = (?)''', [email])
        for i in cursor:
            return i[0]
    elif op_type == 4: #set net loss
        tup = (op_parameter,email)
        cnt.execute('''UPDATE PERSON SET net_loss = (?) WHERE email = (?)''', tup)
        print("Log/database/fun(authenticate)/net_loss updated for:", email)
        cnt.commit()
    elif op_type == 5: #get net loss
        cursor = cnt.execute('''SELECT net_loss FROM PERSON WHERE email = (?)''', [email])
        for i in cursor:
            return i[0]

'''
    Operations related to Transaction table
    op_type = 0 : Display current quantity for a email, stock pair
    op_type = 1 : Perform insert / update operations in History
        transction_type = 1 : Buy
        transaction_type = -1 : Sell
        unit_cost = cost of a unit share
        qty = units of share to be purchased / sold
'''
def transaction_operations(email,op_type,symbol = None ,transaction_type = None,unit_cost = None,qty = None):
    if op_type == 0: #get current quantity of a particular symbol, return quantity else return 0
        cursor = cnt.execute('''SELECT qty FROM HISTORY WHERE EMAIL = (?) and symbol = (?) and unit_cost IS NULL''', (email,symbol))
        for i in cursor:
            return i[0]  #return current quantity
        return 0  #If symbol absent then return 0
    if op_type ==1: #insert transaction
        currentdate = date.today()
        tuple = (email,currentdate,symbol,transaction_type,unit_cost,qty)
        cnt.execute('''INSERT INTO HISTORY VALUES((?),(?),(?),(?),(?),(?))''',tuple)
        cursor = cnt.execute('''SELECT qty FROM HISTORY WHERE EMAIL = (?) and symbol = (?) and unit_cost IS NULL ''',(email,symbol))
        flag = False
        old_qty = None
        for i in cursor:
            old_qty = i[0]
            flag = True
        if flag == False: #stock detail being entered for the first time
            cnt.execute('''INSERT INTO HISTORY VALUES((?),NULL,(?),NULL,NULL,(?))''',(email,symbol,qty))
        elif transaction_type == -1:
            new_qty = old_qty - qty
            cnt.execute('''UPDATE HISTORY SET qty = (?) WHERE email = (?) and symbol = (?) and unit_cost IS NULL''',(new_qty,email,symbol))
        elif transaction_type == 1:
            new_qty = old_qty + qty
            cnt.execute('''UPDATE HISTORY SET qty = (?) WHERE email = (?) and symbol = (?) and unit_cost IS NULL''',(new_qty,email, symbol))
        cnt.commit()

#For debug purpose only
def display_person():
    cursor = cnt.execute('''SELECT * FROM PERSON''')
    for i in cursor:
        print(i)

#return a list of tuples from HISTORY
def display_history(inpt_email):
    cursor = cnt.execute('''SELECT * FROM HISTORY WHERE email = (?) AND unit_cost IS NOT NULL''',[inpt_email])
    list_send = list()
    for i in cursor:
        list_send.append(i)
    return list_send

#drop all tuples from PERSON
def reset_person():
    cnt.execute('''DELETE FROM PERSON''')
    cnt.commit()

#drop all tuples from HISTORY
def reset_history():
    cnt.execute('''DELETE FROM HISTORY''')
    cnt.commit()

print(display_history('sanat@123'))