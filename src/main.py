import json
import os 
from pathlib import Path
from follow_back import follow_back_new

CONFIG_FILE = Path("config.json");

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

    print("\033[1;36m" + banner + "\033[0m")
    
    print(f"{'Welcome to the project automatic-follow-github':<55} \033[1;35m| Made By: luisacoutinho06 💻\033[0m\n")
    
        
def load_config():
      if CONFIG_FILE.exists():
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                  return json.load(f);
      return {};

def save_config(cfg):
      with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(cfg, f, indent=2);

def ensure_credentials():
      cfg = load_config();
      token = cfg.get("token");
      username = cfg.get("username");
      
      if not token:
            token = input("Enter your GitHub Personal Access Token: ").strip();
            cfg["token"] = token;
      if not username:
            username = input("Enter your GitHub username: ").strip();
            cfg["username"] = username;

      save_config(cfg);
      return token, username;

def main_menu():
      token, username = ensure_credentials();
      
      while True:
            print();
            print("\n=== GitHub Auto Follow CLI ===");
            print("1) Follow back new followers");
            print("2) View saved config");
            print("3) Update token");
            print("4) Update username");
            print("5) Exit");
            choice = input("Choose an option: ").strip();
            
            if choice == "1":
                  follow_back_new(token, username);
            elif choice == "2":
                  cfg = load_config();
                  print(json.dumps({
                        "username": cfg.get("username"),
                        "token_present": bool(cfg.get("token"))
                  }, indent=2));
            elif choice == "3":
                  new_token = input("Enter new token: ").strip();
                  cfg = load_config();
                  cfg["token"] = new_token;
                  save_config(cfg);
                  print("Token updated successfully.");
            elif choice == "4":
                  new_username = input("Enter new username: ").strip();
                  cfg = load_config();
                  cfg["username"] = new_username;
                  save_config(cfg);
                  print("Username updated successfully.");
            elif choice == "5":
                  print("Goodbye!");
                  break
            else:
                  print("Invalid option. Try again.");

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print_banner()
    main_menu() 