import pymysql
from datetime import datetime

conn = pymysql.connect( # We start the connection with the MySQL Server 
    host="20.61.60.74",
    port = 3306,
    user="LaMaquinita",
    password="1233",
    db="CHOSE_YOUR_STORY"
)

cur = conn.cursor()

max_lenght = 120
allGameSteps = []
actualStep = 1
actualAdventure = 0
logedUser = ''

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

def correctPassword(Username, password): # This function checks if the given password linked to the username is the correct one for this user
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

def getBanner(tittle,max_lenght): # Func to print a banner with the given name
    print('='*max_lenght)
    sides = max_lenght-len(tittle)+1 / 2
    if sides % 2 == 0:
        print('*'*int(sides/2) + tittle + '*'*int(sides/2))
    else:
        print('*'*int((sides+1)/2) + tittle + '*'*int(sides/2))
    print('='*max_lenght)
    print('')

def getHeaderFromTuples(cols, sizes): # Func to print many columns separated by the given values
    print('='*120)
    print(f'{cols[0]}'.ljust(sizes[0]) + f'{cols[1]}'.ljust(sizes[1])+ f'{cols[2]}'.ljust(sizes[2]))
    print('='*120)

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
    if 1 < 0: # We check if the given ID is negative
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

def formatText(string, max_lenght):
    printable = ''
    final = []
    for i in range(len(string)):
        if i == len(string) - 1:
            printable = printable + str(string[i])
            final.append(printable)
        if len(printable) >= max_lenght:
            final.append(printable)
            printable = ''
        else:
            printable = printable + str(string[i])
    return final

def getDiccAdventures():

    query = f"Select * from ADVENTURE"

    cur.execute(query)

    table = cur.fetchall()

    adventures = {}

    indx = 1

    for i in table:
        adventures[indx] = {"Name": i[1], "Description": i[2], "characters": i[3]}
        indx = indx + 1

    return (adventures)

def get_table(query):
    box=[]
    list_names=[]
    cur.execute(query)
    values = cur.fetchall()
    names = cur.description
    for i in names:
        list_names.append(i[0])
    box.append(tuple(list_names))
    for j in values:
        box.append(j)
    box = tuple(box)
    return box

def get_characters(): # Mirar pasar a un diccionario 
    userLists = []
    userid= []
    dicc = {1:{'Name': ''}}
    cur.execute(
        "SELECT Name , id_character FROM CHARACTERS ORDER BY NAME asc" 
        )
    for Name , id_character in cur.fetchall():
        userLists.append(Name)
        userid.append(id_character)
    for i in range(len(userLists)):
        dicc[userid[i]] = {"Name": userLists[i]}
    print(dicc)

def loginMenu(): # Function to start the gamming with a login system targeting to the DB
    username = input('Username: ')
    if userExists(username):
        password = input('\nPassword: ')
        if correctPassword(username, password):
            return True
    else:
        print("The username doesn't not exists on the Database")

def selectAdventure():
    table = getDiccAdventures()
    getBanner('Adventures', max_lenght)
    print('')
    getHeaderFromTuples(('Name', 'Description', 'Characters'), (40,60,max_lenght)) 
    print('')
    for i in range(len(table)):
        fullDescription = ''
        names = formatText(str(table[i+1]['Name']), 35)
        descriptions = formatText(str(table[i+1]['Description']), 55)
        characters = formatText(str(table[i+1]['characters']), 95)

        print(names[0].ljust(39) + descriptions[0].ljust(61) + characters[0].ljust(80))
        print('')
    opc = input('Adventure select: ')
    if checkVarInt(opc, 1, len(names)):
        print(f'\nSelected adventure number {opc}\n')
        return opc

