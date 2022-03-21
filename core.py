from Rock.constans import PLAY_RULES, PLAYER_OPTIONS
from datetime import datetime
from random import choice


def check_one_hand(user_input, system_choice):
    return PLAY_RULES[user_input][system_choice]


def modify_scores(current_score, current_result):
    if current_result == 1:
        current_score['user_score'] = current_score['user_score'] + 1
    elif current_result == -1:
        current_score['system_score'] = current_score['system_score'] + 1


def get_play_hand():
    play_hands = input('How many hand do you want to play: ')
    try:
        play_hands = int(play_hands)
    except ValueError as e:
        print('Please Enter just integer...', e)
        return get_play_hand()
    return play_hands


def system_choice_generator(n):
    for i in range(n):
        yield choice(list(PLAYER_OPTIONS.keys()))


def check_total(scores):
    if scores['user_score'] == 3:
        scores['total_user'] += 1
        scores['system_score'] = 0
        scores['user_score'] = 0

        print('#' * 30, '\tYou win the hand \t', '#' * 30)
        print('Total score : {} - {}'.format(
            scores['total_user'], scores['total_system']
        ))
        print('#' * 80)

    elif scores['system_score'] == 3:
        scores['total_system'] += 1
        scores['system_score'] = 0
        scores['user_score'] = 0

        print('#' * 30, '\tYou win the hand \t', '#' * 30)
        print('Total score : {} - {}'.format(
            scores['total_user'], scores['total_system']
        ))
        print('#' * 80)


def check_function(func):
    def check_time(*args, **kwargs):
        start_time = datetime.now()
        func()
        ended_time = datetime.now()
        duration = ended_time - start_time
        print('You have been playing in {} : {} seconds'.format(
            duration.seconds // 60, duration.seconds % 60
        ))
        return func()

    return check_time()
