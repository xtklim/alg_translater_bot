#Funcoes de traducoes
#Importando movimentos
import movimentos
moves = movimentos.moves



#Definindo funcao que da o resultado
def res(my_r1):
    resultado = open("temp.txt", "w")
    for i in my_r1 :
        resultado.write("%s " %(i))
    resultado= open("temp.txt", "r")
    print("Novo scramble : %s "%(resultado.read()))
    resultado.close()
    resultado= open("temp.txt", "r")
    resposta = str(resultado.read())
    return resposta

#Definindo funccao inverse scramble
def inv(scramble):
    my_r1 = []
    scramble = scramble.split()
    for s in scramble:
        if s == moves[1]:
           my_r1 = my_r1 +[moves[2]]
        if s == moves[2]:
           my_r1 = my_r1 +[moves[1]]
        if s == moves[3]:
           my_r1 = my_r1 +[moves[4]]
        if s == moves[4]:
           my_r1 = my_r1 +[moves[3]]
        if s == moves[5]:
           my_r1 = my_r1 +[moves[6]]
        if s == moves[6]:
           my_r1 = my_r1 +[moves[5]]
        if s == moves[7]:
           my_r1 = my_r1 +[moves[8]]
        if s == moves[8]:
           my_r1 = my_r1 +[moves[7]]
        if s == moves[9]:
           my_r1 = my_r1 +[moves[10]]
        if s == moves[10]:
           my_r1 = my_r1 +[moves[9]]
        if s == moves[11]:
           my_r1 = my_r1 +[moves[12]]
        if s == moves[12]:
           my_r1 = my_r1 +[moves[11]]
        if s == moves[13]:
            my_r1 = my_r1 +[moves[13]]
        if s == moves[14]:
            my_r1 = my_r1 +[moves[14]]
        if s == moves[15]:
           my_r1 = my_r1 +[moves[15]]
        if s == moves[16]:
           my_r1 = my_r1 +[moves[16]]
        if s == moves[17]:
           my_r1 = my_r1 +[moves[17]]
        if s == moves[18]:
           my_r1 = my_r1 +[moves[18]]
        if s == moves[19]:
           my_r1 = my_r1 +[moves[20]]
        if s == moves[20]:
           my_r1 = my_r1 +[moves[19]]
        if s == moves[21]:
           my_r1 = my_r1 +[moves[22]]
        if s == moves[22]:
           my_r1 = my_r1 +[moves[21]]
        if s == moves[23]:
           my_r1 = my_r1 +[moves[24]]
        if s == moves[24]:
           my_r1 = my_r1 +[moves[23]]
        if s == moves[25]:
           my_r1 = my_r1 +[moves[26]]
        if s == moves[26]:
           my_r1 = my_r1 +[moves[25]]
        if s == moves[27]:
           my_r1 = my_r1 +[moves[28]]
        if s == moves[28]:
           my_r1 = my_r1 +[moves[27]]
        if s == moves[29]:
           my_r1 = my_r1 +[moves[30]]
        if s == moves[30]:
           my_r1 = my_r1 +[moves[29]]
        if s == moves[31]:
           my_r1 = my_r1 +[moves[31]]
        if s == moves[32]:
           my_r1 = my_r1 +[moves[32]]
        if s == moves[33]:
           my_r1 = my_r1 +[moves[33]]
        if s == moves[34]:
           my_r1 = my_r1 +[moves[34]]
        if s == moves[35]:
           my_r1 = my_r1 +[moves[35]]
        if s == moves[36]:
           my_r1 = my_r1 +[moves[36]]
        if s == moves[37]:
           my_r1 = my_r1 +[moves[38]]
        if s == moves[38]:
           my_r1 = my_r1 +[moves[37]]
        if s == moves[39]:
           my_r1 = my_r1 +[moves[39]]
        if s == moves[40]:
           my_r1 = my_r1 +[moves[41]]
        if s == moves[41]:
           my_r1 = my_r1 +[moves[40]]
        if s == moves[42]:
           my_r1 = my_r1 +[moves[42]]
        if s == moves[43]:
           my_r1 = my_r1 +[moves[44]]
        if s == moves[44]:
           my_r1 = my_r1 +[moves[43]]
        if s == moves[45]:
           my_r1 = my_r1 +[moves[45]]
    my_r1 = my_r1[::-1]
    #my_r1 = str(my_r1)
    resp = res(my_r1)
    return resp
      
