from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('D:/repository/ChatBot/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data  = open('D:/repository/ChatBot/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readline()
    bot.train(data)

while True:
    message  = input("You: ")
    if message.strip()!= 'Bye':
        reply = bot.get_response(message)    
        print("ChatBot: ",reply)
    if message.strip() == 'Bye':
        print("ChatBot:Bye")
        break