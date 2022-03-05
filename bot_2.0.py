import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import re
import funcao

#A variavel gta vai guardar o seu token do bot
#Ou vc pode passar o seu token para variavel
gta = os.environ["TOKEN"]

bot = telebot.TeleBot(gta)



def alg_cubing(b):
    url = "https://alg.cubing.net/?type=alg&alg="
    
    c = url + b
    regex_1 = "\'"
    subst_1 = "-"
    test_str = c
    result_1 = re.sub(regex_1, subst_1, test_str, 0, re.MULTILINE)
    
    regex_2 = "\s"
    subst_2 = "_"
    test_str2 = result_1
    result_2 = re.sub(regex_2, subst_2, test_str2, 0, re.MULTILINE)
    
    regex_3 = "_$"
    subst_3 = ""
    test_str3 = result_2
    result_end = re.sub(regex_3, subst_3, test_str3, 0, re.MULTILINE)
    
    return result_end

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
        c = alg_cubing(b)
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(
        InlineKeyboardButton("Ver alg", c))
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s\nLink para o alg cubing" %(b), reply_markup=markup)
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
        c = alg_cubing(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s\nLink para o alg cubing : %s" %(b, c))
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
        c = alg_cubing(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s\nLink para o alg cubing : %s" %(b, c))
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
        c = alg_cubing(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s\nLink para o alg cubing : %s" %(b, c))
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
        c = alg_cubing(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s\nLink para o alg cubing : %s" %(b, c))
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
        c = alg_cubing(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s\nLink para o alg cubing : %s" %(b, c))
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
        c = alg_cubing(b)
        bot.send_message(mensagem.chat.id, "Novo algoritimo rsrs : %s\nLink para o alg cubing : %s" %(b, c))
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