#Definindo rotacao x
def rotacao_x(scramble):
    my_r1 = []
    scramble = scramble.split()
    for s in scramble:
        if s == moves[1]:
           my_r1 = my_r1 +[moves[1]]
        if s == moves[2]:
           my_r1 = my_r1 +[moves[2]]
        if s == moves[3]:
           my_r1 = my_r1 +[moves[11]]
        if s == moves[4]:
           my_r1 = my_r1 +[moves[12]]
        if s == moves[5]:
           my_r1 = my_r1 +[moves[5]]
        if s == moves[6]:
           my_r1 = my_r1 +[moves[6]]
        if s == moves[7]:
           my_r1 = my_r1 +[moves[9]]
        if s == moves[8]:
           my_r1 = my_r1 +[moves[10]]
        if s == moves[9]:
           my_r1 = my_r1 +[moves[3]]
        if s == moves[10]:
           my_r1 = my_r1 +[moves[4]]
        if s == moves[11]:
           my_r1 = my_r1 +[moves[7]]
        if s == moves[12]:
           my_r1 = my_r1 +[moves[8]]
        if s == moves[13]:
            my_r1 = my_r1 +[moves[13]]
        if s == moves[14]:
            my_r1 = my_r1 +[moves[18]]
        if s == moves[15]:
           my_r1 = my_r1 +[moves[15]]
        if s == moves[16]:
           my_r1 = my_r1 +[moves[17]]
        if s == moves[17]:
           my_r1 = my_r1 +[moves[14]]
        if s == moves[18]:
           my_r1 = my_r1 +[moves[16]]
        if s == moves[19]:
           my_r1 = my_r1 +[moves[19]]
        if s == moves[20]:
           my_r1 = my_r1 +[moves[20]]
        if s == moves[21]:
           my_r1 = my_r1 +[moves[21]]
        if s == moves[22]:
           my_r1 = my_r1 +[moves[22]]
        if s == moves[23]:
           my_r1 = my_r1 +[moves[29]]
        if s == moves[24]:
           my_r1 = my_r1 +[moves[30]]
        if s == moves[25]:
           my_r1 = my_r1 +[moves[27]]
        if s == moves[26]:
           my_r1 = my_r1 +[moves[28]]
        if s == moves[27]:
           my_r1 = my_r1 +[moves[23]]
        if s == moves[28]:
           my_r1 = my_r1 +[moves[24]]
        if s == moves[29]:
           my_r1 = my_r1 +[moves[25]]
        if s == moves[30]:
           my_r1 = my_r1 +[moves[26]]
        if s == moves[31]:
           my_r1 = my_r1 +[moves[31]]
        if s == moves[32]:
           my_r1 = my_r1 +[moves[32]]
        if s == moves[33]:
           my_r1 = my_r1 +[moves[36]]
        if s == moves[34]:
           my_r1 = my_r1 +[moves[35]]
        if s == moves[35]:
           my_r1 = my_r1 +[moves[33]]
        if s == moves[36]:
           my_r1 = my_r1 +[moves[34]]
        if s == moves[37]:
           my_r1 = my_r1 +[moves[43]]
        if s == moves[38]:
           my_r1 = my_r1 +[moves[44]]
        if s == moves[39]:
           my_r1 = my_r1 +[moves[45]]
        if s == moves[40]:
           my_r1 = my_r1 +[moves[40]]
        if s == moves[41]:
           my_r1 = my_r1 +[moves[41]]
        if s == moves[42]:
           my_r1 = my_r1 +[moves[42]]
        if s == moves[43]:
           my_r1 = my_r1 +[moves[38]]
        if s == moves[44]:
           my_r1 = my_r1 +[moves[37]]
        if s == moves[45]:
           my_r1 = my_r1 +[moves[39]]
    my_r1 = my_r1
    resp = res(my_r1)
    return resp

