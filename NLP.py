import functions

import weather_data_load

import conversation



def chat_bot():
    know_list = [['you', 'are','not', 'cute'],['you', 'are', 'pretty']]
    answer_list = [['you too! :('],['you are pretty, too!']]
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
            
            print("You ask weather!")

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
            print(know_list)
            print(answer_list)
            print("Parden me?>_<")

chat_bot()
