
import random

class SimpleChatBot:
    def __init__(self):
        self.responses = { 
            "hello":["hi there, i am a chatbot made by haziq", "hello","i might not be friendly but pleased to meet you","greetings!"], 
            "how are you":["i am fine","i am depressed ","good"],
            "bye":["going already","you are leaving me alone? fine!!","good bye :("],
            "name": ["i am chatbot","why do you wanna know my name??","my name is larry"],
            "creator":["i was created by haziq"],
            "are you an ai":["no i am just a chatbot whose responces are pre registered and i give a rendom responces for each comman for each of your quesion"],
                            }
    def get_response(self, user_input):
        user_input = user_input.lower()

        for key  in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
            
        return "that statement is something i hadnt learnt"
    
def main():
    chatbot = SimpleChatBot()
    print("chatbox: HI! i am a simple chat bot made in python")

    while True:
        user_input = input("you:")
        if user_input.lower == 'bye':
            print("Chatbot:", chatbot.get_response(user_input))
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main() 