#definindo rotacao x2
def rotacao_x2(scramble):
    my_r1 = []
    scramble = scramble.split()
    for s in scramble:
        if s == moves[1]:
           my_r1 = my_r1 +[moves[1]]
        if s == moves[2]:
           my_r1 = my_r1 +[moves[2]]
        if s == moves[3]:
           my_r1 = my_r1 +[moves[7]]
        if s == moves[4]:
           my_r1 = my_r1 +[moves[8]]
        if s == moves[5]:
           my_r1 = my_r1 +[moves[5]]
        if s == moves[6]:
           my_r1 = my_r1 +[moves[6]]
        if s == moves[7]:
           my_r1 = my_r1 +[moves[3]]
        if s == moves[8]:
           my_r1 = my_r1 +[moves[4]]
        if s == moves[9]:
           my_r1 = my_r1 +[moves[11]]
        if s == moves[10]:
           my_r1 = my_r1 +[moves[12]]
        if s == moves[11]:
           my_r1 = my_r1 +[moves[9]]
        if s == moves[12]:
           my_r1 = my_r1 +[moves[10]]
        if s == moves[13]:
            my_r1 = my_r1 +[moves[13]]
        if s == moves[14]:
            my_r1 = my_r1 +[moves[16]]
        if s == moves[15]:
           my_r1 = my_r1 +[moves[15]]
        if s == moves[16]:
           my_r1 = my_r1 +[moves[14]]
        if s == moves[17]:
           my_r1 = my_r1 +[moves[18]]
        if s == moves[18]:
           my_r1 = my_r1 +[moves[17]]
        if s == moves[19]:
           my_r1 = my_r1 +[moves[19]]
        if s == moves[20]:
           my_r1 = my_r1 +[moves[20]]
        if s == moves[21]:
           my_r1 = my_r1 +[moves[21]]
        if s == moves[22]:
           my_r1 = my_r1 +[moves[22]]
        if s == moves[23]:
           my_r1 = my_r1 +[moves[25]]
        if s == moves[24]:
           my_r1 = my_r1 +[moves[26]]
        if s == moves[25]:
           my_r1 = my_r1 +[moves[23]]
        if s == moves[26]:
           my_r1 = my_r1 +[moves[24]]
        if s == moves[27]:
           my_r1 = my_r1 +[moves[29]]
        if s == moves[28]:
           my_r1 = my_r1 +[moves[30]]
        if s == moves[29]:
           my_r1 = my_r1 +[moves[27]]
        if s == moves[30]:
           my_r1 = my_r1 +[moves[28]]
        if s == moves[31]:
           my_r1 = my_r1 +[moves[31]]
        if s == moves[32]:
           my_r1 = my_r1 +[moves[32]]
        if s == moves[33]:
           my_r1 = my_r1 +[moves[34]]
        if s == moves[34]:
           my_r1 = my_r1 +[moves[33]]
        if s == moves[35]:
           my_r1 = my_r1 +[moves[36]]
        if s == moves[36]:
           my_r1 = my_r1 +[moves[35]]
        if s == moves[37]:
           my_r1 = my_r1 +[moves[38]]
        if s == moves[38]:
           my_r1 = my_r1 +[moves[37]]
        if s == moves[39]:
           my_r1 = my_r1 +[moves[39]]
        if s == moves[40]:
           my_r1 = my_r1 +[moves[40]]
        if s == moves[41]:
           my_r1 = my_r1 +[moves[41]]
        if s == moves[42]:
           my_r1 = my_r1 +[moves[42]]
        if s == moves[43]:
           my_r1 = my_r1 +[moves[44]]
        if s == moves[44]:
           my_r1 = my_r1 +[moves[43]]
        if s == moves[45]:
           my_r1 = my_r1 +[moves[45]]
    my_r1 = my_r1
    resp = res(my_r1)
    return resp

