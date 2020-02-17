class Monster():
    def __init__(self, name, hp=20):
        self.exp = 0
        self.name = name
        self.type = "Normal"
        self.current_hp = hp
        self.max_hp = hp
        self.attacks = {"wait": 0}
        self.possible_attacks = {"sneak_attack": 1,
                                 "slash": 2,
                                 "ice_storm": 3,
                                 "fire_storm": 3,
                                 "whirlwind": 3,
                                 "earthquake": 2,
                                 "double_hit": 4,
                                 "wait": 0
                                 }
    def add_attack(self, attack_name):
        if attack_name in self.possible_attacks:#check if attack_name is in the possible list and not already in self.attacks
            if attack_name not in self.attacks:
                if len(self.attacks) < 4: #make sure the number of unique attacks are less than 4
                    self.attacks[attack_name] = self.possible_attacks[attack_name]
                    #print(self.attacks)
                    return True
                else:
                    #lowest_values = []
                    lowest_attacks = []
                    x = min(self.attacks.values()) #use min function to sort the attacks by values and append to list
                    for i in self.attacks:
                        if self.attacks[i] == x:
                            lowest_attacks.append(i)
                            #print(lowest_attacks)
                    y = min(lowest_attacks) #remove the lowest attacks
                    self.attacks.pop(y)
                    self.attacks[attack_name] = self.possible_attacks[attack_name]
                    return True
            else:
                return False
        else:
            return False
    def remove_attack(self, attack_name): #check if attack name is in the attacks list
        if attack_name not in self.attacks:
            return False
        else:
            self.attacks.pop(attack_name)

        if len(self.attacks) == 0: #add wait if there is no attacks in self.attacks
            self.attacks["wait"] = 0
        return True

#win_fight should add 5 to monster self.exp and reset curent_hp to max_hp
#lose_fight reset hp but add 1 exp to self.exp

    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp

    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp

#monster1 goes first
#each monster takes a turn using one attack move
class Ghost(Monster):
    def win_fight(self):
        self.exp += 5 #apparently not going through the win_fight of monster class for the exp increase
        self.current_hp = self.max_hp ####
        u = 10
        k = 19
        if self.exp in range(u,k):
            u += 10
            k += 10
            self.max_hp += 5
    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp

class Dragon(Monster):
    def win_fight(self):
        self.exp += 5 ####
        self.current_hp = self.max_hp######
        c = 10
        v = 19
        if self.exp in range(c,v):
            c += 10
            v += 10
            for key in self.attacks:
                self.attacks[key] += 1
    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp

def monster_fight(monster1, monster2):#return round1, monster1, moves1#movies of winner
    if monster1.attacks == {"wait":0} and monster2.attacks == {"wait":0}:  # if both monsters have wait as attack
        return -1, None, None
    movecopy = {} #dict of sorted monster1 attacks
    movecopy2 = {} #dict of sorted monster2 attacks
    for x, y in sorted(monster1.attacks.items(), key=lambda z: z[1], reverse=True): #used StackOverflow to find a method to sort dict by values
        movecopy[x] = y
    for c, d in sorted(monster2.attacks.items(), key=lambda z: z[1], reverse=True):
        movecopy2[c] = d
    #print(movecopy)
    #print(movecopy2)

    M1_list = [] #list of keys of attacks
    for key in movecopy.keys():
        M1_list.append(key)
    M2_list = []
    for key in movecopy2.keys():
        M2_list.append(key)
    #print(M1_list)
    #print(M2_list)
    #print(movecopy['ice_storm'])
    round = 0

    #count1 = 0
    #count2 = 0
    while (monster1.current_hp > 0) and (monster2.current_hp >0):
        if monster1.current_hp <= 0 and monster2.current_hp <= 0:
            break
        round = round + 1
        monster2.current_hp -= movecopy[M1_list[(round - 1) % len(M1_list)]]
        monster1.current_hp -= movecopy2[M2_list[(round - 1) % len(M2_list)]]
        #print(monster1.current_hp)
        #print(monster2.current_hp)
    M1_total_attacks = []
    M2_total_attacks = []
    M1_total_attacks = M1_list * 1000
    M2_total_attacks = M2_list * 1000
    moves1 = M1_total_attacks[0:round]
    moves2 = M2_total_attacks[0:round]
    #print(moves1)
    #print(moves2)
    #print(round)
    round1 = round
    if monster1.current_hp == monster2.current_hp:
        monster1.win_fight()
        monster2.lose_fight()
        return round1, monster1, moves1
    if monster1.current_hp > monster2.current_hp:#check for winner
        monster1.win_fight()
        monster2.lose_fight()
        return round1, monster1, moves1
    elif monster1.current_hp < monster2.current_hp:
        monster2.win_fight()
        monster1.lose_fight()
        return round1, monster2, moves2

# a = Dragon("a", 45)
# b = Ghost("b", 45)
# a.add_attack("ice_storm")
# b.add_attack("double_hit")
# b.remove_attack("wait")
# round1, winner, moves = monster_fight(a,b)
# print(round1)
# print(winner.name)
# print(winner.attacks)
# print(winner.exp)
# print(winner.max_hp)
# print(moves)
# round1, winner, moves = monster_fight(a,b)
# print(round1)
# print(winner.name)
# print(winner.attacks)
# print(winner.exp)
# print(winner.max_hp)
# print(moves)
# a.remove_attack("wait")
# b.remove_attack("double_hit")
# b.add_attack("ice_storm")
# round1, winner, moves = monster_fight(a,b)
# print(round1) #suppose to be 17, not 15
# print(winner.name)
# print(winner.attaks)
# print(winner.exp)
# print(winner.max_hp)
# print(moves)
# a.add_attack("wait")
# round1, winner, moves = monster_fight(a,b)
# print(round1)
# print(winner.name)
# print(winner.attacks)
# print(winner.exp)
# print(winner.max_hp)
# print(moves)
# b.add_attack("double_hit")
# b.remove_attack("ice_storm")
# round1, winner, moves = monster_fight(a,b)
# print(round1)
# print(winner.name)
# print(winner.attacks)
# print(winner.exp)
# print(winner.max_hp)
# print(moves)
