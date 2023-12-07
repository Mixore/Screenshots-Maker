import pyautogui as bot
from sys import exit
N=1
while True:
    N1=bot.prompt(text="Choisissez le nombre de captures d'écran à réaliser :", title='Nombre de captures' , default='')
    try:
        if N1==None:
            N3=bot.confirm(text='Voulez vous quitter ?', title='Validation', buttons=['OK', 'Cancel'])
            if N3=='OK':
                exit(0)
            elif N3=='Cancel':
                continue
        elif int(N1)!=None:
            N2=bot.prompt(text="Choisissez l'intervalle entre chaque capture(en secondes, appuyez sur le bouton cancel pour un intervalle de 0.2 seconde) :", title='Intervalle' , default='')
            if N2==None:
                for i in range(int(N1)):
                    bot.screenshot("Screen"+str(N)+".png",)
                    N+=1
                N0=N-1
                N=1
                bot.alert(text="Les "+str(N0)+" captures ont bien été générées.", title='Tâche finie', button='OK')
            elif int(N2)!=None:
                for i in range(int(N1)):
                    bot.screenshot("Screen"+str(N)+".png")
                    bot.sleep(int(N2))
                    N+=1
                N0=N-1
                N=1
                bot.alert(text="Les "+str(N0)+" captures ont bien été générées.", title='Tâche finie', button='OK')
    except ValueError:
        bot.alert(text="Vous n'avez pas choisi une valeur correcte.", title='Valeur incorrecte', button='OK')
        continue