#definindo rotacao y
def rotacao_y(scramble):
    my_r1 = []
    scramble = scramble.split()
    for s in scramble:
        if s == moves[1]:
            my_r1 = my_r1 +[moves[9]]
        if s == moves[2]:
            my_r1 = my_r1 +[moves[10]]
        if s == moves[3]:
            my_r1 = my_r1 +[moves[3]]
        if s == moves[4]:
            my_r1 = my_r1 +[moves[4]]
        if s == moves[5]:
            my_r1 = my_r1 +[moves[11]]
        if s == moves[6]:
            my_r1 = my_r1 +[moves[12]]
        if s == moves[7]:
            my_r1 = my_r1 +[moves[7]]
        if s == moves[8]:
            my_r1 = my_r1 +[moves[8]]
        if s == moves[9]:
            my_r1 = my_r1 +[moves[5]]
        if s == moves[10]:
            my_r1 = my_r1 +[moves[6]]
        if s == moves[11]:
            my_r1 = my_r1 +[moves[1]]
        if s == moves[12]:
            my_r1 = my_r1 +[moves[2]]
        if s == moves[13]:
            my_r1 = my_r1 +[moves[17]]
        if s == moves[14]:
            my_r1 = my_r1 +[moves[14]]
        if s == moves[15]:
            my_r1 = my_r1 +[moves[18]]
        if s == moves[16]:
            my_r1 = my_r1 +[moves[16]]
        if s == moves[17]:
            my_r1 = my_r1 +[moves[15]]
        if s == moves[18]:
            my_r1 = my_r1 +[moves[13]]
        if s == moves[19]:
           my_r1 = my_r1 +[moves[27]]
        if s == moves[20]:
           my_r1 = my_r1 +[moves[28]]
        if s == moves[21]:
           my_r1 = my_r1 +[moves[29]]
        if s == moves[22]:
           my_r1 = my_r1 +[moves[30]]
        if s == moves[23]:
           my_r1 = my_r1 +[moves[23]]
        if s == moves[24]:
           my_r1 = my_r1 +[moves[24]]
        if s == moves[25]:
           my_r1 = my_r1 +[moves[25]]
        if s == moves[26]:
           my_r1 = my_r1 +[moves[26]]
        if s == moves[27]:
           my_r1 = my_r1 +[moves[21]]
        if s == moves[28]:
           my_r1 = my_r1 +[moves[22]]
        if s == moves[29]:
           my_r1 = my_r1 +[moves[19]]
        if s == moves[30]:
           my_r1 = my_r1 +[moves[20]]
        if s == moves[31]:
           my_r1 = my_r1 +[moves[35]]
        if s == moves[32]:
           my_r1 = my_r1 +[moves[36]]
        if s == moves[33]:
           my_r1 = my_r1 +[moves[33]]
        if s == moves[34]:
           my_r1 = my_r1 +[moves[34]]
        if s == moves[35]:
           my_r1 = my_r1 +[moves[32]]
        if s == moves[36]:
           my_r1 = my_r1 +[moves[31]]
        if s == moves[37]:
           my_r1 = my_r1 +[moves[40]]
        if s == moves[38]:
           my_r1 = my_r1 +[moves[41]]
        if s == moves[39]:
           my_r1 = my_r1 +[moves[42]]
        if s == moves[40]:
           my_r1 = my_r1 +[moves[37]]
        if s == moves[41]:
           my_r1 = my_r1 +[moves[38]]
        if s == moves[42]:
           my_r1 = my_r1 +[moves[39]]
        if s == moves[43]:
           my_r1 = my_r1 +[moves[43]]
        if s == moves[44]:
           my_r1 = my_r1 +[moves[44]]
        if s == moves[45]:
           my_r1 = my_r1 +[moves[45]]
    my_r1 = my_r1
    resp = res(my_r1)
    return resp

