# https://github.com/ClarigeClara/my-pyLibrary
# Importlist
import os
import sys
import subprocess

# Variables
Softwarename = "my-pyLibrary for LINUX by ClarigeClara (german)"
Version = "Version 1.0.0"
agree = ["y", "yes", "ya", "yee", "ye", "ja", "j"]
reject = ["n", "no", "nein", ""]
step1_package1 = "discord"
step1_package2 = "py-cord"
step3_package = "discord.ext-bot"
step4_package = "discord.ui"
step5_package = "discord-ext-forms"
step6_package = "topggpy"
step7_package = "asyncio"
step8_package = "python-dotenv"
step9_package = "colorama"

# Start
print(f'''{Softwarename}

{Version}
https://github.com/ClarigeClara/
-------------------------------------------------------------''')
input("Drücke ENTER, um fortzufahren...\n")


# STEP 1 | UNINSTALL discord und py-cord
os.system('clear')
print(f'''{Softwarename} | {Version}
SCHRITT 1      ■ □ □ □ □ □ □ □ □ □\n   --> Deinstallation von discord und py-cord\n\n
''')
step1 = input(f'(?) EINGABE ERFORDERLICH\nHast du die Bibliotheken "{step1_package1}" und "{step1_package2}" '
              'auf dem System und diese entfernen?\nDrücke ENTER für "nein" (Drücke "j", um fortzufahren):\n')
