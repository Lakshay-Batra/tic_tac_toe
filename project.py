
def board(b):
    
    print('    |     |    ')
    print( b[7]+'   |  '+b[8]+'  |  '+b[9])
    print('----+-----+----')
    print('    |     |    ')
    print( b[4]+'   |  '+b[5]+'  |  '+b[6])
    print('----+-----+----')
    print('    |     |    ')
    print( b[1]+'   |  '+b[2]+'  |  '+b[3])
    print('\n')
def ply_inp():
    mrk=''
    while mrk!='X' and mrk!='O':
        mrk=input('Welcome to Tic Tac Toe.\n Player 1: Choose \'X\' or \'O\' : ')
    player1=mrk
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return(player1,player2)
import random
def first():
     if random.randint(0,1)==0:
        return 'Player 1'
     else:
        return 'Player 2'
def place_mrk(b,mrk,pos):
        b[pos]=mrk  
def win_chk(b,mrk):
        return (b[1]==mrk and b[2]==mrk and b[3]==mrk) or (b[4]==mrk and b[5]==mrk and b[6]==mrk) or (b[7]==mrk and b[8]==mrk and b[9]==mrk) or (b[1]==mrk and b[4]==mrk and b[7]==mrk) or (b[2]==mrk and b[5]==mrk and b[8]==mrk) or (b[3]==mrk and b[6]==mrk and b[9]==mrk) or (b[1]==mrk and b[5]==mrk and b[9]==mrk) or (b[3]==mrk and b[5]==mrk and b[7]==mrk)
def space_chk(b,pos):
        return b[pos]==' '
def full_chk(b):
    for i in range(1,10):
        if space_chk(b,i):
            return False
    return True 
def player_choice(b):
    pos=0
    while pos not in [1,2,3,4,5,6,7,8,9] or not space_chk(b,pos):
        pos=int(input('Enter position(1-9) : '))
    return pos
def replay():
    return input('Want to play again? (Yes/No) : ').lower()=='y'
print('Welcome to Tic Tac Toe!')
b=['#','1','2','3','4','5','6','7','8','9']
print('Enter the positions according to following matrix : \n')
board(b)
while True:
    b=[' ']*10
    player1,player2=ply_inp()
    print(f'Player-1 is : {player1} and Player-2 is : {player2}')
    turn=first()
    print(turn + ' will go first')
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn=='Player 1':
            board(b)
            pos=player_choice(b)
            place_mrk(b,player1,pos)
            if win_chk(b,player1):
                board(b)
                print('Congratulation! Player-1 has won')
                game_on=False
            else:
                if full_chk(b):
                    board(b)
                    print('Match is a draw')
                    break
                else:
                    turn='Player 2'
        else:
            board(b)
            pos=player_choice(b)
            place_mrk(b,player2,pos)
        
            if win_chk(b,player2):
                board(b)
                print('Congratulation! Player-2 has won')
                break
            else:
                if full_chk(b):
                    board(b)
                    print('Match is a draw')
                    break
                else:
                    turn='Player 1'
    if not replay():
        break
print('\nThank You for playing')     
