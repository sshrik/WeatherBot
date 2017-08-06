import functions

import weather_data_load

import conversation



def chat_bot():
    know_list = [['>_<'],['you', 'are','not', 'cute'],['you', 'are', 'pretty'],['are', 'you', 'hungry'],\
['are', 'you', 'sad']]
    answer_list = [['not cute. stop it.'],['you too! :('],['you are pretty, too!'],['i am machine, so i`m not hungry.','can you teach me what is \'hungry\' measn?'],\
['i`m machine, so i`m not sad.','Can you teach me what is feeling?']]
    conversation.print_answer("Hello there?")
    
    while True:
        
        input_value = conversation.get_input()
        
        code = conversation.get_talk_code(input_value, know_list, answer_list)
        
        if code == 0:
            # Teaching
            inputt = conversation.get_input("Teach me : ")
            answer = conversation.get_input("Answer is? : ")
            conversation.teach_language(inputt, answer, know_list, answer_list)
        elif code == 1:
            # ask weather.
            
            print("You ask weather! Wait a second...")

            # Get Country names.
            
            dt = conversation.get_country(input_value)
            
            
            for data in dt:
                
                tm = weather_data_load.load_city(data)
                
                functions.print_weather(data, tm)
        
        elif code == 2:
            # ask greeting.
            
            conversation.print_answer(functions.talk_greet())
        
        elif code == 3:
            # Border check.
            functions.start_game()
        
        elif code == 4:
            # Simple Say.
            conversation.print_answer(conversation.get_simple_say(input_value, know_list, answer_list))
        elif code == 5:
            conversation.print_answer("Bye friends~")
            exit()
        else :
            # Don`t know.
            print("Parden me?>_<")

chat_bot()
