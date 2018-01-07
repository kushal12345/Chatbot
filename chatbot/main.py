from chatterbot.trainers import ListTrainer #method to train chatbot
from chatterbot import ChatBot #importing chatbot
print ('=========================================================================================')
bot = ChatBot('Test') #create chatbot
conv = open('files/chats.txt','r').readlines()
bot.set_trainer(ListTrainer) #set trainer
bot.train(conv)
print ('=========================================================================================')
print ('                  Welcome to chatbot. Your one and only personal assistance')
print(' ')
print('Enter your name:')
name = input()
print(' ')
print('Bot: Hello ' + name + ' Welcome to chatbot version 1.0')
print(' ')
while True:
	request = input(name + ':'  )
	response = bot.get_response(request)

	print ('Bot: ',  response)
