#-*- coding: utf-8 -*-


import telebot
from telebot import types


bot = telebot.TeleBot( "TOKEN" )

@bot.message_handler( content_types=['text'] )
def texto(msg):
	texto = msg.text.upper()
	if texto == "DOAR" or texto == '1':
		bot.send_message( msg.chat.id , "Voce esolheu DOAR" )

	elif texto == "AJUDAR" or texto == "2":
		bot.send_message( msg.chat.id , "Voce escolheu AJUDAR" )

	elif texto == "SOBRE" or texto == "3":
		bot.send_message( msg.chat.id , "Somos HematoPy pra Doarladoawo ndabodb iawbdia0di" )



bot.polling()