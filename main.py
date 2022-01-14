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
    if not var.isdigit():
        print('Not correct option')
        return False
    if int(var) < start or int(var) > end:
        print('Not correct option')
        return False
    else:
        print('Correct value')
        return True

def getUsers(): # Func to get a <List> with the users to the DB
    userLists = []
    cur.execute(
        "SELECT USERNAMES, ID_USERS FROM Users"
    )
    for USERNAMES, id_user in cur.fetchall():
        userLists.append(USERNAMES)
    return userLists

def userExists(name): # Func to check if the given var (only can be a string)  and returns True if exists but not returns False if not
    userLists = []
    cur.execute(
        "SELECT USERNAMES, ID_USERS FROM Users"
    )
    for USERNAMES, ID_USERS in cur.fetchall():
        userLists.append(USERNAMES)

    for username in userLists:
        if username == name:
            return True

def getBanner(tittle): # Func to print a banner with the given name
    print('='*32)
    print('*'*12 + '{}' + '*'*12).format(tittle)
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

def checkUsername(user): # Func to check if the given user is a valid user
    if not user.isalnum():
        print('{} is no alphanumeric'.format(user))
        return False
    if len(user) < 8 or len(user) > 12:
        if len(user) < 8:
            print('{} minimum lenght is 8 characters, username not allowed'.format(user))
        else:
            print('{} maximum lenght is 12 characters, username not allowed'.format(user))
        return False
    else:
        print('{} accepted'.format(user))
        return True

def checkPassword(password): # Func to check if the given password is a valid user
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
            return "La id introducida ya existe"


    sysdate = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute(f"insert into USER values ('{id}','{user}','{password}','LaMaquinita','{sysdate}',null,null)")
    conn.commit() # Save the changes to the DB