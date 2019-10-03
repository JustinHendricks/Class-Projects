#Directions were to take a text file filled with players and their stats and create the best possible fantasy football lineup.
#I mainly uploaded because of the time constraints doing this project. I did it over the course of three hours without being familiar with extracting text. I was also suprised the code wasn't sloppier considering how much I was rushing.

players_text = open("players.txt", "r") #Opens the txt file containing players
player_list = [] #Used to convert raw text to mutable data
qb = [
    [], #List of names
    [], #List of Fantasy totals
    ]
rb = [
    [],
    [],
    ]
wr = [
    [],
    [],
    ]
te = [
    [],
    [],
    ]
line = players_text.readline()[:-1]
while line:
    player = line.split(' ') 
    player_list.append(player)
    line = players_text.readline()[:-1]
#Goes through each line

player_list[-1][7] = 12

def fantasy_points(player):
    points = 0
    points += (int(player[1]) // 25)
    points += (int(player[2]) * 4)
    points += (int(player[3]) // 10)
    points += (int(player[4]) * 6)
    points += (int(player[5]) // 10)
    points += (int(player[6]) * 6)
    return points

def add_to_list(position, lilist):
    if player_list[i][0] == position:      
        player_list[i].remove(player_list[i][0])
        lilist[0].append(player_list[i][0])
        score = fantasy_points(player_list[i])
        lilist[1].append(score)

for i in range(len(player_list)):
    add_to_list("QB", qb)
    add_to_list("RB", rb)
    add_to_list("WR", wr)
    add_to_list("TE", te)


def find_starter(position, number_needed, position_name):
    global find_starter
    x = 1
    while x <= number_needed:
        starter_score = max(position[1])
        i = position[1].index(starter_score)
        starter_name = position[0][i]
        if number_needed > 1:
            print(position_name + str(x) ,starter_name , starter_score)
        else:
            print(position_name , starter_name , starter_score)
        position[0].remove(position[0][i])
        position[1].remove(position[1][i])
        x += 1

def find_flex():
    rb_max = max(rb[1])
    wr_max = max(wr[1])
    te_max = max(te[1])
    max_score = max(rb_max, wr_max, te_max)
    if max_score == rb_max:
        i = rb[1].index(max_score)
        starter_name = rb[0][i]
    elif max_score == wr_max:
        i = wr[1].index(max_score)
        starter_name = wr[0][i]
    elif max_score == te_max:
        i = te[1].index(max_score)
        starter_name = te[0][i]
    print("FLEX" , starter_name, max_score)
    

def fantasy_team():
    find_starter(qb, 1, "QB")
    find_starter(rb, 2, "RB")
    find_starter(wr, 2, "WR")
    find_starter(te, 1, "TE")
    find_flex()

fantasy_team()
