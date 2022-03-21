PLAY_RULES = {
    'r': {'r': 0, 's': 1, 'p': -1},
    's': {'r': -1, 's': 0, 'p': 1},
    'p': {'r': 1, 's': -1, 'p': 0}
}

PLAYER_OPTIONS = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

SCORES = {'user_score': 0, 'system_score': 0, 'total_system': 0, 'total_user': 0}

RESULT_BANNER = {
    -1: 'You lose',
    0: 'You draw',
    1: 'You win'
}

CONTROL_OPTIONS = {'e': 'Exit'}
