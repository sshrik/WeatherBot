from nltk.stem import PorterStemmer
import re


# Sim = simmilarity.



def get_input(input_string=-1):

    if input_string == -1:
        return_value = input("You : ")
    
    else:
        return_value = input(input_string + " : ")
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



def get_talk_code(inputt, know_list, answer_list):
    
    data = tokenize(inputt)

    if check_teach(data):
        return 0 # Teach language.
    elif check_ask_weather(data):
        
        return 1 # Ask Weather.
    
    elif check_ask_greeting(data):
        
        return 2 # Ask Greeting.
    
    elif check_border(data):
        
        return 3 # Border check.
    
    elif check_simple_say(data, know_list, answer_list):
        
        return 4 # Simple conversation.

    elif check_exit(data):
        return 5 # exit conversation.
    else:
        return -1



def teach_language(inputt, answer, know_list, answer_list):
    data = tokenize(inputt)

    if data in know_list:
        answer_list[get_list_in(data, know_list)].append(answer)
    else:
        know_list.append(data)
        answer_list.append(answer)

def get_one_answer(answer_list, i):
    import random
    if len(answer_list[i]) == 1 : return answer_list[i][0]
    else : return answer_list[i][random.randint(0, len(answer_list[i]))]

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


def check_simple_say(data, know_list, answer_list):    
    sim = False

    sim_list = []

    for knowing in know_list:
        sim_list.append(get_simmilarity(data, knowing))

    for simeli in sim_list:
        if simeli > 0.65:
            sim = True
    return sim


def get_simple_say(inputt, know_list, answer_list):
    data = tokenize(inputt)

    sim_list = []
    for knowing in know_list:
        sim_list.append(get_simmilarity(data, knowing))

    # Initailize return.
    return_sim = -1
    return_value = "...!"

    for sim in range(0, len(sim_list)):
        if sim_list[sim] > return_sim:
            return_sim = sim_list[sim]
            return_value = get_one_answer(answer_list, sim)

    return return_value


def check_list_in(list1, list2):
    
    # Check if at least one of list1 is in list2.
    
    return_value = False

    
    for l1 in list1:
        if l1 in list2:
            return_value = True
    
    
    return return_value



def get_list_in(list1, list2):
    
    # Check where is list1 is in list2.
    
    return_value = -1
    
    for l2 in list2:


        if list1 == l2:
            return_value = list2.index(l2)
    return return_value


def check_border(data):
    
    sim = False
    
    bord_list = ["border", "game", "play", "bore", "fun", "nothing", "anything"]
    
    
    if count_list_in(bord_list, data) > 0:
        
        sim = True
    
    
    return sim

def check_teach(data):
    if "<teach>" in data:
        return True
    else:
        return False



def count_list_in(list1, list2):
    
    # Check how many number in list1 is in list2.
    
    return_value = 0

    
    for l1 in list1:
        
        if l1 in list2:
            
            return_value += 1
    
    
    return return_value


def get_simmilarity(list1, list2):
    return count_list_in(list1, list2) / len(list2)
