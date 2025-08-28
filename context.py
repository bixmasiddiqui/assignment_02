#chatbot

def chatbot_response(user_input: str)-> str:
    #Agent identity
    context = "you are a helpful FAQ bot."

    #question/answers
    responses = {
        "what is your name?":  "I am FAQ Bot, created to answers simple questions.",
        "what can you do?": "I can answer a set of predefined FAQ questions.",
        "how are you?": "I am just a bot, but I’m functioning perfectly!",
        "where are you from?": "I live inside your computer 😊",
        "bye": "Goodbye! Have a nice day 👋"
    }


    #Normalise input
    user_input = user_input.lower()

    answer = responses.get(user_input,"Sorry!, I dont know the answer to that.")

    #include context in answers
    return f"{context} {answer}"




def main():
    print("🤖 FAQ Bot is ready! (type 'bye' to exit)/n")

    while True:
        user = input("Enter your question: ")
        if user.lower() == "bye":
            print("bot:", chatbot_response(user))
            break
        print("Bot:",chatbot_response(user))



if __name__ == "__main__":
    main()        
