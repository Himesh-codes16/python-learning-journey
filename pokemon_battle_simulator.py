import random
class pokemon:
    def __init__(self,name,pktype,hp,moves):
        self.name = name
        self.pktype = pktype
        self.max_hp = hp
        self.hp = hp
        self.moves = moves
        self.status = None
    def show_stats(self):
        print("----------")
        print("Name:",self.name)
        print("Type:",self.pktype)
        print("HP:",self.hp)
        print("Status:",self.status)
        print("----------")
    def reset_hp(self):
        self.hp = self.max_hp
        self.status = None
    def attack_pokemon(self,opponent,damage,move):
        print(self.name,"used",move)
        accuracy = self.moves[move]["accuracy"]
        chance = random.randint(1,100)
        if chance > accuracy:
            print(self.name,"missed!")
            print("--------------------")
            return
        multiplier = type_effectiveness[self.pktype][opponent.pktype]
        if multiplier == 2:
            print("It's super effective!")
        elif multiplier == 0.5:
            print("It's not very effective!")
        damage = multiplier*damage
        crit = random.randint(1,100)
        if crit > 90:
            print("It's a Critical Hit!")
            damage += 10
        opponent.hp = opponent.hp - damage
        print(self.name,"attacked",opponent.name)
        print(opponent.name,"lost",damage,"HP")
        if move == "Thunder Shock":
            chance = random.randint(1,4)
            if chance == 1:
                opponent.status = "Paralysed"
                print(opponent.name,"is Paralysed")
        print("--------------------")
    def heal_pk(self,amount,move):
        self.hp = min(self.hp + amount, self.max_hp)
        print(self.name,"used",move)
        print(self.name,"recovered",amount,"HP")
        print(self.name,"HP:",self.hp,"/",self.max_hp)
        print("--------------------")
    def show_hp(self):
        print(self.hp,"/",self.max_hp)
