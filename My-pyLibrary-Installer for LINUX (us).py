# https://github.com/ClarigeClara/my-pyLibrary
# Importlist
import os
import sys
import subprocess

# Variables
Softwarename = "my-pyLibrary-Installer for LINUX by ClarigeClara"
Version = "Version 1.0.1"
agree = ["y", "yes", "ya", "yee", "ye"]
reject = ["n", "no", ""]
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
input("Press ENTER to continue...\n")


# STEP 1 | UNINSTALL discord and py-cord
os.system('clear')
print(f'''{Softwarename} | {Version}
STEP 1      ■ □ □ □ □ □ □ □ □ □\n   --> UNINSTALL discord and py-cord\n\n
''')
step1 = input(f'(?) INPUT REQUIRED\nDo you have the libraries "{step1_package1}" and "{step1_package2}" '
              'on this system and want them removed?\nBlank to select "no"  (Enter "y" to continue):\n')
if step1 in agree:
    print(f'[i] INFORMATION\nThe Library "{step1_package1}" and "{step1_package2}" are removed from this system.')
    input("Press ENTER to continue...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', f'{step1_package1}', '-y'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', f'{step1_package2}', '-y'])
    print(f'[i] INFORMATION\nThe Library "{step1_package1}" and {step1_package2} '
          'have been successfully removed from this system.')
    input("Press ENTER to continue...\n")
if step1 in reject:
    print(f'[i] INFORMATION\nThe Library "{step1_package1}" and "{step1_package2}" are NOT removed from this system.')
    input("Press ENTER to continue...\n")


# STEP 2 | INSTALL discord and py-cord
os.system('clear')
print(f'''{Softwarename} | {Version}
STEP 2      □ ■ □ □ □ □ □ □ □ □\n   --> INSTALL {step1_package2}\n\n
''')
step2 = input(f'(?) INPUT REQUIRED\nDo you want install the libraries "{step1_package2}" on the system?'
              '\nBlank to select "no"  (Enter "y" to continue):\n')
if step2 in agree:
    print(f'[i] INFORMATION\nThe Library "{step1_package2}" are installing on this system.')
    input("Press ENTER to continue...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step1_package1}'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step1_package2}'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', f'{step1_package1}', '-y'])
    print(f'[i] INFORMATION\nThe Library "{step1_package2}" are installed on this system.')
    input("Press ENTER to continue...\n")
if step2 in reject:
    print(f'[i] INFORMATION\nThe Library "{step1_package2}" are NOT installing on this system.')
    input("Press ENTER to continue...\n")


# STEP 3 | INSTALL discord.ext-bot
os.system('clear')
print(f'''{Softwarename} | {Version}
STEP 3      □ □ ■ □ □ □ □ □ □ □\n   --> INSTALL {step3_package}\n\n
''')
step3 = input(f'(?) INPUT REQUIRED\nDo you want install the libraries ""{step3_package}" on the system?'
              '\nBlank to select "no"  (Enter "y" to continue):\n')
if step3 in agree:
    print(f'[i] INFORMATION\nThe Library "{step3_package}" are installing on this system.')
    input("Press ENTER to continue...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step3_package}'])
    print(f'[i] INFORMATION\nThe Library "{step3_package}" are installed on this system.')
    input("Press ENTER to continue...\n")
if step3 in reject:
    print(f'[i] INFORMATION\nThe Library "{step3_package}" are NOT installing on this system.')
    input("Press ENTER to continue...\n")


# STEP 4 | INSTALL discord.ui
os.system('clear')
print(f'''{Softwarename} | {Version}
STEP 4      □ □ □ ■ □ □ □ □ □ □\n   --> INSTALL {step4_package}\n\n
''')
step4 = input(f'(?) INPUT REQUIRED\nDo you want install the libraries "{step4_package}" on the system?'
              '\nBlank to select "no"  (Enter "y" to continue):\n')
if step4 in agree:
    print(f'[i] INFORMATION\nThe Library "{step4_package}" are installing on this system.')
    input("Press ENTER to continue...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step4_package}'])
    print(f'[i] INFORMATION\nThe Library "{step4_package}" are installed on this system.')
    input("Press ENTER to continue...\n")
if step4 in reject:
    print(f'[i] INFORMATION\nThe Library "{step4_package}" are NOT installing on this system.')
    input("Press ENTER to continue...\n")


# STEP 5 | INSTALL discord-ext-forms
os.system('clear')
print(f'''{Softwarename} | {Version}
STEP 5      □ □ □ □ ■ □ □ □ □ □\n   --> INSTALL {step5_package}\n\n
''')
step5 = input(f'(?) INPUT REQUIRED\nDo you want install the libraries "{step5_package}" on the system?'
              '\nBlank to select "no"  (Enter "y" to continue):\n')
if step5 in agree:
    print(f'[i] INFORMATION\nThe Library "{step5_package}" are installing on this system.')
    input("Press ENTER to continue...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step5_package}'])
    print(f'[i] INFORMATION\nThe Library "{step5_package}" are installed on this system.')
    input("Press ENTER to continue...\n")
if step5 in reject:
    print(f'[i] INFORMATION\nThe Library "{step5_package}" are NOT installing on this system.')
    input("Press ENTER to continue...\n")


# STEP 6 | INSTALL topgg
os.system('clear')
print(f'''{Softwarename} | {Version}
STEP 6      □ □ □ □ □ ■ □ □ □ □\n   --> INSTALL {step6_package}\n\n
''')
step6 = input(f'(?) INPUT REQUIRED\nDo you want install the libraries "{step6_package}" on the system?'
              '\nBlank to select "no"  (Enter "y" to continue):\n')
if step6 in agree:
    print(f'[i] INFORMATION\nThe Library "{step6_package}" are installing on this system.')
    input("Press ENTER to continue...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step6_package}'])
    print(f'[i] INFORMATION\nThe Library "{step6_package}" are installed on this system.')
    input("Press ENTER to continue...\n")
if step6 in reject:
    print(f'[i] INFORMATION\nThe Library "{step6_package}" are NOT installing on this system.')
    input("Press ENTER to continue...\n")


# STEP 7 | INSTALL asyncio
os.system('clear')
print(f'''{Softwarename} | {Version}
STEP 7      □ □ □ □ □ □ ■ □ □ □\n   --> INSTALL {step7_package}\n\n
''')
step7 = input(f'(?) INPUT REQUIRED\nDo you want install the libraries "{step7_package}" on the system?'
              '\nBlank to select "no"  (Enter "y" to continue):\n')
if step7 in agree:
    print(f'[i] INFORMATION\nThe Library "{step7_package}" are installing on this system.')
    input("Press ENTER to continue...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step7_package}'])
    print(f'[i] INFORMATION\nThe Library "{step7_package}" are installed on this system.')
    input("Press ENTER to continue...\n")
if step7 in reject:
    print(f'[i] INFORMATION\nThe Library "{step7_package}" are NOT installing on this system.')
    input("Press ENTER to continue...\n")


# STEP 8 | INSTALL python-dotenv
os.system('clear')
print(f'''{Softwarename} | {Version}
STEP 8      □ □ □ □ □ □ □ ■ □ □\n   --> INSTALL {step8_package}\n\n
''')
step8 = input(f'(?) INPUT REQUIRED\nDo you want install the libraries "{step8_package}" on the system?'
              '\nBlank to select "no"  (Enter "y" to continue):\n')
if step8 in agree:
    print(f'[i] INFORMATION\nThe Library "{step8_package}" are installing on this system.')
    input("Press ENTER to continue...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step8_package}'])
    print(f'[i] INFORMATION\nThe Library "{step8_package}" are installed on this system.')
    input("Press ENTER to continue...\n")
if step8 in reject:
    print(f'[i] INFORMATION\nThe Library "{step8_package}" are NOT installing on this system.')
    input("Press ENTER to continue...\n")


# STEP 9 | INSTALL python-dotenv
os.system('clear')
print(f'''{Softwarename} | {Version}
STEP 9      □ □ □ □ □ □ □ □ ■ □\n   --> INSTALL {step9_package}\n\n
''')
step9 = input(f'(?) INPUT REQUIRED\nDo you want install the libraries "{step9_package}" on the system?'
              '\nBlank to select "no"  (Enter "y" to continue):\n')
if step9 in agree:
    print(f'[i] INFORMATION\nThe Library "{step9_package}" are installing on this system.')
    input("Press ENTER to continue...\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{step9_package}'])
    print(f'[i] INFORMATION\nThe Library "{step9_package}" are installed on this system.')
    input("Press ENTER to continue...\n")
if step9 in reject:
    print(f'[i] INFORMATION\nThe Library "{step9_package}" are NOT installing on this system.')
    input("Press ENTER to continue...\n")

# STEP 10 | COMPLETE
os.system('clear')
print(f'''{Softwarename} | {Version}
STEP 10      □ □ □ □ □ □ □ □ □ ■\n

FINISH! 
The script was successfully executed and will now be terminated.
Thank you very much for using the software.''')
