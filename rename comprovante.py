# -*- coding: UTF-8 -*-
#importação de biblioteca de automatização
import pyautogui as pd
from tqdm.auto import tqdm
pd.PAUSE = 0.5
#biblioteca do teclado para encerrar execução do programa
import keyboard
#biblioteca do tempo durante a execução do programa
import time
pd.FAILSAFE = True

quantidade_comprovantes = input('Quantidade de comprovantes?  ')
#ALERTA PARA INICIO DO PROGRAMA
pd.alert('Organize sua tela, clique em ok para iniciar!')
#intervalo de tempo de uma ação para outra afim de evitar erros

#alterar quantidade no contador e no loop

for i in tqdm(range(int(quantidade_comprovantes))):
    pd.press("enter")
    pd.moveTo(2360, 852)
    pd.tripleClick()
    pd.hotkey('ctrl','c')
    pd.hotkey('alt','tab')
    pd.press('F2')
    pd.hotkey('ctrl','v')
    pd.press('enter')
    pd.press('s')
    pd.press('home')
    time.sleep(0.5)
    if keyboard.is_pressed('alt'):
        break
    else:
        True
    
pd.alert('Finalizado, pode usar seu computador!')








