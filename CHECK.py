from time import sleep
import os
import locale






fail = False

emoji = {
    True:  u'\u2705',
    False: u'\u274C',
    None:  u'\u2754',
        }

err = u'\u26A1'
tme = u'\u23F3'

check_msg_en = {'mcpi'          :" --- " +err+ "ERROR#01! mcpi not found! Please, open cmd and do: 'pip install mcpi'",
                'minecraftstuff':" --- " +err+ "ERROR#02! minecraftstuff not found! Please, open cmd and do: 'pip install minecraftstuff'",
                'server'        :" --- " +err+ "ERROR#03! Server not found! Please, start the SERVER",
                'plugin'        :" --- " +err+ "ERROR#04! There are no players on the server"}

check_msg_ru = {'mcpi'          :" --- " +err+ "ERROR#01! mcpi не установлен! Зайдите в терминал сmd и выполните команду: 'pip install mcpi'",
                'minecraftstuff':" --- " +err+ "ERROR#02! minecraftstuff не установлен! Зайдите в терминал сmd и выполните команду: 'pip install minecraftstuff'",
                'server'        :" --- " +err+ "ERROR#03! Не могу подключиться к серверу, запустите сервер, кликнув по ярлыку START в папке сервера",
                'plugin'        :" --- " +err+ "ERROR#04! Плагин не найден, свяжитесь с преподавателем для устрановки"}


if locale.getdefaultlocale()[0] == 'ru_RU':
    check_msg = check_msg_ru
else:
    check_msg = check_msg_en

checklist = {i: None for i in check_msg.keys()}


def print_check():
    checking = False
    stop = False
    #print(checklist)
    #sleep(3)
    for w in range(4):

        os.system('cls' if os.name == 'nt' else 'clear')

        for s in checklist.keys():

            print(emoji[checklist[s]] + ' - ' + s, end='')

            if checklist[s] == True:
                print(" --- "+ u'\u2728'*3+"OK", end='')
            elif checklist[s] == False:
                print(check_msg[s], end='')
                stop = True

            elif checklist[s] == None and not checking and not stop:
                print(" --- "+ tme*(3-w)+ "Checking" , end='')
                checking = True
            print()
        checking = False
        sleep(0.5)


def check_mcpi():
    global checklist
    try:
        import mcpi
        checklist['mcpi'] = True
    except ImportError:
        checklist['mcpi'] = False
    print_check()
    return checklist['mcpi']



def check_minecraftstuff():
    global checklist
    try:
        import minecraftstuff
        checklist['minecraftstuff'] = True
    except ImportError:
        checklist['minecraftstuff'] = False
    print_check()
    return checklist['minecraftstuff']

def check_server():
    global checklist
    try:
        Minecraft.create()
        checklist['server'] = True
    except:
        checklist['server'] = False
    print_check()
    return checklist['server']

def check_rj():
    global checklist
    try:
        mc.postToChat("Boo")
        checklist['plugin'] = True
    except:
        checklist['plugin'] = False
    print_check()
    return checklist['plugin']

if __name__ == "__main__":
    print_check()
    for a in range(1):

        if check_mcpi():
            from mcpi.minecraft import Minecraft
        else:
            break

        if not check_minecraftstuff():
            break
        if check_server():
            mc = Minecraft.create()
            check_rj()
    if False in checklist.values():
        print("Устраните ошибки и попробуйте ещё раз")
    else:
        print("Замечательно! Всё готово к работе!")




