# This is ID related ( sign-in and valid api-key ) Modules.
# This module can be used with Node server.

import sys
import pymongo as mogdb

def isIdExist(ID):
    '''
    ARGS : 
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        resultValue = Boolean value if id exists, return True, else, return false.
    '''

def getAPIKey(ID):
    '''
    ARGS : 
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        APIKey = Get appropriate api key with ID.
    '''

def signIn(ID):
    '''
    ARGS : 
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        APIKey = Get appropriate api key with ID.
    '''
    

def teachLanguage(input, output, id) :
    '''
    ARGS :
        input = 
        output = 
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        actionState = True, False or added, generated `s action state.
    '''

def talkToJavis(input, id) :
    '''
    ARGS :
        input =  
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