#definindo rotacao y2
def rotacao_y2(scramble):
    my_r1 = []
    scramble = scramble.split()
    for s in scramble:
        if s == moves[1]:
            my_r1 = my_r1 +[moves[5]]
        if s == moves[2]:
            my_r1 = my_r1 +[moves[6]]
        if s == moves[3]:
            my_r1 = my_r1 +[moves[3]]
        if s == moves[4]:
            my_r1 = my_r1 +[moves[4]]
        if s == moves[5]:
            my_r1 = my_r1 +[moves[1]]
        if s == moves[6]:
            my_r1 = my_r1 +[moves[2]]
        if s == moves[7]:
            my_r1 = my_r1 +[moves[7]]
        if s == moves[8]:
            my_r1 = my_r1 +[moves[8]]
        if s == moves[9]:
            my_r1 = my_r1 +[moves[11]]
        if s == moves[10]:
            my_r1 = my_r1 +[moves[12]]
        if s == moves[11]:
            my_r1 = my_r1 +[moves[9]]
        if s == moves[12]:
            my_r1 = my_r1 +[moves[10]]
        if s == moves[13]:
            my_r1 = my_r1 +[moves[15]]
        if s == moves[14]:
            my_r1 = my_r1 +[moves[14]]
        if s == moves[15]:
            my_r1 = my_r1 +[moves[13]]
        if s == moves[16]:
            my_r1 = my_r1 +[moves[16]]
        if s == moves[17]:
            my_r1 = my_r1 +[moves[18]]
        if s == moves[18]:
            my_r1 = my_r1 +[moves[17]]
        if s == moves[19]:
           my_r1 = my_r1 +[moves[21]]
        if s == moves[20]:
           my_r1 = my_r1 +[moves[22]]
        if s == moves[21]:
           my_r1 = my_r1 +[moves[19]]
        if s == moves[22]:
           my_r1 = my_r1 +[moves[20]]
        if s == moves[23]:
           my_r1 = my_r1 +[moves[23]]
        if s == moves[24]:
           my_r1 = my_r1 +[moves[24]]
        if s == moves[25]:
           my_r1 = my_r1 +[moves[25]]
        if s == moves[26]:
           my_r1 = my_r1 +[moves[26]]
        if s == moves[27]:
           my_r1 = my_r1 +[moves[29]]
        if s == moves[28]:
           my_r1 = my_r1 +[moves[30]]
        if s == moves[29]:
           my_r1 = my_r1 +[moves[27]]
        if s == moves[30]:
           my_r1 = my_r1 +[moves[28]]
        if s == moves[31]:
           my_r1 = my_r1 +[moves[32]]
        if s == moves[32]:
           my_r1 = my_r1 +[moves[31]]
        if s == moves[33]:
           my_r1 = my_r1 +[moves[33]]
        if s == moves[34]:
           my_r1 = my_r1 +[moves[34]]
        if s == moves[35]:
           my_r1 = my_r1 +[moves[36]]
        if s == moves[36]:
           my_r1 = my_r1 +[moves[35]]
        if s == moves[37]:
           my_r1 = my_r1 +[moves[38]]
        if s == moves[38]:
           my_r1 = my_r1 +[moves[37]]
        if s == moves[39]:
           my_r1 = my_r1 +[moves[39]]
        if s == moves[40]:
           my_r1 = my_r1 +[moves[41]]
        if s == moves[41]:
           my_r1 = my_r1 +[moves[40]]
        if s == moves[42]:
           my_r1 = my_r1 +[moves[42]]
        if s == moves[43]:
           my_r1 = my_r1 +[moves[43]]
        if s == moves[44]:
           my_r1 = my_r1 +[moves[44]]
        if s == moves[45]:
           my_r1 = my_r1 +[moves[45]]
    my_r1 = my_r1
    resp = res(my_r1)
    return resp

