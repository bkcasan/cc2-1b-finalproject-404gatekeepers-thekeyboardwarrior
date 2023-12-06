class Dialogues:
    @staticmethod
    def start_menu():
        print("""
888    d8P                    888                                     888       888       888                          d8b                  
888   d8P                     888                                     888       888   o   888                          Y8P                  
888  d8P                      888                                     888       888  d8b  888                                               
888d88K      .d88b.  888  888 88888b.   .d88b.   8888b.  888d888  .d88888       888 d888b 888  8888b.  888d888 888d888 888  .d88b.  888d888 
8888888b    d8P  Y8b 888  888 888 "88b d88""88b     "88b 888P"   d88" 888       888d88888b888     "88b 888P"   888P"   888 d88""88b 888P"   
888  Y88b   88888888 888  888 888  888 888  888 .d888888 888     888  888       88888P Y88888 .d888888 888     888     888 888  888 888     
888   Y88b  Y8b.     Y88b 888 888 d88P Y88..88P 888  888 888     Y88b 888       8888P   Y8888 888  888 888     888     888 Y88..88P 888     
888    Y88b  "Y8888   "Y88888 88888P"   "Y88P"  "Y888888 888      "Y88888       888P     Y888 "Y888888 888     888     888  "Y88P"  888     
                          888                                                                                                               
                     Y8b d88P                                                                                                               
                      "Y88P"                                                                                                                                                                                                                             
""")
        print("1. Start")
        print("2. Credits")
        print("3. Exit")

    @staticmethod
    def player_stats(player_stats):
        print("Player Stats:")
        print(f"Health: {player_stats['health']}")
        print(f"Attack: {player_stats['attack']}")
        print(f"Defense: {player_stats['defense']}")

    @staticmethod
    def enemy_stats(enemy_stats):
        print("Enemy Stats:")
        print(f"Health: {enemy_stats['health']}")
        print(f"Attack: {enemy_stats['attack']}")
        print(f"Defense: {enemy_stats['defense']}")

    @staticmethod
    def enemy_encounter():
        print("You've encountered an enemy!")

    @staticmethod
    def checkpoint_reached():
        print("You've met a old friend")
        print("""
⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉                                                                                                                                                                                                                     
""")

    @staticmethod
    def victory():
        print("You defeated the enemy!")

    @staticmethod
    def credits():
        print("Game created by Your Name")