pikachu_moves = {
    "Thunder Shock": {"damage": 20, "accuracy": 90},
    "Quick Attack": {"damage": 15, "accuracy": 100},
    "Electro Ball": {"damage": 30, "accuracy": 85},
    "Recover": {"heal": 20, "accuracy": 100}
}
sqirtle_moves = {
    "Water Gun": {"damage": 20, "accuracy": 95},
    "Tackle": {"damage": 15, "accuracy": 100},
    "Bubble": {"damage": 25, "accuracy": 95},
    "Aqua Ring": {"heal": 20, "accuracy": 100}
}
charizard_moves = {
    "Flamethrower": {"damage": 25, "accuracy": 95},
    "Dragon Claw": {"damage": 20, "accuracy": 100},
    "Fire Spin": {"damage": 30, "accuracy": 80},
    "Roost": {"heal": 20, "accuracy": 100}
}
bulbasaur_moves = {
    "Vine Whip": {"damage": 20, "accuracy": 95},
    "Tackle": {"damage": 15, "accuracy": 100},
    "Razor Leaf": {"damage": 30, "accuracy": 85},
    "Synthesis": {"heal": 20, "accuracy": 100}
}
geodude_moves = {
    "Rock Throw": {"damage": 25, "accuracy": 90},
    "Tackle": {"damage": 15, "accuracy": 100},
    "Rock Slide": {"damage": 30, "accuracy": 85},
    "Recover": {"heal": 20, "accuracy": 100}
}
pidgey_moves = {
    "Gust": {"damage": 20, "accuracy": 95},
    "Quick Attack": {"damage": 15, "accuracy": 100},
    "Wing Attack": {"damage": 25, "accuracy": 90},
    "Roost": {"heal": 20, "accuracy": 100}
}
machop_moves = {
    "Low Kick": {"damage": 20, "accuracy": 95},
    "Karate Chop": {"damage": 25, "accuracy": 90},
    "Brick Break": {"damage": 30, "accuracy": 85},
    "Bulk Up": {"heal": 20, "accuracy": 100}
}
gastly_moves = {
    "Lick": {"damage": 20, "accuracy": 95},
    "Night Shade": {"damage": 25, "accuracy": 90},
    "Shadow Ball": {"damage": 30, "accuracy": 85},
    "Recover": {"heal": 20, "accuracy": 100}
}
type_effectiveness = {
    "Electric":{
        "Water":2,
        "Flying":2,
        "Grass":0.5,
        "Rock":0.5,
        "Fire":0.5,
        "Electric":1,
        "Fighting":1,
        "Ghost":1
    },
    "Water":{
        "Fire":2,
        "Rock":2,
        "Grass":0.5,
        "Electric":0.5,
        "Water":1,
        "Flying":1,
        "Fighting":1,
        "Ghost":1
    },
    "Fire":{
        "Grass":2,
        "Rock":0.5,
        "Water":0.5,
        "Fire":1,
        "Electric":1,
        "Flying":1,
        "Fighting":1,
        "Ghost":1
    },
    "Grass":{
        "Water":2,
        "Rock":2,
        "Fire":0.5,
        "Flying":0.5,
        "Grass":1,
        "Electric":1,
        "Fighting":1,
        "Ghost":1
    },
    "Rock":{
        "Fire":2,
        "Flying":2,
        "Electric":2,
        "Water":0.5,
        "Grass":0.5,
        "Rock":1,
        "Fighting":1,
        "Ghost":1
    },
    "Flying":{
        "Grass":2,
        "Fighting":2,
        "Electric":0.5,
        "Rock":0.5,
        "Fire":1,
        "Water":1,
        "Flying":1,
        "Ghost":1
    },
    "Fighting":{
        "Rock":2,
        "Ghost":0.5,
        "Flying":0.5,
        "Fighting":1,
        "Fire":1,
        "Water":1,
        "Grass":1,
        "Electric":1
    },
    "Ghost":{
        "Fighting":2,
        "Ghost":2,
        "Electric":1,
        "Water":1,
        "Fire":1,
        "Grass":1,
        "Rock":1,
        "Flying":1
    }
}
pikachu = pokemon("Pikachu","Electric",100,pikachu_moves)
sqirtle = pokemon("Squirtle","Water",100,sqirtle_moves)
charizard = pokemon("Charizard","Fire",100,charizard_moves)
bulbasaur = pokemon("Bulbasaur","Grass",100,bulbasaur_moves)
geodude = pokemon("Geodude","Rock",100,geodude_moves)
pidgey = pokemon("Pidgey","Flying",100,pidgey_moves)
machop = pokemon("Machop","Fighting",100,machop_moves)
gastly = pokemon("Gastly","Ghost",100,gastly_moves)
pokemon_list = [
    pikachu,
    sqirtle,
    charizard,
    bulbasaur,
    geodude,
    pidgey,
    machop,
    gastly
]
def play_game():
    print("\n\n================================")
    print("        ⚡ POKEMON BATTLE ⚡")
    print("================================")
    print("Choose your Pokemon!\n")
    for num,pk in enumerate(pokemon_list,1):
        print(f"{num}.{pk.name} - {pk.pktype} Type")
    while True:
        print("\n================================")
        print("       TYPE EFFECTIVENESS")
        print("================================")
        print("Electric  → Water, Flying")
        print("Water     → Fire, Rock")
        print("Fire      → Grass")
        print("Grass     → Water, Rock")
        print("Rock      → Fire, Flying, Electric")
        print("Flying    → Grass, Fighting")
        print("Fighting  → Rock")
        print("Ghost     → Fighting, Ghost")
        print("--------------------------------")
        print("×2   = Super Effective")
        print("×0.5 = Not Very Effective")
        print("×1   = Normal Damage")
        print("================================")
        try:
            choice = int(input("Choose your Pokemon "))
            if choice >= 1 and choice <= 8:
                player_pk = pokemon_list[choice-1]
                break
            else:
                print("Invalid Choice ! Please choose a valid Pokemon (1-8) Enter the number of the Pokemon You want to select")
        except:
            print("Invalid Choice ! Please choose a valid Pokemon (1-8) Enter the number of the Pokemon You want to select")
    while True:
        computer_pk = random.choice(pokemon_list)
        if computer_pk == player_pk:
            continue
        else:
            break
    player_pk.show_stats()
    computer_pk.show_stats()
    print("\n==============================")
    print("          BATTLE START")
    print("==============================")
    print(f"{player_pk.name}  VS  {computer_pk.name}")
    print("==============================")
    while True:
        ch1 = input(f"\nDo you want to attack {computer_pk.name}? (yes/no): ").lower()
        if ch1 == "yes":
            print("\n---------- MOVES ----------")
            for number,move in enumerate(player_pk.moves,1):
                move_data = player_pk.moves[move]
                if "damage" in move_data:
                    print(f"{number}. {move} | Damage: {move_data['damage']} | Accuracy: {move_data['accuracy']}%")
                elif "heal" in move_data:
                    print(f"{number}. {move} | Heal: {move_data['heal']} HP | Accuracy: {move_data['accuracy']}%")
            print("---------------------------")
            while True:
                try:
                    sel = int(input("Which move you want to use "))
                    if sel >= 1 and sel <= 4:
                        break
                    else:
                        print("Please enter a valid choice number (1-4)")
                except:
                    print("Invalid Input! Please enter a number")
            selected_move = list(player_pk.moves)[sel - 1]
            print(f"\nYou selected: {selected_move}")
            if player_pk.status == "Paralysed":
                if random.randint(1,4) == 1:
                    print(player_pk.name, "is Paralysed and cannot attack!")
                    continue
            if "damage" in player_pk.moves[selected_move]:
                player_pk.attack_pokemon(computer_pk,
                                         player_pk.moves[selected_move]["damage"],
                                         selected_move)
            elif "heal" in player_pk.moves[selected_move]:
                player_pk.heal_pk(player_pk.moves[selected_move]["heal"],
                      selected_move)
            print(computer_pk.name)
            computer_pk.show_hp()
            if computer_pk.hp <= 0:
                break
        elif ch1 == "no":
            break
        else:
            print("Please enter yes or no")
            continue
        if computer_pk.status == "Paralysed":
            if random.randint(1, 4) == 1:
                print(computer_pk.name, "is Paralysed and cannot attack!")
                continue
        computer = random.choice(list(computer_pk.moves))
        if "damage" in computer_pk.moves[computer]:
            computer_pk.attack_pokemon(player_pk,
                                        computer_pk.moves[computer]["damage"],
                                        computer)
        elif "heal" in computer_pk.moves[computer]:
            computer_pk.heal_pk(computer_pk.moves[computer]["heal"],
                                computer)
        print(computer_pk.name, "used", computer)
        print(player_pk.name)
        player_pk.show_hp()
        if player_pk.hp <= 0:
            break
    print("\n==============================")
    if computer_pk.hp <= 0:
        print("        BATTLE OVER")
        print("==============================")
        print(f"🏆 {player_pk.name} WINS!")
        print(f"{player_pk.name} remaining HP: {player_pk.hp}/{player_pk.max_hp}")
    elif player_pk.hp <= 0:
        print("        BATTLE OVER")
        print("==============================")
        print(f"🏆 {computer_pk.name} WINS!")
        print(f"{computer_pk.name} remaining HP: {computer_pk.hp}/{computer_pk.max_hp}")
    print("==============================")
while True:
    play_game()
    for pk in pokemon_list:
        pk.reset_hp()
    print("\n==============================")
    print("        PLAY AGAIN?")
    print("==============================")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        continue
    elif play_again == "no":
         break
    else:
        print("Enter Valid Input ")