#definindo rotacao z
def rotacao_z(scramble):
    my_r1 = []
    scramble = scramble.split()
    for s in scramble:
        if s == moves[1]:
            my_r1 = my_r1 +[moves[7]]
        if s == moves[2]:
            my_r1 = my_r1 +[moves[8]]
        if s == moves[3]:
            my_r1 = my_r1 +[moves[1]]
        if s == moves[4]:
            my_r1 = my_r1 +[moves[2]]
        if s == moves[5]:
            my_r1 = my_r1 +[moves[3]]
        if s == moves[6]:
            my_r1 = my_r1 +[moves[4]]
        if s == moves[7]:
            my_r1 = my_r1 +[moves[5]]
        if s == moves[8]:
            my_r1 = my_r1 +[moves[6]]
        if s == moves[9]:
            my_r1 = my_r1 +[moves[9]]
        if s == moves[10]:
            my_r1 = my_r1 +[moves[10]]
        if s == moves[11]:
            my_r1 = my_r1 +[moves[11]]
        if s == moves[12]:
            my_r1 = my_r1 +[moves[12]]
        if s == moves[13]:
            my_r1 = my_r1 +[moves[16]]
        if s == moves[14]:
            my_r1 = my_r1 +[moves[13]]
        if s == moves[15]:
            my_r1 = my_r1 +[moves[14]]
        if s == moves[16]:
            my_r1 = my_r1 +[moves[15]]
        if s == moves[17]:
            my_r1 = my_r1 +[moves[17]]
        if s == moves[18]:
            my_r1 = my_r1 +[moves[18]]
        if s == moves[19]:
           my_r1 = my_r1 +[moves[25]]
        if s == moves[20]:
           my_r1 = my_r1 +[moves[26]]
        if s == moves[21]:
           my_r1 = my_r1 +[moves[23]]
        if s == moves[22]:
           my_r1 = my_r1 +[moves[24]]
        if s == moves[23]:
           my_r1 = my_r1 +[moves[19]]
        if s == moves[24]:
           my_r1 = my_r1 +[moves[20]]
        if s == moves[25]:
           my_r1 = my_r1 +[moves[21]]
        if s == moves[26]:
           my_r1 = my_r1 +[moves[22]]
        if s == moves[27]:
           my_r1 = my_r1 +[moves[27]]
        if s == moves[28]:
           my_r1 = my_r1 +[moves[28]]
        if s == moves[29]:
           my_r1 = my_r1 +[moves[29]]
        if s == moves[30]:
           my_r1 = my_r1 +[moves[30]]
        if s == moves[31]:
           my_r1 = my_r1 +[moves[34]]
        if s == moves[32]:
           my_r1 = my_r1 +[moves[33]]
        if s == moves[33]:
           my_r1 = my_r1 +[moves[31]]
        if s == moves[34]:
           my_r1 = my_r1 +[moves[32]]
        if s == moves[35]:
           my_r1 = my_r1 +[moves[35]]
        if s == moves[36]:
           my_r1 = my_r1 +[moves[36]]
        if s == moves[37]:
           my_r1 = my_r1 +[moves[37]]
        if s == moves[38]:
           my_r1 = my_r1 +[moves[38]]
        if s == moves[39]:
           my_r1 = my_r1 +[moves[39]]
        if s == moves[40]:
           my_r1 = my_r1 +[moves[43]]
        if s == moves[41]:
           my_r1 = my_r1 +[moves[44]]
        if s == moves[42]:
           my_r1 = my_r1 +[moves[45]]
        if s == moves[43]:
           my_r1 = my_r1 +[moves[41]]
        if s == moves[44]:
           my_r1 = my_r1 +[moves[40]]
        if s == moves[45]:
           my_r1 = my_r1 +[moves[42]]
    my_r1 = my_r1
    resp = res(my_r1)
    return resp

