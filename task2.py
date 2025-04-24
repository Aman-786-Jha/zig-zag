import random

def zig_zag():


    dice_roll_history = {'player_1' : 0, 'player_2' : 0, 'player_3' : 0}
    position_history_players = {'player_1' : 0, 'player_2' : 0, 'player_3' : 0}
    grid_size = int(input("enter the no."))

    coordinate_player_history = {'player_1' : {-1,-1}, 'player_2' : {-1,-1}, 'player_3' : {-1,-1}}

    coordinate_history_grid_2 = {
        1 : (0,0),
        2 : (1,0),
        3 : (1,1),
        4 : (0,1)
        
    }

    coordinate_history_grid_3 = {
        1 : (0,0),
        2 : (1,0),
        3 : (2,0),
        4 : (2,1),
        5 : (1,1),
        6 : (0,1),
        7 : (0,2),
        8 : (1,2),
        9 : (2,2)
        
    }

    coordinate_history_grid_4 = {
        1 : (0,0),
        2 : (1,0),
        3 : (2,0),
        4 : (3,0),
        5 : (3,1),
        6 : (2,1),
        7 : (1,1),
        8 : (0,1),
        9 : (0,2),
        10 : (1,2),
        11 : (2,2),
        12 : (3,2),
        13 : (3,3),
        14 : (2,3),
        15 : (1,3),
        16 : (0,3)
        
    }

    
    while True:

        if grid_size == 2:

            player_1 = random.randint(1,6)
            print('player_1---------->', player_1)    # 1
            player_2 = random.randint(1,6)
            print('player_2---------->', player_2)   # 1
            player_3 = random.randint(1,6)
            print('player_3---------->', player_3)   # 5
            # print('dice_roll_history---------->', dice_roll_history)
            # print('position_history_players---------->', position_history_players)


            if player_1:
                dice_roll_history['player_1'] = player_1
                dice_roll_history['player_2'] = player_2
                dice_roll_history['player_3'] = player_3

                print('dice_roll_history---------->', dice_roll_history)
                # print('position_history_players---------->', position_history_players)
                # print('position_history_players---------->', position_history_players['player_1'])
                if position_history_players['player_1'] + player_1 > grid_size * grid_size:
                    print('no. comes outside of the grid')
                
                    
                else:
                    # dice_roll_history['player_1'] = player_1   # e.g 3
                    position_history_players['player_1'] += player_1   # now at position 3
                    print('position_history_players_when_player_1_played---------->', position_history_players)
                    old_position_player_1 = position_history_players['player_1']
                    if old_position_player_1 in coordinate_history_grid_2:
                        print('coordinate_history_of_player_1----------->>', coordinate_history_grid_2[old_position_player_1])
                        coordinate_player_history['player_1'] = coordinate_history_grid_2[old_position_player_1]
                        print('coordinate_history_player------------>', coordinate_player_history)

                if position_history_players['player_1'] == grid_size*grid_size:
                    # print('position of player 1 winning time-------------->',position_history_players['player_1'])
                    print('position history_at_winning_time-------------->',position_history_players)
                    # print('dice history-------------->',dice_roll_history)
                    print('player_1 wins')
                    old_position_player_1 = position_history_players['player_1']
                    if old_position_player_1 in coordinate_history_grid_2:
                        print('coordinate_history_of_player_1----------->>', coordinate_history_grid_2[old_position_player_1])
                        coordinate_player_history['player_1'] = coordinate_history_grid_2[old_position_player_1]
                        print('coordinate_history_player------------>', coordinate_player_history)
                    return 1


                if position_history_players['player_2'] == position_history_players['player_1']:
                    position_history_players['player_2'] = 0
                    print('position_history_players_when_player_1 cut_player_2---------->', position_history_players)
                    # old_position_player_2 = position_history_players['player_2']
                    # if old_position_player_2 in coordinate_history_grid_2:
                    #     print('coordinate_history_of_player----------->>', coordinate_history_grid_2[old_position_player_1])
                    

                if position_history_players['player_3'] == position_history_players['player_1']:
                    position_history_players['player_3'] = 0
                    print('position_history_players_when_player_1 cut_player_3---------->', position_history_players)

                

                


            if player_2:

                dice_roll_history['player_1'] = player_1
                dice_roll_history['player_2'] = player_2
                dice_roll_history['player_3'] = player_3

                print('dice_roll_history---------->', dice_roll_history)
                # print('position_history_players---------->', position_history_players)

                if position_history_players['player_2'] + player_2 > grid_size * grid_size:
                    print('no. comes outside of the grid')
                    
                else:
                    # dice_roll_history['player_2'] = player_2   # e.g 3
                    position_history_players['player_2'] += player_2   # now at position 3
                    print('position_history_players_when_player_2_played---------->', position_history_players)
                    old_position_player_2 = position_history_players['player_2']
                    if old_position_player_2 in coordinate_history_grid_2:
                        print('coordinate_history_of_player_2----------->>', coordinate_history_grid_2[old_position_player_2])
                        coordinate_player_history['player_2'] = coordinate_history_grid_2[old_position_player_2]
                        print('coordinate_history_player------------>', coordinate_player_history)
                
                

                if position_history_players['player_2'] == grid_size*grid_size:
                    # print('position of player 2 winning time-------------->',position_history_players['player_2'])
                    print('position history when player 2 winning time-------------->',position_history_players)
                    # print('dice history-------------->',dice_roll_history)
                    print('player_2 wins')
                    old_position_player_2 = position_history_players['player_2']
                    if old_position_player_2 in coordinate_history_grid_2:
                        print('coordinate_history_of_player_2----------->>', coordinate_history_grid_2[old_position_player_2])
                        coordinate_player_history['player_2'] = coordinate_history_grid_2[old_position_player_2]
                        print('coordinate_history_player------------>', coordinate_player_history)
                    return 1


                if position_history_players['player_1'] == position_history_players['player_2']:
                    position_history_players['player_1'] = 0
                    print('position history when player 2 cuts player 1-------------->',position_history_players)

                if position_history_players['player_3'] == position_history_players['player_2']:
                    position_history_players['player_3'] = 0
                    print('position history when player 2 cuts player 3-------------->',position_history_players)

                


            if player_3:
                dice_roll_history['player_1'] = player_1
                dice_roll_history['player_2'] = player_2
                dice_roll_history['player_3'] = player_3

                print('dice_roll_history---------->', dice_roll_history)
                # print('position_history_players---------->', position_history_players)
                if position_history_players['player_3'] + player_3 > grid_size * grid_size:
                    print('no. comes outside of the grid')
                    
                else:
                    # dice_roll_history['player_3'] = player_3   # e.g 3
                    position_history_players['player_3'] += player_3   # now at position 3
                    print('position_history_players_when_player_3_played---------->', position_history_players)
                    old_position_player_3 = position_history_players['player_3']
                    if old_position_player_3 in coordinate_history_grid_2:
                        print('coordinate_history_of_player_3----------->>', coordinate_history_grid_2[old_position_player_3])
                        coordinate_player_history['player_3'] = coordinate_history_grid_2[old_position_player_3]
                        print('coordinate_history_player------------>', coordinate_player_history)

                
                
                

                if position_history_players['player_3'] == grid_size*grid_size:
                    # print('position of player 3 winning time-------------->',position_history_players['player_3'])
                    print('position history at the time of winning player 3-------------->',position_history_players)
                    # print('dice history-------------->',dice_roll_history)
                    print('player_3 wins')
                    old_position_player_3 = position_history_players['player_3']
                    if old_position_player_3 in coordinate_history_grid_2:
                        print('coordinate_history_of_player_3----------->>', coordinate_history_grid_2[old_position_player_3])
                        coordinate_player_history['player_3'] = coordinate_history_grid_2[old_position_player_3]
                        print('coordinate_history_player------------>', coordinate_player_history)
                    return 1


                if position_history_players['player_1'] == position_history_players['player_3']:
                    position_history_players['player_1'] = 0

                if position_history_players['player_2'] == position_history_players['player_3']:
                    position_history_players['player_2'] = 0


