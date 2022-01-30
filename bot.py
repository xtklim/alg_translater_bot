import os
import telebot 
import re
import funcao


gta = os.environ["TOKEN"]

bot = telebot.TeleBot(gta) 



@bot.message_handler(commands=["inv"]) 
def inverso(mensagem):
    regex = r"(^(?:\/inv(?:@alg_translater_bot)?\s)(([RULDFBMEwS\s2]\'?)+))"
    #print(mensagem)
    test_str = str(mensagem.text)
    match = re.search(regex, test_str, re.MULTILINE)
    try:
        a = match.group(2)
        scramble = a
        b = funcao.inv(scramble)
        print(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s" %(b))
    except:
        bot.send_message(mensagem.chat.id, "Insira o algoritimo logo apos o /inv com um espaco")

@bot.message_handler(commands=["rot_x"]) 
def x(mensagem):
    regex = r"(^(?:\/rot_x(?:@alg_translater_bot)?\s)(([RULDFBMEwS\s2]\'?)+))"
    #print(mensagem)
    test_str = str(mensagem.text)
    match = re.search(regex, test_str, re.MULTILINE)
    try:
        a = match.group(2)
        scramble = a
        b = funcao.rotacao_x(scramble)
        print(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s" %(b))
    except:
        texto="""
        Por favor insira o comando corretamente.
    Exemplo /rot_x R U"""
        bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["rot_x2"]) 
def x2(mensagem):
    regex = r"(^(?:\/rot_x2(?:@alg_translater_bot)?\s)(([RULDFBMEwS\s2]\'?)+))"
    #print(mensagem)
    test_str = str(mensagem.text)
    match = re.search(regex, test_str, re.MULTILINE)
    try:
        a = match.group(2)
        scramble = a
        b = funcao.rotacao_x2(scramble)
        print(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s" %(b))
    except:
        texto="""
        Por favor insira o comando corretamente.
    Exemplo /rot_x2 R U"""
        bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["rot_y"]) 
def y(mensagem):
    regex = r"(^(?:\/rot_y(?:@alg_translater_bot)?\s)(([RULDFBMEwS\s2]\'?)+))"
    #print(mensagem)
    test_str = str(mensagem.text)
    match = re.search(regex, test_str, re.MULTILINE)
    try:
        a = match.group(2)
        scramble = a
        b = funcao.rotacao_y(scramble)
        print(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s" %(b))
    except:
        texto="""
        Por favor insira o comando corretamente.
    Exemplo /rot_y R U"""
        bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["rot_y2"]) 
def y2(mensagem):
    regex = r"(^(?:\/rot_y2(?:@alg_translater_bot)?\s)(([RULDFBMEwS\s2]\'?)+))"
    #print(mensagem)
    test_str = str(mensagem.text)
    match = re.search(regex, test_str, re.MULTILINE)
    try:
        a = match.group(2)
        scramble = a
        b = funcao.rotacao_y2(scramble)
        print(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s" %(b))
    except:
        texto="""
        Por favor insira o comando corretamente.
    Exemplo /rot_y2 R U"""
        bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["rot_z"]) 
def z(mensagem):
    regex = r"(^(?:\/rot_z(?:@alg_translater_bot)?\s)(([RULDFBMEwS\s2]\'?)+))"
    #print(mensagem)
    test_str = str(mensagem.text)
    match = re.search(regex, test_str, re.MULTILINE)
    try:
        a = match.group(2)
        scramble = a
        b = funcao.rotacao_z(scramble)
        print(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s" %(b))
    except:
        texto="""
        Por favor insira o comando corretamente.
    Exemplo /rot_z R U"""
        bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["rot_z2"]) 
def z2(mensagem):
    regex = r"(^(?:\/rot_z2(?:@alg_translater_bot)?\s)(([RULDFBMEwS\s2]\'?)+))"
    #print(mensagem)
    test_str = str(mensagem.text)
    match = re.search(regex, test_str, re.MULTILINE)
    try:
        a = match.group(2)
        scramble = a
        b = funcao.rotacao_z2(scramble)
        print(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s" %(b))
    except:
        texto="""
        Por favor insira o comando corretamente.
    Exemplo /rot_z2 R U"""
        bot.send_message(mensagem.chat.id, texto)


def verificar(mensagem): 
    return True 

@bot.message_handler(func=verificar) 
def responder(mensagem): 
    texto = """ Escolha uma opção para continuar (Clique e segure no item): 

/inv inverte um algoritimo
/rot_x rotacao no eixo x o algoritimo
/rot_x2 rotacao no eixo x 2 o algoritimo
/rot_y rotacao no eixo y o algoritimo
/rot_y2 rotacao no eixo y 2 vezes o algoritimo
/rot_z rotacao no eixo z o algoritimo
/rot_z2 rotacao no eixo z 2 vezes o algoritimo

exemplo de uso
/comando R U R' U'

Responder qualquer outra coisa não vai funcionar""" 
    #print(mensagem)
    bot.reply_to(mensagem, texto) 


bot.polling()
