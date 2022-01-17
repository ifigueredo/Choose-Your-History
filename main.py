import pymysql
from datetime import datetime

conn = pymysql.connect( # We start the connection with the MySQL Server 
    host="13.80.74.30",
    port = 3306,
    user="LaMaquinita",
    password="1233",
    db="CHOSE_YOUR_STORY"
)

cur = conn.cursor()

# Iván

def checkVarInt(var,start,end): # Func to check if the given var is a valid int | start and end are the vars to select the avaiable rank of numbers
    var = str(var)
    if not var.isdigit():
        print('Not a correct option')
        return False
    if int(var) < start or int(var) > end:
        print('Not a correct option')
        return False
    else:
        return True

def getUsers(): # Func to get a <List> with the users to the DB
    userLists = []
    cur.execute(
        "SELECT Usernames, id_users FROM USER"
    )
    for Usernames, id_users in cur.fetchall():
        userLists.append(Usernames)
    return userLists

def userExists(name): # Func to check if the given var (only can be a string)  and returns True if exists but not returns False if not
    userLists = []
    cur.execute(
        "SELECT Username, id_user FROM USER"
    )
    for Username, id_user in cur.fetchall():
        userLists.append(Username)

    for username in userLists:
        if username == name:
            return True

def correctPassword(Username, password):
    userRealPassword = []
    cur.execute(
        f"SELECT Password FROM USER where Username = '{Username}'"
    )

    for Password in cur.fetchall():
        userRealPassword.append(Password)
    if userRealPassword[0][0] == password:
        return True
    else:
        print('Incorrect password')
        return False

def getBanner(tittle): # Func to print a banner with the given name
    print('='*32)
    print('*'*11 + tittle + '*'*10)
    print('='*32)

def getHeaderFromTuples(cols, sizes): # Func to print many columns separated by the given values
    print('='*70)
    print('Column 1'.ljust(sizes[0]) + 'Column 2'.ljust(sizes[1])+ 'Column 3'.ljust(sizes[2]))
    print('='*70)
    '''
        cols = ('Col1', 'Col2','Col3' )
        sizes = (20,35,50)
        getHeaderFromTuples(cols, sizes)
    '''

def create_checkUsername(username): # Func to check if the given user is a valid user
    if not str(username).isalnum():
        print('{} is no alphanumeric'.format(username))
        return False
    if len(username) < 8 or len(username) > 12:
        if len(username) < 8:
            print('{} minimum lenght is 8 characters, username not allowed'.format(username))
        else:
            print('{} maximum lenght is 12 characters, username not allowed'.format(username))
        return False
    else:
        print('{} accepted'.format(username))
        return True

def create_checkPassword(password): # Func to check if the given password is a valid user
    validUsername,validPassword,digit, lower, upper, space, alphanum, notAlphanum = False, False, False, False, False, False, False, False
    for i in range(len(password)):
        if password[i].isdigit() == True:
            digit = True
        if password[i].islower() == True:
            lower = True
        if password[i].isupper() == True:
            upper = True
        if password[i].isspace() == True:
            space = True
        if password[i].isalnum() == True:
            alphanum = True
        if password[i].isalnum() == False:
            notAlphanum = True

    if alphanum == True and len(password) >= 8 and digit == True and lower == True and upper == True and space is not True:
        print(">> PASSWORD ACCEPTED")
        return True
    else:
        print('No valid password')
        return False

def getUserIds(): # Func to get a <List> with the users and the Ids on this way [[Usernames],[Ids]]
    userNames, userIds,listUsers = [], [], []
    cur.execute(
        "SELECT Username, id_user FROM Users"
    )
    for Username, id_user in cur.fetchall():
        userNames.append(Username)
        userIds.append(id_user)
    listUsers.append(userNames)
    listUsers.append(userIds)
    return listUsers

def InsertUser(id,user,password): # Func to insert a user to the DB with the givin values
    if id < 0: # We check if the given ID is negative
        return "La id no puede ser negativa"

    cur.execute(
        "select id_user from USER"
    )
    users_id = cur.fetchall()

    for i in users_id:
        if i[0] == int(id):
            return "The given ID exists on the database"

    sysdate = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute(
        f"insert into USER values ('{id}','{user}','{password}','LaMaquinita','{sysdate}',null,null)"
    )
    conn.commit() # Save the changes to the DB

def getIdGame(): # Get ID Games it will return a <List> of integers
    gamesID = []
    cur.execute(
        "SELECT id_game FROM GAME"
    )
    for id_game in cur.fetchall():
        gamesID.append(id_game)
    return gamesID

def formaText1(text): # Function to format all the text
    
    x = text
    y = ''
    z = ''
    for i in x:
        y += i
        if len(y) >= 105 and i.isspace():
            z = z + y + '\n'
            y =  ' '
        
    z = z + y 
    print(z)

def adventureBanner(): # Get the adventure banner
    print('Adventure banner')

# Menu system

def mainMenu(): # Main menu function to select all the options
    while 1:
        print('1) Login\n2) Create User\n3) Replay adventure\n4) Reports\n5) Exit\n\n')
        opc = input('Option: ')
        print(opc)
        if checkVarInt(opc, 1, 5):
            if int(opc) == 1:
                if loginMenu():
                    adventureBanner()
                    input('Enter to continue\n\n')
            if int(opc) == 2:
                createUser()
            if int(opc) == 3:
                replayAdventure()
            if int(opc) == 4:
                reports()
            if int(opc) == 5:
                exit()

def loginMenu(): # Function to start the gamming with a login system targeting to the DB
    username = input('Username:\n')
    if userExists(username):
        password = input('Password:\n')
        if correctPassword(username, password):
            return True
    else:
        print("The username doesn't not exists on the Database")
    
def createUser(): # Func to create a new user and add it with InsertUser to the DB
    while True:
        getBanner('Create user')
        username = input('Username: ')
        if create_checkUsername(username):
            password = input('Password: ')
            if create_checkPassword(password):
                InsertUser(100, username, password)
                return True

def replayAdventure(): # Func to replay the released games
    print('hi replay')                              

#if __main__ == '__name__':
    #mainMenu()