import json
import os 
from pathlib import Path
from follow_back import follow_back_new
from unfollow_nonfollowers import unfollow_nonfollowers
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

CONFIG_FILE = Path("config.json")

def print_banner():
    banner = r"""
                       .,,uod8B8bou,,.                             
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.                    
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||                   
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||                   
         !.......:!?|||||!!^^""'            ||||                   
         !.........||||                     ||||                   
         !.........||||  ##                 ||||                   
         !.........||||                     ||||                   
         !.........||||                     ||||                   
         !.........||||                     ||||                   
         !.........||||                     ||||                   
         `.........||||                    ,||||                   
          .;.......||||               _.-!!|||||                   
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'                    
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....               
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.             
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.           
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.         
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.   
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo. 
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `     
      `......:::::::::;iof688888888888888888888888888888b.         
        `....:::;iof688888888888888888888888888888888899fT!        
          `..::!8888888888888888888888888888888899fT|!^"'          
            `' !!988888888888888888888888899fT|!^"'                
                `!!8888888888888888899fT|!^"'                      
                  `!988888888899fT|!^"'                             
                    `!9899fT|!^"'                                  
    """

    print(Fore.CYAN + banner + Style.RESET_ALL)

    title = pyfiglet.figlet_format("automatic-follow-github", font="slant")
    print(Fore.YELLOW + title + Style.RESET_ALL)

    print(f"{'Welcome to the project automatic-follow-github':<55} {Fore.MAGENTA}| Made By: luisacoutinho06 💻{Style.RESET_ALL}\n")


def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_config(cfg):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)

def ensure_credentials():
    cfg = load_config()
    token = cfg.get("token")
    username = cfg.get("username")

    if not token:
        token = input(Fore.CYAN + "Enter your GitHub Personal Access Token: " + Style.RESET_ALL).strip()
        cfg["token"] = token
    if not username:
        username = input(Fore.CYAN + "Enter your GitHub username: " + Style.RESET_ALL).strip()
        cfg["username"] = username

    save_config(cfg)
    return token, username

def main_menu():
    token, username = ensure_credentials()

    while True:
        print()
        print(Fore.GREEN + "\n=== GitHub Auto Follow CLI ===" + Style.RESET_ALL)
        print(Fore.CYAN + "1)" + Style.RESET_ALL + " Follow back new followers")
        print(Fore.CYAN + "2)" + Style.RESET_ALL + " Unfollow users who don’t follow back")
        print(Fore.CYAN + "3)" + Style.RESET_ALL + " View saved config")
        print(Fore.CYAN + "4)" + Style.RESET_ALL + " Update token")
        print(Fore.CYAN + "5)" + Style.RESET_ALL + " Update username")
        print(Fore.CYAN + "6)" + Style.RESET_ALL + " Exit")

        choice = input(Fore.YELLOW + "Choose an option: " + Style.RESET_ALL).strip()

        if choice == "1":
            follow_back_new(token, username)
        elif choice == "2":
                unfollow_nonfollowers(token, username)
        elif choice == "3":
            cfg = load_config()
            print(Fore.WHITE + json.dumps({
                "username": cfg.get("username"),
                "token_present": bool(cfg.get("token"))
            }, indent=2) + Style.RESET_ALL)
        elif choice == "4":
            new_token = input(Fore.CYAN + "Enter new token: " + Style.RESET_ALL).strip()
            cfg = load_config()
            cfg["token"] = new_token
            save_config(cfg)
            print(Fore.GREEN + "Token updated successfully." + Style.RESET_ALL)
        elif choice == "5":
            new_username = input(Fore.CYAN + "Enter new username: " + Style.RESET_ALL).strip()
            cfg = load_config()
            cfg["username"] = new_username
            save_config(cfg)
            print(Fore.GREEN + "Username updated successfully." + Style.RESET_ALL)
        elif choice == "6":
            print(Fore.MAGENTA + "Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid option. Try again." + Style.RESET_ALL)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print_banner()
    main_menu()