#Definido rotacao z2
def rotacao_z2(scramble):
    my_r1 = []
    scramble = scramble.split()
    for s in scramble:
        if s == moves[1]:
            my_r1 = my_r1 +[moves[5]]
        if s == moves[2]:
            my_r1 = my_r1 +[moves[6]]
        if s == moves[3]:
            my_r1 = my_r1 +[moves[7]]
        if s == moves[4]:
            my_r1 = my_r1 +[moves[8]]
        if s == moves[5]:
            my_r1 = my_r1 +[moves[1]]
        if s == moves[6]:
            my_r1 = my_r1 +[moves[2]]
        if s == moves[7]:
            my_r1 = my_r1 +[moves[3]]
        if s == moves[8]:
            my_r1 = my_r1 +[moves[4]]
        if s == moves[9]:
            my_r1 = my_r1 +[moves[9]]
        if s == moves[10]:
            my_r1 = my_r1 +[moves[10]]
        if s == moves[11]:
            my_r1 = my_r1 +[moves[11]]
        if s == moves[12]:
            my_r1 = my_r1 +[moves[12]]
        if s == moves[13]:
            my_r1 = my_r1 +[moves[15]]
        if s == moves[14]:
            my_r1 = my_r1 +[moves[16]]
        if s == moves[15]:
            my_r1 = my_r1 +[moves[13]]
        if s == moves[16]:
            my_r1 = my_r1 +[moves[14]]
        if s == moves[17]:
            my_r1 = my_r1 +[moves[17]]
        if s == moves[18]:
            my_r1 = my_r1 +[moves[18]]
        if s == moves[19]:
           my_r1 = my_r1 +[moves[21]]
        if s == moves[20]:
           my_r1 = my_r1 +[moves[22]]
        if s == moves[21]:
           my_r1 = my_r1 +[moves[19]]
        if s == moves[22]:
           my_r1 = my_r1 +[moves[20]]
        if s == moves[23]:
           my_r1 = my_r1 +[moves[25]]
        if s == moves[24]:
           my_r1 = my_r1 +[moves[26]]
        if s == moves[25]:
           my_r1 = my_r1 +[moves[23]]
        if s == moves[26]:
           my_r1 = my_r1 +[moves[24]]
        if s == moves[27]:
           my_r1 = my_r1 +[moves[27]]
        if s == moves[28]:
           my_r1 = my_r1 +[moves[28]]
        if s == moves[29]:
           my_r1 = my_r1 +[moves[29]]
        if s == moves[30]:
           my_r1 = my_r1 +[moves[30]]
        if s == moves[31]:
           my_r1 = my_r1 +[moves[32]]
        if s == moves[32]:
           my_r1 = my_r1 +[moves[31]]
        if s == moves[33]:
           my_r1 = my_r1 +[moves[34]]
        if s == moves[34]:
           my_r1 = my_r1 +[moves[33]]
        if s == moves[35]:
           my_r1 = my_r1 +[moves[35]]
        if s == moves[36]:
           my_r1 = my_r1 +[moves[36]]
        if s == moves[37]:
           my_r1 = my_r1 +[moves[37]]
        if s == moves[38]:
           my_r1 = my_r1 +[moves[38]]
        if s == moves[39]:
           my_r1 = my_r1 +[moves[39]]
        if s == moves[40]:
           my_r1 = my_r1 +[moves[41]]
        if s == moves[41]:
           my_r1 = my_r1 +[moves[40]]
        if s == moves[42]:
           my_r1 = my_r1 +[moves[42]]
        if s == moves[43]:
           my_r1 = my_r1 +[moves[43]]
        if s == moves[44]:
           my_r1 = my_r1 +[moves[44]]
        if s == moves[45]:
           my_r1 = my_r1 +[moves[45]]
    my_r1 = my_r1
    resp = res(my_r1)
    return resp