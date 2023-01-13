import sqlite3

def openDb():
    # Create a connection to the database
    global conn
    conn = sqlite3.connect("accounts.db")
    # Create a cursor
    global c
    c = conn.cursor()

def closeDb():
    # Close the connection as always
    c.close()
    conn.close()

# Create a table
def createTable():
    openDb()

    c.execute('''
        CREATE TABLE IF NOT EXISTS accounts(
            First_Name TEXT,
            Last_Name TEXT,
            Username TEXT,
            Password TEXT,
            Data_Registered TEXT
        )
    ''')

    closeDb()

createTable()

# Create functions
def register(first, last, username, password, date):
    openDb()

    c.execute('''
        INSERT INTO accounts
        VALUES (?,?,?,?,?)
    ''', (first, last, username, password, date))
    conn.commit()

    closeDb()
    
def login(username, password):
    openDb()

    c.execute('''
        SELECT * FROM accounts
        WHERE username = (?) AND password = (?)
    ''', (username, password))

    data = c.fetchone()
    if data: 
        closeDb() 
        return True
    else:
        closeDb()
        return False

def get_accountInfo(username, password):
    openDb()

    c.execute('''
        SELECT * FROM accounts
        WHERE username = (?) AND password = (?)
    ''', (username, password))

    data = c.fetchone()
    closeDb()
    return data



def update_firstName(username, password, newfirstName):
    openDb()

    c.execute('''
        UPDATE accounts
        set First_Name = (?)
        WHERE Username = (?) AND Password = (?)
    ''', (newfirstName, username, password))
    conn.commit()

    closeDb()

def update_lastName(username, password, newlastName):
    openDb()

    c.execute('''
        UPDATE accounts
        set Last_name = (?)
        WHERE Username = (?) AND Password = (?)
    ''', (newlastName, username, password))
    conn.commit()

    closeDb()

def update_username(username, password, new_user):
    openDb()

    c.execute('''
        UPDATE accounts
        set Username = (?)
        WHERE Username = (?) AND Password = (?)
    ''', (new_user, username, password))
    conn.commit()

    closeDb()

def update_password(username, password, new_pass):
    openDb()

    c.execute('''
        UPDATE accounts
        set Password = (?)
        WHERE Username = (?) AND Password = (?)
    ''', (new_pass, username, password))
    conn.commit()

    closeDb()

def deleteData(username, password):
    openDb()

    c.execute('''
        DELETE FROM accounts
        WHERE Username = (?) AND Password = (?)
    ''', (username, password))
    conn.commit()

    closeDb()


########################
# register("Brian", "Tecson", "brian_tec", "bigboyz", "09-08-2022")
# update_firstName("paul_cruz", "zurclaup00", "JohnPa")
# deleteData("brian_tec", "bigboyz")
