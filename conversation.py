from nltk.stem import PorterStemmer
import re


# Sim = simmilarity.


def get_input():
    
    return_value = input("You : ")
    
    return return_value


def print_answer(answer):
    
    name = "Javis"
    
    print(name + " : " + answer)
    
    return 0



def tokenize(inputt):
    
    # Delete `s or etc ...
    
    input_str = re.sub("`.","",inputt)
    
    # Delete ?! and ., ...
    
    input_str = re.sub("[!?.,~]","",input_str)
    
    tok = input_str.split(" ")

    
    for eli in range(0, len(tok)):
        
        if tok[eli] == "kuala":
            
            tok[eli] = "kuala lumpur"
        
        if tok[eli] == "delhi":
            
            tok[eli] = "new delhi"

    
    return_value = []

    
    st = PorterStemmer()

    for token in tok:
        
        return_value.append(st.stem(token))
    
    
    return return_value



def get_talk_code(inputt):
    
    data = tokenize(inputt)
    
    if check_ask_weather(data):
        
        return 1 # Ask Weather.
    
    elif check_ask_greeting(data):
        
        return 2 # Ask Greeting.
    
    elif check_border(data):
        
        return 3 # Border check.
    
    elif check_simple_say(data):
        
        return 4 # Simple conversation.

    elif check_exit(data):
        return 5 # exit conversation.
    else:
        
        return -1



def check_exit(data):
    exit_list = ["exit", "bye", "quit"]
    if check_list_in(data, exit_list):
        return True
    return False


def check_ask_weather(data):
    
    sim = False
    
    city_list = ["seoul","kuala lumpur", "london", "new delhi", "beijing"]

    
    
    if check_list_in(city_list, data) and ("what" in data or "weather" in data):
        
        sim = True
    
    
    return sim



def check_ask_greeting(data):
    
    sim = False
    
    greet_list = ["hello","hi", "how", "me", "greet", "you", "what", "up", "bro"]

    
    
    if count_list_in(greet_list, data) > len(data) / 3:
        
        sim = True

    
    return sim



def get_country(inputt):
    
    data = tokenize(inputt)
    
    country = []
    
    city_list = ["seoul","kuala lumpur", "london", "new delhi","beijing"]


  
    for dt in data:
        
        if dt in city_list:
            
            country.append(dt)    
    
    
    return country



def check_simple_say(data):
    
    sim = False

    
    return sim



def check_list_in(list1, list2):
    
    # Check if at least one of list1 is in list2.
    
    return_value = False

    
    for l1 in list1:
        
        if l1 in list2:
            
            return_value = True
    
    
    return return_value



def check_border(data):
    
    sim = False
    
    bord_list = ["border", "game", "play", "bore", "fun", "nothing", "anything"]
    
    
    if count_list_in(bord_list, data) > 0:
        
        sim = True
    
    
    return sim



def count_list_in(list1, list2):
    
    # Check how many number in list1 is in list2.
    
    return_value = 0

    
    for l1 in list1:
        
        if l1 in list2:
            
            return_value += 1
    
    
    return return_value
