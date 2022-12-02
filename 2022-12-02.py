
f = open('2022-12-02.csv','r')

strategy = []
first_score_count = 0
second_score_count = 0


my_dict = {
                'X': 'rock',
                'Y': 'paper',
                'Z': 'scissors'}

necessary_result = {
                    'X': 'loss',
                    'Y': 'draw',
                    'Z': 'win'
                    }

opponent_dict = {
            'A': 'rock',
            'B': 'paper',
            'C': 'scissors'
            }

score_dict = {
            'rock': 1,
            'paper': 2,
            'scissors': 3
            }

result_score_dict = {
                    'loss': 0,
                    'draw': 3,
                    'win': 6
                    }
def find_the_right_move(opp_move, necessary_result):
    # function used for part two
    if necessary_result == 'draw':
        return opp_move, result_score_dict[necessary_result]
    elif opp_move == 'rock' and necessary_result == 'loss':
        return 'scissors', result_score_dict[necessary_result]
    elif opp_move == 'scissors' and necessary_result == 'win':
        return 'rock', result_score_dict[necessary_result]
    elif necessary_result == 'loss':
        return [i for i in score_dict.keys() if score_dict[i] == score_dict[opp_move]-1][0], result_score_dict[necessary_result]
    else:
        return [i for i in score_dict.keys() if score_dict[i] == score_dict[opp_move]+1][0], result_score_dict[necessary_result]

for line in f:
    line = line.replace('\n', '')
    opp_move = opponent_dict[line[0]]
    my_move = my_dict[line[-1]]
    first_score_count += score_dict[my_move]

    if opp_move == my_move:
        first_score_count += result_score_dict['draw']
    elif (my_move == 'rock' and opp_move == 'scissors'):
        first_score_count += result_score_dict['win']
    elif (my_move == 'scissors' and opp_move == 'rock'):
        first_score_count += result_score_dict['loss']
    elif score_dict[my_move] > score_dict[opp_move]:
        first_score_count += result_score_dict['win']
    else:
        first_score_count += result_score_dict['loss']

    # calculate the values for part 2:
    second_my_move, game_result = find_the_right_move(opp_move, necessary_result[line[-1]])
    second_score_count += score_dict[second_my_move] + game_result

f.close()

print(first_score_count)
print(second_score_count)