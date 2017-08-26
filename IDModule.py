# This is ID related ( sign-in and valid api-key ) Modules.
# This module can be used with Node server.
# Referenced 1 : http://meonggae.blogspot.kr/2016/08/nodejs-python-shell-python.html
# Referenced 2 : http://ngee.tistory.com/335

import sys
import pymongo as mogdb
import uuid
import random

def isIdExist(ID):
    '''
    ARGS : 
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        resultValue = Boolean value if id exists, return True, else, return false.
    '''
    collection = connectToMasterDB()
    signInSchema = collection["signIn"]

    IDList = signInSchema.find({"ID" : ID})
    if IDList.count() > 0:
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
    collection = connectToMasterDB()
    signInSchema = collection["signIn"]
    # SIGNIN Schema has id and api key list.

    IDList = signInSchema.find({"ID" : ID})
    print(IDList[0][u"APIKey"]) # Node can read with console print.
    return IDList[0][u"APIKey"]

def signIn(ID):
    '''
    ARGS : 
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        APIKey = Get appropriate api key with ID.
    '''
    collection = connectToMasterDB()
    signInSchema = collection["signIn"]

    IDList = signInSchema.find({"ID" : ID})

    APIKey = generateAPIKey(ID)
    listSize = signInSchema.find({"APIKey" : APIKey}).count()

    # While there is no APIKey in Database...
    while listSize != 0:
        APIKey = generateAPIKey(ID)
        listSize = signInSchema.find({"APIKey" : APIKey}).count()
    
    signInSchema.insert({"ID":ID, "APIKey": APIKey})
    print(APIKey) # Node can read with console print.
    return APIKey
    

def teachLanguage(inputData, output, id) :
    '''
    ARGS :
        inputData = what you are says.
        output = what javis want to say about this.
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        actionState = True, False or added, generated `s action state.
    '''
    database = connectToNonMasterDB(id+"Language")
    # SIGNIN Schema has id and api key list.
    collection = database.conversation;

    languageList = collection.find({u"input":inputData})
    if languageList.count() == 0:
        # If not exist, insert it.
        collection.insert({u"input":inputData, u"output":[output], "id":id})
        return False
    else:
        # If exist, same language is not in there, update it.
        if output in languageList[0][u"output"]:
            return False
        else:
            collection.update({u"input":inputData, u"output":(languageList[0][u"output"]), u"id":id},\
                              {u"input":inputData, u"output":(languageList[0][u"output"] + [output]), u"id":id})
            return True

def teachWordTag(tag, word, id):
    '''
    ARGS :
        tag = the general / representative meaning of word.
        word = the real word.
        id = which id you want to add.
    RETURNS :
        actionState = True, False or added, generated `s action state.
    '''
    database = connectToNonMasterDB(id+"wordTag")
    collection = database.conversation;

    wordList = collection.find({"tag": tag})
    if wordList.count() == 0:
        # If not exist, insert it.
        collection.insert({"tag":tag, "word":[word], "id":id})
        return False
    else:
        # If exist, same language is not in there, update it.
        if word in wordList[0][u"word"]:
            return False
        else:
            collection.update({"tag":tag, "word":wordList[0]["word"], "id":id}, \
                              {"tag":tag, "word":wordList[0]["word"] + [word], "id":id})
            return True

def teachSenctenceTag(tag, sentence, id):
    '''
    ARGS :
        tag = the general / representative meaning of sentence.
        sentence = the real sentence.
        id = which id you want to add.
    RETURNS :
        actionState = True, False or added, generated `s action state.
    '''
    database = connectToNonMasterDB(id+"sentenceTag")
    # SIGNIN Schema has id and api key list.
    collection = database.conversation;

    sentenceList = collection.find({u"tag":tag})
    if sentenceList.count() == 0:
        # If not exist, insert it.
        collection.insert({u"tag":tag, u"sentence":[sentence], u"id":id})
        return False
    else:
        # If exist, same language is not in there, update it.
        if sentence in sentenceList[0][u"sentence"]:
            return False
        else:
            collection.update({u"tag":tag, u"sentence":sentenceList[0][u"sentence"], u"id":id}, \
                          {u"tag":tag, u"sentence":sentenceList[0][u"sentence"] + [sentence], u"id":id})
        return True

def talkToJavis(inputData, id) :
    '''
    ARGS :
        input = what you are says.
        ID  = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        resultValue = Boolean value if id exists, return True, else, return false.
    '''
    database = connectToNonMasterDB(id+"Language")
    # SIGNIN Schema has id and api key list.
    collection = database.conversation;

    languageList = collection.find({"input":inputData})
    if languageList.count() == 0:
        # If not exist, return False and say ERROR:404.
        print("ERROR:404")
        return False
    else:
        # If exist, return True and say anything.
        outputList = languageList[0][u"output"]
        return outputList[random.randint(0, len(outputList))]

# TODO
def forgetTag(tag, id):
    '''
    '''

def forgetWordTag(tag, word, id):
    '''
    '''

def forgetWord(word, id):
    '''
    '''

def forgetSentenceTag(tag, sentence, id):
    '''
    '''

def forgetSentence(sentence, id):
    '''
    '''

def forgetConversation(input, id):
    '''
    '''

def forgetConversationOutput(input, output, id):
    '''
    '''
# TODO

def connectToMasterDB(to='localhost',port=27017):
    '''
    ARGS :
        to = where the db is located ip. Default is localhos, 127.0.0.1.
        port = where the db is located port. Default is 27017.
    RETURNS :
        databasePlace = where can find data.
    '''
    connection = mogdb.MongoClient(to, port)
    databasePlace = connection["master"]

    return databasePlace

def connectToNonMasterDB(id, to='localhost',port=27017):
    '''
    ARGS :
        to = where the db is located ip. Default is localhos, 127.0.0.1.
        port = where the db is located port. Default is 27017.
    RETURNS :
        databasePlace = where can find data.
    '''
    connection = mogdb.MongoClient(to, port)
    databasePlace = connection[id]

    return databasePlace

def generateAPIKey(ID):
    '''
    ARGS :
        ID = ID which user makes. Can be seperated with Javis`s save locate.
    RETURNS :
        APIKey = api key with given ID.
    '''
    # Reference to http://ngee.tistory.com/562
    return str(uuid.uuid4()).replace("-","")

# connectToDB()
if len(sys.argv) == 1:
    print("Wrong Function call.")
elif sys.argv[1] == "isIdExist" :
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