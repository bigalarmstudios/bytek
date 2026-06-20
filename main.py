import os
import subprocess
import sys
import time
from colorama import Fore
# ASCII art
bytek = r"""
██████╗ ██╗   ██╗████████╗███████╗██╗  ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝██║ ██╔╝
██████╔╝ ╚████╔╝    ██║   █████╗  █████╔╝ 
██╔══██╗  ╚██╔╝     ██║   ██╔══╝  ██╔═██╗ 
██████╔╝   ██║      ██║   ███████╗██║  ██╗
╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝
"""
BreadInSchool = r"""
██████╗ ██████╗ ███████╗ █████╗ ██████╗     ██╗███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██║████╗  ██║
██████╔╝██████╔╝█████╗  ███████║██║  ██║    ██║██╔██╗ ██║
██╔══██╗██╔══██╗██╔══╝  ██╔══██║██║  ██║    ██║██║╚██╗██║
██████╔╝██║  ██║███████╗██║  ██║██████╔╝    ██║██║ ╚████║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝     ╚═╝╚═╝  ╚═══╝

███████╗ ██████╗██╗  ██╗ ██████╗  ██████╗ ██╗     
██╔════╝██╔════╝██║  ██║██╔═══██╗██╔═══██╗██║     
███████╗██║     ███████║██║   ██║██║   ██║██║     
╚════██║██║     ██╔══██║██║   ██║██║   ██║██║     
███████║╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████╗
╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝"""

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

files = [
    "text/help.txt",
    "text/help2.txt",
    "text/releaseBreadInSchool.txt",
    "text/howToGetTheGame.txt",
    "text/howToPlay.txt",
    "text/whySimpleWebsites.txt",
    "text/moreCommands.txt"
]

how_to_play = (
    "how to play",
    "how to play?",
    "how do i play",
    "how do i play?",
    "how do i start",
    "how do i start the game",
    "how do you play",
    "how to play the game",
    "how do i play the game",
    "what do i do in the game",
    "how does the game work",
    "can you explain how to play",
    "idk how to play",
    "i dont know how to play",
    "help me play",
    "game tutorial",
    "tutorial",
)

simple_websites = (
    "why do we have simple websites",
    "why do we have simple websites?",
    "why are the websites simple",
    "why are the websites so simple",
    "why is the website simple",
    "why do we use simple websites",
    "why do we have simple websites in school",
    "why are school websites simple",
    "why are websites simple in school",
    "what's the point of simple websites",
    "why not make better websites",
)

get_game = (
    "how to get the game",
    "how do i get the game",
    "where do i get the game",
    "where can i download the game",
    "how can i install the game",
    "how to install bread in school",
    "download link",
    "where is the download",
    "how do i download it",
    "can i download the game",
    "where can i play the game",
    "is the game out",
    "how to play bread in school",
)

release_date = (
    "release date for bread in school",
    "when is bread in school coming out",
    "when is bread in school releasing",
    "when does bread in school release",
    "when will bread in school release",
    "when is the game coming out",
    "when does the game come out",
    "release date",
    "is there a release date",
    "when can we play",
    "when will it be playable",
    "when is it launching",
)

more_commands = (
    "more commands",
    "more commands?",
    "show more commands",
    "what other commands are there",
    "what commands can i use",
    "list commands",
    "command list",
    "all commands",
    "help",
    "bot commands",
    "what can the bot do",
)

def spinner(duration=2):
    frames = ["|", "/", "-", "\\"]
    end = time.time() + duration
    i = 0

    while time.time() < end:
        sys.stdout.write("\rSystem: Retrieving information... " + frames[i % 4])
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

    print("\rSystem: Information retrieved successfully!   ")

def startCheck():
    print("checking for missing files...")
    time.sleep(1)

    if all(os.path.exists(f) for f in files):
        print("All files found, starting...")
        time.sleep(1)
    else:
        print("Missing files found, creating... do not close program.")
        subprocess.run([sys.executable, "createHelp.py"])
        print("Files created. Starting...")
        time.sleep(1)

def main():
    Question = input("User: ")
    if Question == "/help" or Question == "/Help" or Question == "/HELP":
        print(open("text/help.txt").read())
        print("[C] Continue / [R] Return")
        Question = input("User: ")
        if Question == "C" or Question == "c":
            print(open("text/help2.txt").read())
            print("[R] Return")
            Question = input("User: ")
            if Question == "R" or Question == "r":
                main()
            else:
                main()
        else:
            main()
    elif Question.lower() in release_date:
        print("-------------------------------------\n")
        spinner(3.2)
        print(open("text/releaseBreadInSchool.txt").read())
        print("-------------------------------------\n")
        main()
    elif Question.lower() in get_game:
        print("-------------------------------------\n")
        spinner(3.2)
        print(open("text/howToGetTheGame.txt").read())
        print("-------------------------------------\n")
        main()
    elif Question.lower() in how_to_play:
        print("-------------------------------------\n")
        spinner(3.2)
        print(open("text/howToPlay.txt").read())
        print("-------------------------------------\n")
        main()
    elif Question.lower() in simple_websites:
        print("-------------------------------------\n")
        spinner(5)
        print(open("text/whySimpleWebsites.txt").read())
        print("-------------------------------------\n")
        main()
    elif Question.lower() in more_commands:
        print("-------------------------------------\n")
        spinner(3.2)
        print(open("text/moreCommands.txt").read())
        print("-------------------------------------\n")
        main()
    else:
        print("-------------------------------------\n")
        spinner(4)
        print("Bytek: I'm sorry, I don't understand that command. Please try again or type '/help' for a list of commands.")
        print("-------------------------------------\n")
        main()

# Starts here
startCheck()
print(bytek)
print("Bytek: Hello! I am your helper for the game 'Bread In School' Q&A.")
print("System: for help type '/help'")
input("Press Enter to start...")
main()