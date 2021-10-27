def main():
    import os
    import msvcrt
    import random
    version='Alpha'

    #number of rows and columns in playing area. (Maximum suggested size is 10 ). 
    rows_and_columns=15


    #declaring variable for point coordinates, coordinates=(X,Y) starting position random position between 0,0 and playing area-1,playing area-1. Excluding 0,0 as
    #it is default posiition of a player
    def make_point_coordinates(forbidden):
        point_coordinates=[(random.randint(0,(rows_and_columns)-1)),(random.randint(0,(rows_and_columns)-1))]
        if (point_coordinates[0] ==forbidden[0] and point_coordinates[1]==forbidden[1]):
            point_coordinates=make_point_coordinates([0, 0])
        return(point_coordinates)

    #function to make new GLOBAL point coordinates for all functions
    def new_point_coordinates(forbidden):
        global point_coordinates
        point_coordinates=make_point_coordinates(forbidden)
    
    #make point coordinates for the first time
    new_point_coordinates([0, 0])




    #check if position of a point is 0,0. If it is, change it



    #declaring variable for player coordinates, coordinates=(X,Y) starting position 0,0.
    coordinates=[0,0]


    #player's score
    global score
    score=0

    #declaring function for clearing console
    def clear_console():
        os.system('cls')

    #declaring function for writing output into console
    def output_write():
        for x in all_list:
            m=' '.join(x)
            print(m)
        print('\n skóre: '+str(score))

    #tutorial function:
    def tutorial():
        print('Pre pre pohyb hore slač klávesu:\"W\"' + '\nPre pohyb dole slač klávesu:\"A\"' + '\nPre pohyb doprava slač klávesu:\"D\"' + '\nPre pohyb dolava slač klávesu:\"A\"')
        print('Pre návrat do menu slač klávesu:\"M\"')
        input=input=msvcrt.getch().decode("utf-8")
        if input == 'm':
            menu()


    #create a list with all rows and columns filled with black dot
    all_list=[]
    for x in range(0,rows_and_columns):
        m=['⚫' for x in range(0,rows_and_columns)]
        all_list.append(m)
    all_list[0][0]='⚪'
    all_list[point_coordinates[0]][point_coordinates[1]]='🔴'

    #changing coordinates of player based on axis and direction given
    # axis is either 0=x or 1=y. direction is either 1, which means to add 1 or -1 which means to subtract 1
    def mover(axis,direction):
        global score
        if coordinates[axis]+direction > -1 and coordinates[axis]+direction < rows_and_columns:
            #adding empty space to previous position
            all_list[coordinates[0]][coordinates[1]]='⚫'
            #adding player to new position
            coordinates[axis]=coordinates[axis]+direction
            all_list[coordinates[0]][coordinates[1]]='⚪'
            clear_console()
            #if coordinates of the player and point are same, add 1 to score and make new position for point and put it in all_list.
            if coordinates==point_coordinates:
                score+=1
                new_point_coordinates(point_coordinates)
                all_list[point_coordinates[0]][point_coordinates[1]]='🔴'
            output_write()
        

    #this is the main game controller. It takes player's input and starts mover function
    def controller():
        while True:
            input=input=msvcrt.getch().decode("utf-8")
            if input == 'w':
                mover(0,-1)
            elif input == 's':
                mover(0,1)
            elif input == 'a':
                mover(1, -1)
            elif input == 'd':
                mover(1,1)
            elif input =='q':
                clear_console()
                exit()


    #defalt game menu and the first think player sees
    def menu():
        clear_console()
        print('Vitaj v testovacej hre ' +'\nVerzia:', version)
        print('Pre start hry slač klávesu:\"S\"')
        print('Pre pomoc a navody slač klávesu:\"H\"')
        print('Pre ukončenie programu slač klávesu:\"Q\"')
        input=msvcrt.getch().decode("utf-8") 
        if input == 'h':
            clear_console()
            tutorial()
        elif input == 's':
            clear_console()
            output_write()
            controller()
        elif input == 'q':
            clear_console()
            exit()


    #starting program       
    menu()



# if you don't understand, why this section of code should be included in each runnable script, please watch: https://www.youtube.com/watch?v=sugvnHA7ElY
if __name__ == "__main__":
    main()

