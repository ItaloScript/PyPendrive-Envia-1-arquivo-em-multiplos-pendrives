from shutil import copytree,copyfile
from ctypes import windll
from easygui import indexbox,fileopenbox,diropenbox
from os import path
from os import system
from time import sleep






print("Bem Vindo ao PyPendrive!!!\n\n")
print("Passo 1 -  RETIRE TODOS OS PENDRIVES")
print("Para o programa poder reconhecer os dispositivos")
print("que ja fazem parte do computador")
print("Então aperte enter")
input()
drivers = []
system("cls")
for  i in range(26):
    letra = chr(ord("A")+i)
    if path.exists(f"{letra}://"):
        drivers.append(letra)

selecionar = indexbox(msg=f"                              Selecione uma opção".upper(),title="PyPendrive",choices=("Copiar Arquivo","Copiar Pasta"))



if selecionar==None:
    quit()
elif selecionar==0:
    caminho = fileopenbox(msg="Selecione um arquivo")
else:
    caminho = diropenbox(msg="Selecione uma Pasta")

if(caminho==None):
    quit()
system("cls")
print("Ok, agora insira o pendrive e vamos começar")
count = 0


while True:
    sem_pendrive = True
    if(count==0):
        print("...................")
        print("Procurando Pendrive")
        count +=1
    while sem_pendrive:
        
        sleep(0.3)
        for i in range(len(drivers)):
                if path.exists(f"{drivers[i]}://"):
                    pass
                else:
                    drivers.pop(i)
        for  i in range(26):
            letra = chr(ord("A")+i)
            if path.exists(f"{letra}://") and letra not in drivers:
                sem_pendrive = False
                break


    print("Pendrive Encontrado passando arquivos")
    destino = f"{letra}:/arquivos_copiados"
    contador = 0

    while True:
        if not path.exists(destino):
            if path.isdir(caminho):
                copytree(caminho, destino)
            else:
                copyfile(caminho, f"{letra}:/{path.split(caminho)[1]}")
            break
        elif (path.exists(destino)):
            contador +=1
            destino = f"{letra}:/arquivos_copiados({contador})"
    count = 0           
    drivers.append(letra)
    print("Arquivos Copiados pode retirar")



