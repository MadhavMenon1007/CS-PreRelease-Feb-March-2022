### Task 1 ###

recheck = True
while recheck == True:
    num_players = int(input("Enter the number of players (2/3/4): "))
    while num_players < 2 or num_players > 4:
        num_players = int(input("Error. Only 2, 3, or 4 players can play. Enter again: "))
    names = []
    for i in range(num_players):
        name = input(f"Player {i+1}, enter your name: ")
        names.append(name)
    num_holes = int(input("Enter the number of holes (9/18): "))
    while num_holes != 9 and num_holes != 18:
        num_holes = int(input("Error. Only 9 or 18 holes can be played. Enter again: "))
    player_one_scores = []
    player_two_scores = []
    player_three_scores = []
    player_four_scores = []
    total_scores = []
    for i in range(num_holes):
        player_one_scores.append(0)
        player_two_scores.append(0)
        player_three_scores.append(0)
        player_four_scores.append(0)
    
    for i in range(num_players):
        total_scores.append(0)
    par = int(input("Enter the par: "))
    while par < num_holes:
        par = int(input("Error. par cannot be less than ", num_holes, "enter par again: "))
    print("Number of players playing: ", num_players)
    for i in names:
        print(i, "is playing")
    print("Number of holes: ", num_holes)
    print("Par: ", par)
    choice = input("Would you like to make changes?(Y/N): ")
    if choice == "N" or choice == "n":
        recheck = False

### Task 2 ###

num_holes_played = 1
while num_holes_played <= num_holes:
    print("Hole", num_holes_played, "is over.")
    for i in range(0, num_players):
        score_one = int(input(f"{names[i]}, enter your score for hole {num_holes_played}: "))
        score_two = int(input(f"Enter your score again for verification: "))
        while score_one != score_two:
            score_two = int(input("Error. score one must equal score two. Enter score two again: "))
        total_scores[i]+=score_two
        if i==0:
            player_one_scores[num_holes_played-1] = score_two
        if i==1:
            player_two_scores[num_holes_played-1] = score_two
        if i==2:
            player_three_scores[num_holes_played-1] = score_two
        if i==3:
            player_four_scores[num_holes_played-1] = score_two
        choice = input(f"{names[i]}, would you like to see your total score so far?(Y/N): ")
        if choice == "Y" or choice == "y":
            print("Your total score so far is", total_scores[i])
    num_holes_played+=1

### Task 3 ###

for i in range(0, num_players):
    if total_scores[i] > par:
        print(names[i], "had a score of", total_scores[i]-par, "over par")
    if total_scores[i] < par:
        print(names[i], "had a score of", par - total_scores[i],"under par")
    if total_scores[i] == par:
        print(names[i], "had a score equal to par")

winner_score = total_scores[i]
winner_name = ""
for i in range(0, num_players):
    if winner_score > total_scores[i]:
        winner_score = total_scores[i]
        winner_name = names[i]

print("The winner is", winner_name,"who had a score of",winner_score)

choice_again = True
while choice_again == True:
    choice = int(input("Choose an additional option if you would like to. \n1. Each player’s score for each hole. \n2. Number of hole in ones per player\n 3. Average score for the round. \n4. Average score for the hole\n: "))
    while choice < 1 or choice > 4:
        choice = int(input("Error. Enter again: "))


    if choice == 1:
        for i in range(0, num_players):
            print(names[i], "scores: ")
            for hole in range(0, num_holes):
                if i==0:
                    print("Hole", hole+1, ":",end=" ")
                    print(player_one_scores[hole], "strokes")
                if i==1:
                    print("Hole", hole+1, ":",end=" ")
                    print(player_two_scores[hole], "strokes")
                if i==2:
                    print("Hole", hole+1, ":",end=" ")
                    print(player_three_scores[hole], "strokes")
                if i==3:
                    print("Hole", hole+1, ":",end=" ")
                    print(player_four_scores[hole], "strokes")
        
    if choice == 2:
        for i in range(0, num_players):
            for hole in range(0, num_holes):
                if i==0:
                    if player_one_scores[hole] == 1:
                        print(names[i],"has a hole in one at", hole+1)
                if i==1:
                    if player_two_scores[hole] == 1:
                        print(names[i],"has a hole in one at", hole+1)
                if i==2:
                    if player_three_scores[hole] == 1:
                        print(names[i],"has a hole in one at", hole+1)
                if i==3:
                    if player_four_scores[hole] == 1:
                        print(names[i],"has a hole in one at", hole+1)

    if choice == 3:
        total_sum_score = 0
        for score in total_scores:
            total_sum_score += score
        average_round_score = total_sum_score / num_players
        print("The average score for the round is", average_round_score)

    if choice == 4:
        for hole in range(0, num_holes):
            total_hole_score = 0
            total_hole_score = player_one_scores[hole] + player_two_scores[hole] + player_three_scores[hole] + player_four_scores[hole]
            average_hole_score = total_hole_score / num_players
            print("The average score for hole", hole+1, "is", average_hole_score)
    choice_check = input("Would you like to continue again? (Y/N): ")
    if choice_check == "N" or choice_check == "n":
        choice_again = False

    