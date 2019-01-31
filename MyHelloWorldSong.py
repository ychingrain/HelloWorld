def victory():
    vararray = ['Hello World!', 'Here is my song.',  'Let's all learn to program.','Because it's kinda fun.,','Hello World is our jam.']
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
