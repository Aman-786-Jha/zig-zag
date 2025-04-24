import random

def zig_zag():


    dice_roll_history = {'player_1' : 0, 'player_2' : 0, 'player_3' : 0}
    position_history_players = {'player_1' : 0, 'player_2' : 0, 'player_3' : 0}
    grid_size = int(input("enter the no."))
    

    
    while True:

        player_1 = random.randint(1,6)
        print('player_1---------->', player_1)    # 1
        player_2 = random.randint(1,6)
        print('player_2---------->', player_2)   # 1
        player_3 = random.randint(1,6)
        print('player_3---------->', player_3)   # 5
        # print('dice_roll_history---------->', dice_roll_history)
        # print('position_history_players---------->', position_history_players)


        if player_1:
            print('position_history_players---------->', position_history_players['player_1'])
            if position_history_players['player_1'] + player_1 > grid_size * grid_size:
                print('no. comes outside of the grid')
                
            else:
                # dice_roll_history['player_1'] = player_1   # e.g 3
                position_history_players['player_1'] += player_1   # now at position 3

            if position_history_players['player_1'] == grid_size*grid_size:
                print('position of player 1 winning time-------------->',position_history_players['player_1'])
                print('position history-------------->',position_history_players)
                print('dice history-------------->',dice_roll_history)
                print('player_1 wins')
                return 1


            if position_history_players['player_2'] == position_history_players['player_1']:
                position_history_players['player_2'] = 0

            if position_history_players['player_3'] == position_history_players['player_1']:
                position_history_players['player_3'] = 0

            dice_roll_history['player_1'] = player_1
            dice_roll_history['player_2'] = 0
            dice_roll_history['player_3'] = 0

            print('dice_roll_history---------->', dice_roll_history)
            print('position_history_players---------->', position_history_players)

            


        if player_2:

            if position_history_players['player_2'] + player_2 > grid_size * grid_size:
                print('no. comes outside of the grid')
                
            else:
                # dice_roll_history['player_2'] = player_2   # e.g 3
                position_history_players['player_2'] += player_2   # now at position 3
            
            

            if position_history_players['player_2'] == grid_size*grid_size:
                print('position of player 2 winning time-------------->',position_history_players['player_2'])
                print('position history-------------->',position_history_players)
                print('dice history-------------->',dice_roll_history)
                print('player_2 wins')
                return 1


            if position_history_players['player_1'] == position_history_players['player_2']:
                position_history_players['player_1'] = 0

            if position_history_players['player_3'] == position_history_players['player_2']:
                position_history_players['player_3'] = 0

            dice_roll_history['player_1'] = 0
            dice_roll_history['player_2'] = player_2
            dice_roll_history['player_3'] = 0

            print('dice_roll_history---------->', dice_roll_history)
            print('position_history_players---------->', position_history_players)


        if player_3:
            if position_history_players['player_3'] + player_3 > grid_size * grid_size:
                print('no. comes outside of the grid')
                
            else:
                # dice_roll_history['player_3'] = player_3   # e.g 3
                position_history_players['player_3'] += player_3   # now at position 3

            
            
            

            if position_history_players['player_3'] == grid_size*grid_size:
                print('position of player 3 winning time-------------->',position_history_players['player_3'])
                print('position history-------------->',position_history_players)
                print('dice history-------------->',dice_roll_history)
                print('player_3 wins')
                return 1


            if position_history_players['player_1'] == position_history_players['player_3']:
                position_history_players['player_1'] = 0

            if position_history_players['player_2'] == position_history_players['player_3']:
                position_history_players['player_2'] = 0

            dice_roll_history['player_1'] = 0
            dice_roll_history['player_2'] = 0
            dice_roll_history['player_3'] = player_3

            print('dice_roll_history---------->', dice_roll_history)
            print('position_history_players---------->', position_history_players)




zig_zag()