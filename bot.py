#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randint
import telepot

import config


class Bot:

    def __init__(self):
        self.bot = telepot.Bot(config.token)
        
    def run(self):
        self.bot.message_loop(self.handle, run_forever='Listening...')

    def handle(self, msg):
        c_type, chat_type, chat_id = telepot.glance(msg)
        if c_type != 'text':
            self.bot.sendMessage(chat_id, 'Excuse me, I understand only text')
            return
        decision = 0
        if ' или ' in msg['text'].lower():
            text = msg['text'].lower().replace('?', '')
            choices = text.split(' или ')
            if 'работать' in choices:
                self.bot.sendMessage(chat_id, 'Работать')
                return
            else:
                self.bot.sendMessage(chat_id, choices[randint(0, len(choices) - 1)].capitalize())
                return
        if decision == 0:
            self.bot.sendMessage(chat_id, msg['text'])
            return


if __name__ == '__main__':
    try:
        Bot().run()
    except KeyboardInterrupt:
        print('Shutting down...')
