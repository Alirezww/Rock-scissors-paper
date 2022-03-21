from Rock.constans import SCORES, PLAYER_OPTIONS, RESULT_BANNER, CONTROL_OPTIONS
from Rock.core import check_one_hand, modify_scores, check_total, check_function, get_play_hand, system_choice_generator


@check_function
def start_game():
    play = True
    plays_hands = get_play_hand()
    system_choice = 'r'
    while play:
        user_input = input('Please Enter your option (s, r, p) : ')
        for i in system_choice_generator(plays_hands):
            system_choice = i

        if user_input in PLAYER_OPTIONS.keys():
            result = check_one_hand(user_input, system_choice)
            modify_scores(SCORES, result)

            print("Your choice : {} , System choice : {}, result : {}\tscores : {} - {} ".format(
                PLAYER_OPTIONS[user_input], PLAYER_OPTIONS[system_choice], RESULT_BANNER[result], SCORES['user_score'],
                SCORES['system_score']
            ))

            check_total(SCORES)

        elif user_input in CONTROL_OPTIONS.keys():
            play = False
            print('The game is over,,,  bye!!')

        else:
            print('PLease enter another option .... ')


if __name__ == '__main__':
    start_game()
