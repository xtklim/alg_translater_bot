import telebot, re, binascii, base64, os

gta = os.environ["TOKEN"]

bot = telebot.TeleBot(gta)

def gerador(texto):
    hex_texto = binascii.hexlify(texto).decode('utf-8')
    txtbyt = binascii.unhexlify(hex_texto)
    b64 = base64.b64encode(txtbyt)
    b64 = b64[::-1]
    b64 = bytes(b64).decode()
    return b64

@bot.message_handler(commands=["cfg"])
def resposta(msg):
	
	regex = r"(^(?:\/cfg\s)(.*))"
	test_str = str(msg.text)
	match = re.search(regex, test_str, re.MULTILINE)
	try:
	     a = match.group(2).encode('utf-8')
	     print('matcheado kkk')
	     b = gerador(a)
	     print(b)
	     bot.send_message(msg.chat.id, f"Ei {msg.from_user.first_name}\nFoi caralho")
	     bot.send_message(msg.chat.id, f"{b}")
	     bot.send_message(msg.chat.id, "Agradeco por usar esse simples bot")
	except:
	    bot.send_message(msg.chat.id, "Insira a sua cofiguracao pura editada logo apos o /cfg com um espaco")


def verificar(mensagem): 
    return True
    
@bot.message_handler(func=verificar) 
def responder(mensagem): 
    texto = "Me mande o texto da sua config\ncom a seguinte sintaxe /cfg texto\nResponder qualquer outra coisa não vai funcionar" 
    print(mensagem)
    bot.reply_to(mensagem, texto) 


bot.polling()
