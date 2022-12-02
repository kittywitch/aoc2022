with open("input.txt") as f:
    input = f.read().splitlines()

moves = {
    "A":"rock",
    "B":"paper",
    "C":"scissors",
    "X":"rock",
    "Y":"paper",
    "Z":"scissors",
}

outcomes = {
    "X":"lost",
    "Y":"draw",
    "Z":"win"
}

# paper beats rock B -> X, Y -> A
# rock beats scissors A -> Z, X -> C
# scissors beats paper C -> Y, Z -> B

hand_points = {
    "rock":1,
    "paper":2,
    "scissors":3
}

outcome_points = {
    "lost": 0,
    "draw":3,
    "win":6
}

def decide_outcome(player, opponent):
    if player == opponent:
        return "draw"
    elif player == "rock" and opponent == "scissors":
        return "win"
    elif player == "paper" and opponent == "rock":
        return "win"
    elif player == "scissors" and opponent == "paper":
        return "win"
    else:
        return "lost"

def fix_outcome(opponent, outcome):
    if outcome == "draw":
        return opponent
    elif outcome == "win":
        if opponent == "scissors":
            return "rock"
        elif opponent == "rock":
            return "paper"
        elif opponent == "paper":
            return "scissors"
    elif outcome == "lost":
        if opponent == "scissors":
            return "paper"
        elif opponent == "rock":
            return "scissors"
        elif opponent == "paper":
            return "rock"

def decide_round(line):
    player = moves[line[2]]
    opponent = moves[line[0]]
    outcome = decide_outcome(player, opponent)
    hand_point = hand_points[player]
    outcome_point = outcome_points[outcome]
    round_point = hand_point + outcome_point
    print(player, opponent, outcome, round_point)
    return round_point

def fix_round(line):
    print(line)
    outcome_decision = outcomes[line[2]]
    opponent = moves[line[0]]
    player = fix_outcome(opponent, outcome_decision)
    hand_point = hand_points[player]
    outcome_point = outcome_points[outcome_decision]
    round_point = hand_point + outcome_point
    print(player, opponent, outcome_decision, round_point)
    return round_point

total = 0
for line in input:
    total += decide_round(line)
print(total)

total = 0
for line in input:
    total += fix_round(line)
print(total)

