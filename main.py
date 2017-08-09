#!/usr/bin/python
# -*- coding: utf-8 -*-

#######
#
# Canal en Telegram: https://t.me/programacion
# Grupo en Telegram: https://t.me/joinchat/CR14KUNB0RrcXg53nTiIHw
#
#########

import time
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import pave_event_space, per_chat_id, create_open

"""
Despues de **insertar token** en el codigo fuente, ejecutelo:
```
$ python3 main.py
```
[Documetacion del Modulo Telepot](http://telepot.readthedocs.io/en/latest/)

Descripcion del Bot: Encargado de saludar a mienbros recien ingredos al Grupo, mandando un mensaje de bienvenida.

Comandos Soportados: 
- `/ayuda` - Ayuda

"""

# Clase definida para el Bot
class MessageWelcome(telepot.helper.ChatHandler):

    # Inicializador de la Clase
    def __init__(self, *args, **kwargs):
        super(MessageWelcome, self).__init__(*args, **kwargs)

    # Funcion definida para la interaccion
    def on_chat_message(self, msg):
	# Lenguaje del usuario
	lenguage = msg['chat']['lenguage_code']
        # ID de Chat
        chat_id = msg['chat']['id']
        # Variable vacia
        command = ''

        # Identificar el idioma del remitente o mensaje del usuario
        if 'es' in msg['from']['language_code']:
            print("Idioma Español")
        
        if 'en' in msg['from']['language_code']:
            print("Idioma Inglés")

        # Estas en un SuperGrupo
        if msg['chat']['type'] == 'supergroup':

            # Para la bienvenida en Supergrupo
            if 'new_chat_member' in msg and  'new_chat_members' in msg and 'new_chat_participant' in msg:
                bot.sendMessage(chat_id, "Bienvenido al grupo referente a Programación @" + msg['new_chat_member']['username'] +", esperamos ayudarte en tus dudas 😝")
                bot.sendMessage(chat_id, "Si deseas contenido referente a programación. Entra al Canal @programacion")
            
            #Para el que se fue del Supergrupo
            if 'left_chat_member' in msg and 'left_chat_participant' in msg:
                bot.sendMessage(chat_id, "Adios compañero @"+ msg['left_chat_member']['username'] +", te recordaremos 😢")
 
        # Estas en un Grupo
        elif msg['chat']['type'] == 'group':

            # Para la bienvenida en Grupo
            if 'new_chat_member' in msg and  'new_chat_members' in msg and 'new_chat_participant' in msg:
                bot.sendMessage(chat_id, "Bienvenido al grupo referente a Programación @" + msg['new_chat_member']['username'] +", esperamos ayudarte en tus dudas 😝")
                bot.sendMessage(chat_id, "Si deseas contenido referente a programación. Entra al Canal @programacion")
            
            #Para el que se fue del Grupo
            if 'left_chat_member' in msg and 'left_chat_participant' in msg:
                bot.sendMessage(chat_id, "Adios compañero @"+ msg['left_chat_member']['username'] +", te recordaremos 😢")


        # Estas en un Chat Privado
        elif msg['chat']['type'] == 'private':
            # Texto o Comando enviado por el usuario
            if 'text' in msg:
                command = msg['text']
            # Mensaje a mostrar cuando inicien el bot en privado
            if command == '/start':
                bot.sendMessage(chat_id, "Bienvenido a este Bot de uso para Grupos, No puedes usarlo para otros propositos 😝.")
            # Mostrar mensaje cuando soliciten  ayuda
            if command == '/ayuda':
                bot.sendMessage(chat_id, "Hola, Este bot solo es para uso de Grupo. Si deseas mas información, Mandar un mensaje al desarrollador @lu1tr0n 😝")

        # No reconozco el tipo de Chat que haces
        else:
            pass
        

# Este token debe ser el que se asigna por botFather
TOKEN = '** TOKEN **'   # TOKEN generado por botFather

# Instanciacion de telepot
bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MessageWelcome, timeout=10),
])
bot.setWebhook()  # unset webhook by supplying no parameter
# Bucle a la espera de mensajes
MessageLoop(bot).run_as_thread()
print("Esperando Mensajes")

# Bucle Infinito  
while 1:
    time.sleep(10)
