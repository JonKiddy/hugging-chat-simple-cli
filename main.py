#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (Code From Article) HuggingChat Python API: Your No-Cost Alternative
# https://www.kdnuggets.com/2023/05/huggingchat-python-api-alternative.html

from hugchat import hugchat

# Create a chatbot connection
chatbot = hugchat.ChatBot()

# New a conversation (ignore error)
id = chatbot.new_conversation()
chatbot.change_conversation(id)

# Intro message
print('[[ Welcome to HugChat. Let\'s talk! ]]')
print('\'q\' or \'quit\' to exit')
print('\'c\' or \'change\' to change conversation')
print('\'n\' or \'new\' to start a new conversation')

while True:
	user_input = input('> ')
	if user_input.lower() == '':
		pass
	elif user_input.lower() in ['q', 'quit']:
		break
	elif user_input.lower() in ['c', 'change']:
		print('Choose a conversation to switch to:')
		print(chatbot.get_conversation_list())
	elif user_input.lower() in ['n', 'new']:
		print('Clean slate!')
		id = chatbot.new_conversation()
		chatbot.change_conversation(id)
	else:
		print(chatbot.chat(user_input))