if step1 in agree:
    print(f'[i] INFORMATION\nDie Bibliotheken  "{step1_package1}" und "{step1_package2}" '
          'werden auf dem System entfernt.')
    input("Drücke ENTER, um fortzufahren...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', f'{step1_package1}', '-y'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', f'{step1_package2}', '-y'])
    print(f'[i] INFORMATION\nDie Bibliotheken "{step1_package1}" und {step1_package2} '
          'wurden vom System erfolgreich deinstalliert.')
    input("Drücke ENTER, um fortzufahren...\n")
if step1 in reject:
    print(f'[i] INFORMATION\nDie Bibliotheken "{step1_package1}" und "{step1_package2}" '
          'wurden vom System nicht entfernt.')
    input("Drücke ENTER, um fortzufahren...\n")


# STEP 2 | INSTALL discord and py-cord
os.system('clear')
print(f'''{Softwarename} | {Version}
SCHRITT 2      □ ■ □ □ □ □ □ □ □ □\n   --> Installation von {step1_package2}\n\n
''')
step2 = input(f'(?)EINGABE ERFORDERLICH\nMöchtest du die Bibliotheken "{step1_package2}" auf dem System installieren?'
              '\nDrücke ENTER für "nein" (Drücke "j", um fortzufahren):\n')
if step2 in agree:
    print(f'[i] INFORMATION\nDie Bibliothek "{step1_package2}" wird auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step1_package1}'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step1_package2}'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', f'{step1_package1}', '-y'])
    print(f'[i] INFORMATION\nDie Bibliothek "{step1_package2}" wurde erfolgreich auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
if step2 in reject:
    print(f'[i] INFORMATION\nDie Bibliothek "{step1_package2}" wird NICHT auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")


# STEP 3 | INSTALL discord.ext-bot
os.system('clear')
print(f'''{Softwarename} | {Version}
SCHRITT 3      □ □ ■ □ □ □ □ □ □ □\n   --> Installation von {step3_package}\n\n
''')
step3 = input(f'(?) EINGABE ERFORDERLICH\nMöchtest du die Bibliotheken "{step3_package}" auf dem System installieren?'
              '\nDrücke ENTER für "nein" (Drücke "j", um fortzufahren):\n')
if step3 in agree:
    print(f'[i] INFORMATION\nDie Bibliothek "{step3_package}" wird auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step3_package}'])
    print(f'[i] INFORMATION\nDie Bibliothek "{step3_package}" wurde erfolgreich auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
if step3 in reject:
    print(f'[i] INFORMATION\nDie Bibliothek "{step3_package}" auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")


# STEP 4 | INSTALL discord.ui
os.system('clear')
print(f'''{Softwarename} | {Version}
SCHRITT 4      □ □ □ ■ □ □ □ □ □ □\n   --> Installation von {step4_package}\n\n
''')
step4 = input(f'(?) EINGABE ERFORDERLICH\nMöchtest du die Bibliotheken "{step4_package}" auf dem System installieren?'
              '\nDrücke ENTER für "nein" (Drücke "j", um fortzufahren):\n')
if step4 in agree:
    print(f'[i] INFORMATION\nDie Bibliothek "{step4_package}" wird auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step4_package}'])
    print(f'[i] INFORMATION\nDie Bibliothek "{step4_package}" wurde erfolgreich auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
if step4 in reject:
    print(f'[i] INFORMATION\nDie Bibliothek "{step4_package}" auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")


# STEP 5 | INSTALL discord-ext-forms
os.system('clear')
print(f'''{Softwarename} | {Version}
SCHRITT 5      □ □ □ □ ■ □ □ □ □ □\n   --> Installation von {step5_package}\n\n
''')
step5 = input(f'(?) EINGABE ERFORDERLICH\nMöchtest du die Bibliotheken "{step5_package}" auf dem System installieren?'
              '\nDrücke ENTER für "nein" (Drücke "j", um fortzufahren):\n')
if step5 in agree:
    print(f'[i] INFORMATION\nDie Bibliothek "{step5_package}" wird auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step5_package}'])
    print(f'[i] INFORMATION\nDie Bibliothek "{step5_package}" wurde erfolgreich auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
if step5 in reject:
    print(f'[i] INFORMATION\nDie Bibliothek "{step5_package}" auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")


# STEP 6 | INSTALL topgg
os.system('clear')
print(f'''{Softwarename} | {Version}
SCHRITT 6      □ □ □ □ □ ■ □ □ □ □\n   --> Installation von {step6_package}\n\n
''')
step6 = input(f'(?) EINGABE ERFORDERLICH\nMöchtest du die Bibliotheken "{step6_package}" auf dem System installieren?'
              '\nDrücke ENTER für "nein" (Drücke "j", um fortzufahren):\n')
if step6 in agree:
    print(f'[i] INFORMATION\nDie Bibliothek "{step6_package}" wird auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step6_package}'])
    print(f'[i] INFORMATION\nDie Bibliothek "{step6_package}" wurde erfolgreich auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
if step6 in reject:
    print(f'[i] INFORMATION\nDie Bibliothek "{step6_package}" auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")


# STEP 7 | INSTALL asyncio
os.system('clear')
print(f'''{Softwarename} | {Version}
SCHRITT 7      □ □ □ □ □ □ ■ □ □ □\n   --> Installation von {step7_package}\n\n
''')
step7 = input(f'(?) EINGABE ERFORDERLICH\nMöchtest du die Bibliotheken "{step7_package}" auf dem System installieren?'
              '\nDrücke ENTER für "nein" (Drücke "j", um fortzufahren):\n')
if step7 in agree:
    print(f'[i] INFORMATION\nDie Bibliothek "{step7_package}" wird auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step7_package}'])
    print(f'[i] INFORMATION\nDie Bibliothek "{step7_package}" wurde erfolgreich auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
if step7 in reject:
    print(f'[i] INFORMATION\nDie Bibliothek "{step7_package}" auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")


# STEP 8 | INSTALL python-dotenv
os.system('clear')
print(f'''{Softwarename} | {Version}
SCHRITT 8      □ □ □ □ □ □ □ ■ □ □\n   --> Installation von {step8_package}\n\n
''')
step8 = input(f'(?) EINGABE ERFORDERLICH\nMöchtest du die Bibliotheken "{step8_package}" auf dem System installieren?'
              '\nDrücke ENTER für "nein" (Drücke "j", um fortzufahren):\n')
if step8 in agree:
    print(f'[i] INFORMATION\nDie Bibliothek "{step8_package}" wird auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step8_package}'])
    print(f'[i] INFORMATION\nDie Bibliothek "{step8_package}" wurde erfolgreich auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
if step8 in reject:
    print(f'[i] INFORMATION\nDie Bibliothek "{step8_package}" auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")

# STEP 9 | INSTALL python-dotenv
os.system('clear')
print(f'''{Softwarename} | {Version}
SCHRITT 9      □ □ □ □ □ □ □ □ ■ □\n   --> Installation von {step9_package}\n\n
''')
step9 = input(f'(?) EINGABE ERFORDERLICH\nMöchtest du die Bibliotheken "{step9_package}" auf dem System installieren?'
              '\nDrücke ENTER für "nein" (Drücke "j", um fortzufahren):\n')
if step9 in agree:
    print(f'[i] INFORMATION\nDie Bibliothek "{step9_package}" wird auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step9_package}'])
    print(f'[i] INFORMATION\nDie Bibliothek "{step9_package}" wurde erfolgreich auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")
if step9 in reject:
    print(f'[i] INFORMATION\nDie Bibliothek "{step9_package}" auf dem System installiert.')
    input("Drücke ENTER, um fortzufahren...\n")

# STEP 10 | ABGESCHLOSSEN
os.system('clear')
print(f'''{Softwarename} | {Version}
SCHRITT 10      □ □ □ □ □ □ □ □ □ ■\n

BEENDEN! 
Das Skript wurde erfolgreich ausgeführt und wird nun beendet.
Vielen Dank, dass du die Software benutzt hast.''')