def get_Step(id_adventures, id_step):
    test = []
    cur.execute(
        f'select id_steps , Description from STEP where id_adventures = {id_adventures} '
    )
    Steps=cur.fetchall()
    ListaSteps=[]
    for i in Steps:
        ListaSteps.append(i)
    getBanner('STEPS',max_lenght)
    for mr in ListaSteps:
        description=[str(mr[1]).split("\n")]
        cadena=""
        for j in description:
            if len(j)>1:
                cadena=j[0]+"\n".ljust(37)+j[1]
                print("\n".ljust(15),mr[0],"".ljust(18),(formatText(cadena,max_lenght))[0],"\n")
            else:
                cadena = j[0]
                print("".ljust(14),mr[0],"".ljust(18),(formatText(cadena,max_lenght))[0],"\n")

def gameInsert(id_user, id_character, id_adventure):
    cur.execute(
        f"select max(id_game) from GAME"
    )
    maxID = cur.fetchone()
    gameID = int(maxID[0]) + 1


    sysdate = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute(
        f"insert into GAME values ('{gameID}','{id_user}','{id_character}','{id_adventure}','{sysdate}','LaMaquinita@79.156.212.72','{sysdate}', null, null)"
    )
    conn.commit()

def characterSelect(id_adventure):
    getBanner(' Character selection ', max_lenght)
    cur.execute(
        f"select id_characters from ADVENTURE where id_adventures = {id_adventure}"
    )
    charList = cur.fetchall()
    charList = list(charList)
    for i in range(len(charList)):
        charList[i] = list(charList[i])
    characterFinal = []
    if len(charList) == 1:
        cur.execute(
            f"select Name from CHARACTERS where id_character = {charList[0][0]}"
        )
        charName = cur.fetchone()
        characterFinal.append(charName)
    else:
        for i in range(len(charList)):
            cur.execute(
                f"select Name from CHARACTERS where id_character = {charList[i][0]}"
            )
            charName = cur.fetchone()
            characterFinal.append(charName)

    for i in range(len(characterFinal)):
        print('\n' + ' ' * 20 + str(i+1) + ' ' * 20 +  str(characterFinal[i][0]))
    print('')
    opc = input('Select player: ')
    if checkVarInt(opc, 1, len(characterFinal)):
        print('\n' + str(characterFinal[0][int(opc)-1]) + ' selected to play \n')
        return str(characterFinal[0][int(opc)-1])