################################## grid size 3 ###############
        if grid_size == 3:

            player_1 = random.randint(1,6)
            print('player_1---------->', player_1)    # 1
            player_2 = random.randint(1,6)
            print('player_2---------->', player_2)   # 1
            player_3 = random.randint(1,6)
            print('player_3---------->', player_3)   # 5
            # print('dice_roll_history---------->', dice_roll_history)
            # print('position_history_players---------->', position_history_players)


            if player_1:
                dice_roll_history['player_1'] = player_1
                dice_roll_history['player_2'] = player_2
                dice_roll_history['player_3'] = player_3

                print('dice_roll_history---------->', dice_roll_history)
                # print('position_history_players---------->', position_history_players)
                # print('position_history_players---------->', position_history_players['player_1'])
                if position_history_players['player_1'] + player_1 > grid_size * grid_size:
                    print('no. comes outside of the grid')
                
                    
                else:
                    # dice_roll_history['player_1'] = player_1   # e.g 3
                    position_history_players['player_1'] += player_1   # now at position 3
                    print('position_history_players_when_player_1_played---------->', position_history_players)
                    old_position_player_1 = position_history_players['player_1']
                    if old_position_player_1 in coordinate_history_grid_3:
                        print('coordinate_history_of_player_1----------->>', coordinate_history_grid_3[old_position_player_1])
                        coordinate_player_history['player_1'] = coordinate_history_grid_3[old_position_player_1]
                        print('coordinate_history_player------------>', coordinate_player_history)

                if position_history_players['player_1'] == grid_size*grid_size:
                    # print('position of player 1 winning time-------------->',position_history_players['player_1'])
                    print('position history_at_winning_time-------------->',position_history_players)
                    # print('dice history-------------->',dice_roll_history)
                    print('player_1 wins')
                    old_position_player_1 = position_history_players['player_1']
                    if old_position_player_1 in coordinate_history_grid_3:
                        print('coordinate_history_of_player_1----------->>', coordinate_history_grid_3[old_position_player_1])
                        coordinate_player_history['player_1'] = coordinate_history_grid_3[old_position_player_1]
                        print('coordinate_history_player------------>', coordinate_player_history)
                    return 1


                if position_history_players['player_2'] == position_history_players['player_1']:
                    position_history_players['player_2'] = 0
                    print('position_history_players_when_player_1 cut_player_2---------->', position_history_players)
                    # old_position_player_2 = position_history_players['player_2']
                    # if old_position_player_2 in coordinate_history_grid_2:
                    #     print('coordinate_history_of_player----------->>', coordinate_history_grid_2[old_position_player_1])
                    

                if position_history_players['player_3'] == position_history_players['player_1']:
                    position_history_players['player_3'] = 0
                    print('position_history_players_when_player_1 cut_player_3---------->', position_history_players)

                

                


            if player_2:

                dice_roll_history['player_1'] = player_1
                dice_roll_history['player_2'] = player_2
                dice_roll_history['player_3'] = player_3

                print('dice_roll_history---------->', dice_roll_history)
                # print('position_history_players---------->', position_history_players)

                if position_history_players['player_2'] + player_2 > grid_size * grid_size:
                    print('no. comes outside of the grid')
                    
                else:
                    # dice_roll_history['player_2'] = player_2   # e.g 3
                    position_history_players['player_2'] += player_2   # now at position 3
                    print('position_history_players_when_player_2_played---------->', position_history_players)
                    old_position_player_2 = position_history_players['player_2']
                    if old_position_player_2 in coordinate_history_grid_3:
                        print('coordinate_history_of_player_2----------->>', coordinate_history_grid_3[old_position_player_2])
                        coordinate_player_history['player_2'] = coordinate_history_grid_3[old_position_player_2]
                        print('coordinate_history_player------------>', coordinate_player_history)
                
                

                if position_history_players['player_2'] == grid_size*grid_size:
                    # print('position of player 2 winning time-------------->',position_history_players['player_2'])
                    print('position history when player 2 winning time-------------->',position_history_players)
                    # print('dice history-------------->',dice_roll_history)
                    print('player_2 wins')
                    old_position_player_2 = position_history_players['player_2']
                    if old_position_player_2 in coordinate_history_grid_3:
                        print('coordinate_history_of_player_2----------->>', coordinate_history_grid_3[old_position_player_2])
                        coordinate_player_history['player_2'] = coordinate_history_grid_3[old_position_player_2]
                        print('coordinate_history_player------------>', coordinate_player_history)
                    return 1


                if position_history_players['player_1'] == position_history_players['player_2']:
                    position_history_players['player_1'] = 0
                    print('position history when player 2 cuts player 1-------------->',position_history_players)

                if position_history_players['player_3'] == position_history_players['player_2']:
                    position_history_players['player_3'] = 0
                    print('position history when player 2 cuts player 3-------------->',position_history_players)

                


            if player_3:
                dice_roll_history['player_1'] = player_1
                dice_roll_history['player_2'] = player_2
                dice_roll_history['player_3'] = player_3

                print('dice_roll_history---------->', dice_roll_history)
                # print('position_history_players---------->', position_history_players)
                if position_history_players['player_3'] + player_3 > grid_size * grid_size:
                    print('no. comes outside of the grid')
                    
                else:
                    # dice_roll_history['player_3'] = player_3   # e.g 3
                    position_history_players['player_3'] += player_3   # now at position 3
                    print('position_history_players_when_player_3_played---------->', position_history_players)
                    old_position_player_3 = position_history_players['player_3']
                    if old_position_player_3 in coordinate_history_grid_3:
                        print('coordinate_history_of_player_3----------->>', coordinate_history_grid_3[old_position_player_3])
                        coordinate_player_history['player_3'] = coordinate_history_grid_3[old_position_player_3]
                        print('coordinate_history_player------------>', coordinate_player_history)

                
                
                

                if position_history_players['player_3'] == grid_size*grid_size:
                    # print('position of player 3 winning time-------------->',position_history_players['player_3'])
                    print('position history at the time of winning player 3-------------->',position_history_players)
                    # print('dice history-------------->',dice_roll_history)
                    print('player_3 wins')
                    old_position_player_3 = position_history_players['player_3']
                    if old_position_player_3 in coordinate_history_grid_3:
                        print('coordinate_history_of_player_3----------->>', coordinate_history_grid_3[old_position_player_3])
                        coordinate_player_history['player_3'] = coordinate_history_grid_3[old_position_player_3]
                        print('coordinate_history_player------------>', coordinate_player_history)
                    return 1


                if position_history_players['player_1'] == position_history_players['player_3']:
                    position_history_players['player_1'] = 0

                if position_history_players['player_2'] == position_history_players['player_3']:
                    position_history_players['player_2'] = 0



        if grid_size == 4:

            player_1 = random.randint(1,6)
            print('player_1---------->', player_1)    # 1
            player_2 = random.randint(1,6)
            print('player_2---------->', player_2)   # 1
            player_3 = random.randint(1,6)
            print('player_3---------->', player_3)   # 5
            # print('dice_roll_history---------->', dice_roll_history)
            # print('position_history_players---------->', position_history_players)


            if player_1:
                dice_roll_history['player_1'] = player_1
                dice_roll_history['player_2'] = player_2
                dice_roll_history['player_3'] = player_3

                print('dice_roll_history---------->', dice_roll_history)
                # print('position_history_players---------->', position_history_players)
                # print('position_history_players---------->', position_history_players['player_1'])
                if position_history_players['player_1'] + player_1 > grid_size * grid_size:
                    print('no. comes outside of the grid')
                
                    
                else:
                    # dice_roll_history['player_1'] = player_1   # e.g 3
                    position_history_players['player_1'] += player_1   # now at position 3
                    print('position_history_players_when_player_1_played---------->', position_history_players)
                    old_position_player_1 = position_history_players['player_1']
                    if old_position_player_1 in coordinate_history_grid_4:
                        print('coordinate_history_of_player_1----------->>', coordinate_history_grid_4[old_position_player_1])
                        coordinate_player_history['player_1'] = coordinate_history_grid_4[old_position_player_1]
                        print('coordinate_history_player------------>', coordinate_player_history)

                if position_history_players['player_1'] == grid_size*grid_size:
                    # print('position of player 1 winning time-------------->',position_history_players['player_1'])
                    print('position history_at_winning_time-------------->',position_history_players)
                    # print('dice history-------------->',dice_roll_history)
                    print('player_1 wins')
                    old_position_player_1 = position_history_players['player_1']
                    if old_position_player_1 in coordinate_history_grid_4:
                        print('coordinate_history_of_player_1----------->>', coordinate_history_grid_4[old_position_player_1])
                        coordinate_player_history['player_1'] = coordinate_history_grid_4[old_position_player_1]
                        print('coordinate_history_player------------>', coordinate_player_history)
                    return 1


                if position_history_players['player_2'] == position_history_players['player_1']:
                    position_history_players['player_2'] = 0
                    print('position_history_players_when_player_1 cut_player_2---------->', position_history_players)
                    # old_position_player_2 = position_history_players['player_2']
                    # if old_position_player_2 in coordinate_history_grid_2:
                    #     print('coordinate_history_of_player----------->>', coordinate_history_grid_2[old_position_player_1])
                    

                if position_history_players['player_3'] == position_history_players['player_1']:
                    position_history_players['player_3'] = 0
                    print('position_history_players_when_player_1 cut_player_3---------->', position_history_players)

                

                


            if player_2:

                dice_roll_history['player_1'] = player_1
                dice_roll_history['player_2'] = player_2
                dice_roll_history['player_3'] = player_3

                print('dice_roll_history---------->', dice_roll_history)
                # print('position_history_players---------->', position_history_players)

                if position_history_players['player_2'] + player_2 > grid_size * grid_size:
                    print('no. comes outside of the grid')
                    
                else:
                    # dice_roll_history['player_2'] = player_2   # e.g 3
                    position_history_players['player_2'] += player_2   # now at position 3
                    print('position_history_players_when_player_2_played---------->', position_history_players)
                    old_position_player_2 = position_history_players['player_2']
                    if old_position_player_2 in coordinate_history_grid_4:
                        print('coordinate_history_of_player_2----------->>', coordinate_history_grid_4[old_position_player_2])
                        coordinate_player_history['player_2'] = coordinate_history_grid_4[old_position_player_2]
                        print('coordinate_history_player------------>', coordinate_player_history)
                
                

                if position_history_players['player_2'] == grid_size*grid_size:
                    # print('position of player 2 winning time-------------->',position_history_players['player_2'])
                    print('position history when player 2 winning time-------------->',position_history_players)
                    # print('dice history-------------->',dice_roll_history)
                    print('player_2 wins')
                    old_position_player_2 = position_history_players['player_2']
                    if old_position_player_2 in coordinate_history_grid_4:
                        print('coordinate_history_of_player_2----------->>', coordinate_history_grid_4[old_position_player_2])
                        coordinate_player_history['player_2'] = coordinate_history_grid_4[old_position_player_2]
                        print('coordinate_history_player------------>', coordinate_player_history)
                    return 1


                if position_history_players['player_1'] == position_history_players['player_2']:
                    position_history_players['player_1'] = 0
                    print('position history when player 2 cuts player 1-------------->',position_history_players)

                if position_history_players['player_3'] == position_history_players['player_2']:
                    position_history_players['player_3'] = 0
                    print('position history when player 2 cuts player 3-------------->',position_history_players)

                


            if player_3:
                dice_roll_history['player_1'] = player_1
                dice_roll_history['player_2'] = player_2
                dice_roll_history['player_3'] = player_3

                print('dice_roll_history---------->', dice_roll_history)
                # print('position_history_players---------->', position_history_players)
                if position_history_players['player_3'] + player_3 > grid_size * grid_size:
                    print('no. comes outside of the grid')
                    
                else:
                    # dice_roll_history['player_3'] = player_3   # e.g 3
                    position_history_players['player_3'] += player_3   # now at position 3
                    print('position_history_players_when_player_3_played---------->', position_history_players)
                    old_position_player_3 = position_history_players['player_3']
                    if old_position_player_3 in coordinate_history_grid_4:
                        print('coordinate_history_of_player_3----------->>', coordinate_history_grid_4[old_position_player_3])
                        coordinate_player_history['player_3'] = coordinate_history_grid_4[old_position_player_3]
                        print('coordinate_history_player------------>', coordinate_player_history)

                
                
                

                if position_history_players['player_3'] == grid_size*grid_size:
                    # print('position of player 3 winning time-------------->',position_history_players['player_3'])
                    print('position history at the time of winning player 3-------------->',position_history_players)
                    # print('dice history-------------->',dice_roll_history)
                    print('player_3 wins')
                    old_position_player_3 = position_history_players['player_3']
                    if old_position_player_3 in coordinate_history_grid_4:
                        print('coordinate_history_of_player_3----------->>', coordinate_history_grid_4[old_position_player_3])
                        coordinate_player_history['player_3'] = coordinate_history_grid_4[old_position_player_3]
                        print('coordinate_history_player------------>', coordinate_player_history)
                    return 1


                if position_history_players['player_1'] == position_history_players['player_3']:
                    position_history_players['player_1'] = 0

                if position_history_players['player_2'] == position_history_players['player_3']:
                    position_history_players['player_2'] = 0

                




zig_zag()