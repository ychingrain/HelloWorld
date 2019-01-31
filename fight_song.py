def victory():
    vararray = ['Go,team,go!', 'Defeat your foe.',  'Default your foe.','Simply the best,','Better than the rest.']
    return vararray

def initseq():
    sequence = [0,1,9,0,2,3,4,0,1,9,0,2,3,4,0,1,9,0,1] #9 is a bookmark for skip a line
    return sequence

def sing_fight_song ():
    myarray = victory()
    myseq = initseq()
    
    for i in myseq:
        if i == 9: #this if statement is indicating when to skip a line
            print('')
        else:
            print(myarray[i])

sing_fight_song ()
