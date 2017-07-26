import functions
import weather_data_load
import conversation

def chat_bot():
    conversation.print_answer("Hello?")
    while True:
        input_value = conversation.get_input()
        code = conversation.get_talk_code(input_value)
        
        if code == 1:
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
            print("No..!>_<")
        else :
            # Don`t know.
            print("Parden me?>_<")

chat_bot()
