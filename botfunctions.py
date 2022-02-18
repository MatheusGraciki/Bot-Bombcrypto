import pyautogui
import time



#loga na conta 1
def loginaccount1():
    time.sleep(3)
    # clicando na aba onde está a conta que deseja aplicar o bot
    pyautogui.click(36,417)
    time.sleep(3)
    pyautogui.hotkey('browserrefresh')
    time.sleep(5)
    #Clicando em conectar carteira
    pyautogui.click(x=540, y=524)
    time.sleep(5)
    #Clicando em assinar contrato na metamesk
    pyautogui.click(x=770, y=370)
    pyautogui.click(x=770, y=370)
    pyautogui.click(x=770, y=370)
#loga na conta 2
def loginaccount2():
    time.sleep(3)
    # clicando na aba onde está a conta que deseja aplicar o bot
    pyautogui.click(x=131, y=720)
    time.sleep(3)
    pyautogui.hotkey('browserrefresh')
    time.sleep(5)
    #Clicando em conectar carteira
    pyautogui.click(x=636, y=643)
    time.sleep(5)
    #Clicando em assinar contrato na metamesk
    pyautogui.click(x=883, y=655)
    pyautogui.click(x=883, y=655)
    pyautogui.click(x=883, y=655)
#loga na conta 3
def loginaccount3():
    time.sleep(3)
    # clicando na aba onde está a conta que deseja aplicar o bot
    pyautogui.click(x=215, y=889)
    time.sleep(3)
    pyautogui.hotkey('browserrefresh')
    time.sleep(5)
    #Clicando em conectar carteira
    pyautogui.click(x=713, y=797)
    time.sleep(5)
    #Clicando em assinar contrato na metamesk
    pyautogui.click(x=934, y=370)
    pyautogui.click(x=934, y=370)
    pyautogui.click(x=934, y=370)


# coloca os herois da conta 1 para trabalharem   
def puttingherotowork1():
    # clicando na aba onde está a conta que deseja aplicar o bot
    pyautogui.click(36,417)
    #clicando na aba de herois
    pyautogui.click(x=775, y=569)
    time.sleep(3)
    #colocando os herois para trabalharem
    pyautogui.click(x=497, y=357)
    time.sleep(3)
    #fechando aba dos herois
    pyautogui.click(x=578, y=319)
    pyautogui.click(x=578, y=319)
    pyautogui.click(x=578, y=319)
    time.sleep(5)
    #clicando no modo "TEASURE HUNT"
    pyautogui.click(x=553, y=423)
    pyautogui.click(x=553, y=423)
    pyautogui.click(x=553, y=423)
# coloca os  herois da conta 2 para trabalharem 
def puttingherotowork2():
    # clicando na aba onde está a conta que deseja aplicar o bot
    pyautogui.click(x=131, y=720)
    #clicando na aba de herois
    pyautogui.click(x=859, y=673)
    time.sleep(3)
    #colocando os herois para trabalharem
    pyautogui.click(x=580, y=469)
    pyautogui.click(x=580, y=469)
    time.sleep(3)
    #fechando aba dos herois
    pyautogui.click(x=661, y=438)
    pyautogui.click(x=661, y=438)
    pyautogui.click(x=661, y=438)
    time.sleep(5)
    #clicando no modo "TEASURE HUNT"
    pyautogui.click(x=626, y=552)
    pyautogui.click(x=626, y=552)
    pyautogui.click(x=626, y=552)
# coloca os herois da conta 3 para trabalharem 
def puttingherotowork3():
    # clicando na aba onde está a conta que deseja aplicar o bot
    pyautogui.click(x=215, y=889)
    #clicando na aba de herois
    pyautogui.click(x=932, y=827)
    time.sleep(3)
    #colocando os herois para trabalharem
    pyautogui.click(x=662, y=620)
    pyautogui.click(x=662, y=620)
    time.sleep(3)
    #fechando aba dos herois
    pyautogui.click(x=740, y=595)
    pyautogui.click(x=740, y=595)
    pyautogui.click(x=740, y=595)
    time.sleep(5)
    #clicando no modo "TEASURE HUNT"
    pyautogui.click(x=707, y=691)
    pyautogui.click(x=707, y=691)
    pyautogui.click(x=707, y=691)



#Entra no Teasure Hunt e volta para o menu na conta 1
def entryandgoout1():
    # clicando na aba onde está a conta que deseja aplicar o bot
    pyautogui.click(36,417)
    time.sleep(3)
    # votando para o menu principal para nao ser desconectado
    pyautogui.click(x=300, y=279)
    pyautogui.click(x=300, y=279)
    pyautogui.click(x=300, y=279)
    time.sleep(3)
    # clicando no modo "TEASURE HUNT"
    pyautogui.click(x=554, y=452)
    pyautogui.click(x=553, y=423)
#Entra no Teasure Hunt e volta para o menu na conta 2
def entryandgoout2():
    pyautogui.click(x=131, y=720)
    time.sleep(3)
    # votando para o menu principal para nao ser desconectado
    pyautogui.click(x=381, y=396)
    pyautogui.click(x=381, y=396)
    pyautogui.click(x=381, y=396)
    
    time.sleep(5)
    #clicando no modo "TEASURE HUNT"
    pyautogui.click(x=626, y=552)
    pyautogui.click(x=626, y=552)
    pyautogui.click(x=626, y=552)
#Entra no Teasure Hunt e volta para o menu na conta 3    
def entryandgoout3():
    pyautogui.click(x=215, y=889)
    # votando para o menu principal para nao ser desconectado
    pyautogui.click(x=464, y=545)
    pyautogui.click(x=464, y=545)
    pyautogui.click(x=464, y=545)
    time.sleep(3)
    time.sleep(5)
    #clicando no modo "TEASURE HUNT"
    pyautogui.click(x=707, y=691)
    pyautogui.click(x=707, y=691)
    pyautogui.click(x=707, y=691)