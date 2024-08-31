# game/views.py

from django.shortcuts import render
import random

def index(request):
    if request.method == 'POST':
        player_move = request.POST.get('move')
        computer_move = random.choice(['Rock', 'Paper', 'Scissors'])
        
        result = get_result(player_move, computer_move)
        
        return render(request, 'game/index.html', {
            'player_move': player_move,
            'computer_move': computer_move,
            'result': result,
        })
    
    return render(request, 'game/index.html')

def get_result(player_move, computer_move):
    if player_move == computer_move:
        return 'Tie'
    elif (player_move == 'Rock' and computer_move == 'Scissors') or \
         (player_move == 'Paper' and computer_move == 'Rock') or \
         (player_move == 'Scissors' and computer_move == 'Paper'):
        return 'You Win!'
    else:
        return 'You Lose!'
