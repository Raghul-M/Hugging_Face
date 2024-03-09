from transformers import pipeline,Conversation

chatbot = pipeline(model="facebook/blenderbot-400M-distill")
user_input=""

while True:
    conversation = []
    user_input = input("User : ")
    if user_input == "exit" or user_input == "":
        print("Thanks for using this Chatbot")
        break
    conversation.append(user_input)
    conversation = chatbot(conversation)
    print("Chatbot : ",conversation[0]['generated_text'])
    

