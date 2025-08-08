from typing import * 

import telebot 
from telebot import TeleBot

from TARGETS_OF_SENDING import TARGETS_OF_SENDING

def send(bot:TeleBot, string:str):
    
    try:
        target:int 
        for target in TARGETS_OF_SENDING:
            bot.send_message(chat_id=target, text=string)
    except telebot.apihelper.ApiTelegramException as er:
        print(f"there was an error sending report to {target}: {er}")


