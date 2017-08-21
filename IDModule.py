# This is ID related ( sign-in and valid api-key ) Modules.
# This module can be used with Node server.

import sys
import pymongo as mogdb

connection = mogdb.MongoClient('localhost', 27017)

def isIdExist(ID):
    '''
    ARGS : 
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        resultValue = Boolean value if id exists, return True, else, return false.
    '''
    IDList = connection.find({"ID" : ID})
    if len(IDList) > 0:
        print("True") # Node can read with console print.
        return True
    else:
        print("False") # Node can read with console print.
        return False

def getAPIKey(ID):
    '''
    ARGS : 
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        APIKey = Get appropriate api key with ID.
    '''
    IDList = connection.find({"ID" : ID})
    print(IDList.APIKey) # Node can read with console print.
    return IDList.APIKey

def signIn(ID):
    '''
    ARGS : 
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        APIKey = Get appropriate api key with ID.
    '''
    APIKey = generateAPIKey(ID)

    print(APIKey) # Node can read with console print.
    return APIKey
    

def teachLanguage(input, output, id) :
    '''
    ARGS :
        input = what you are says.
        output = what javis want to say about this.
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        actionState = True, False or added, generated `s action state.
    '''

def talkToJavis(input, id) :
    '''
    ARGS :
        input = what you are says.
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        resultValue = Boolean value if id exists, return True, else, return false.
    '''

def connectToDB(to='localhost',port=27017):
    '''
    ARGS :
        to = where the db is located ip. Default is localhos, 127.0.0.1.
        port = where the db is located port. Default is 27017.
    RETURNS :
        resultValue = Boolean value if id exists, return True, else, return false.
    '''
    mogdb.MongoClient(to, port)

def generateAPIKey(ID):
    '''
    ARGS :
        ID = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        APIKey = api key with given ID.
    '''
    return ID

# connectToDB()
if sys.argv[1] == "isIdExist" :
    sys.argv[1](sys.argv[2])
elif sys.argv[1] == "getAPIKey":
    sys.argv[1](sys.argv[2])
elif sys.argv[1] == "signIn":
    sys.argv[1](sys.argv[2])
elif sys.argv[1] == "teachLanguage":
    sys.argv[1](sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1] == "talkToJavis":
    sys.argv[1](sys.argv[2], sys.argv[3])
else :
    print("Wrong Function call.")