def getOption(id_adventure, id_step):
    AdventureSteps = []
    cur.execute(
        f"select id_steps from OPTIONS group by id_steps"
    )
    steps = cur.fetchall()
    for i in steps:
        AdventureSteps.append(list(i))
    cur.execute(
        f"select final_step from STEP where id_steps = {id_step}"
    )
    isFinal = cur.fetchone()
    if isFinal[0] != 1:

        title = ' Story '
        getBanner(title,max_lenght)

        cur.execute(
            f"select Description from STEP where id_steps = {id_step}"
        )
        Des_step = cur.fetchone()
        Des_step = str(Des_step[0]).split("\n")
        
        if len(Des_step) != 1:
            cadena_opt = Des_step[0] + Des_step[1]
        else:
            cadena_opt = Des_step[0]
        print("\n".ljust(15),(formatText(cadena_opt,max_lenght))[0],"\n")

        title = ' Options '
        getBanner(title,max_lenght)
            
        cur.execute(
            f"select id_options , Description from OPTIONS where id_steps = {id_step} and id_adventures = {id_adventure}"
        )
        Options=cur.fetchall()
        ListaOptions=[]
        for i in Options:
            ListaOptions.append(i)
        k = 0
        for mo in ListaOptions:
            k +=1
            desc_opt = [str(mo[1]).split("\n")]
            cadena = ""
            for j in desc_opt:
                if len(j) > 1:
                    cadena = j[0] + "\n".ljust(37) + j[1]
                    print("\n".ljust(15), str(k), "".ljust(18), (formatText(cadena, max_lenght))[0], "\n")
                else:
                    cadena = j[0]
                    print("\n".ljust(15), str(k), "".ljust(18), (formatText(cadena, max_lenght))[0], "\n")

        opc = input('Option: ')
        if checkVarInt(opc, 1, k):
            cur.execute(
                f"select Response from OPTIONS where id_steps = {id_step} and id_options = {opc}"
            )
            test = cur.fetchone()
            test = list(test)
            getBanner(' Adventure log  ', max_lenght)
            printable = test[0].ljust(45)
            print('\n' + ' '*20 + test[0].ljust(45) + '\n')
            print('='*max_lenght)
        
        for i in range(len(AdventureSteps)):
            if AdventureSteps[i][0] == id_step:
                print(AdventureSteps[i][0])
        AdventureSteps.pop(i-1)

        getOption(id_adventure, AdventureSteps[0][0])
    else:
        title = ' Story '
        getBanner(title,max_lenght)

        cur.execute(
            f"select Description from STEP where id_steps = {id_step}"
        )
        Des_step = cur.fetchone()
        Des_step = str(Des_step[0]).split("\n")
        if len(Des_step) != 1:
            cadena_opt = Des_step[0] + Des_step[1]
        else:
            cadena_opt = Des_step[0]

        print("\n".ljust(15),(formatText(cadena_opt,max_lenght))[0],"\n")

        title = ' Options '
        getBanner(title,max_lenght)
            
        cur.execute(
            f"select id_options , Description from OPTIONS where id_steps = {id_step} and id_adventures = {id_adventure}"
        )
        Options=cur.fetchall()
        ListaOptions=[]
        for i in Options:
            ListaOptions.append(i)
        k = 0
        for mo in ListaOptions:
            k +=1
            desc_opt = [str(mo[1]).split("\n")]
            cadena = ""
            for j in desc_opt:
                if len(j) > 1:
                    cadena = j[0] + "\n".ljust(37) + j[1]
                    print("\n".ljust(15), str(k), "".ljust(18), (formatText(cadena, max_lenght))[0], "\n")
                else:
                    cadena = j[0]
                    print("\n".ljust(15), str(k), "".ljust(18), (formatText(cadena, max_lenght))[0], "\n")
        opc = input('Option: ')
        if checkVarInt(opc, 1, k):
            if opc == 1:   
                cur.execute(
                    f"select * from OPTIONS where id_options = {4} and id_steps = {6}"
                )
            else:
                cur.execute(
                    f"select Response from OPTIONS where id_options = {5} and id_steps = {6}"
                )
            test = cur.fetchall()
            getBanner(' Adventure log  ', max_lenght)
            print('\n' + ' '*20 + str(test[0][0]) + '\n')
            print('='*max_lenght)

        print('\nFIN\n\n\n')

def createUser(): # Func to create a new user and add it with InsertUser to the DB
    while True:
        getBanner('Create user', max_lenght)
        username = input('Username: ')
        if create_checkUsername(username):
            password = input('Password: ')
            if create_checkPassword(password):
                cur.execute(
                    f"select max(id_user) from USER"
                )
                maxID = cur.fetchone()
                InsertUser(maxID[0] + 1, username, password)
                conn.commit()
                return True

def replayAdventure(): # Func to replay the released games
    print('hi replay')

def reports():
    print('hi reports')

def mainMenu(): # Main menu function to select all the options
    while 1: 
        getBanner(' MAIN MENU ', max_lenght)
        print('1) Login\n2) Create User\n3) Replay adventure\n4) Reports\n5) Exit\n')
        opc = input('Option: ')
        print('')
        if checkVarInt(opc, 1, 5):
            if int(opc) == 1:
                getBanner('User login', max_lenght)
                print('')

                if loginMenu():
                    id_adventures = selectAdventure()
                    id_character = characterSelect(id_adventures)                                                                                                                                                                     
                    getOption(id_adventures,actualStep)
                    # gameInsert()
            if int(opc) == 2:
                if createUser():
                    print('\nThe user is has been added into the Database')
                else:
                    print('\nThe user has not been added to the Database')
            if int(opc) == 3:
                replayAdventure()
            if int(opc) == 4:
                reports()
            if int(opc) == 5:
                exit()

mainMenu()