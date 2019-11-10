"""
Daniel Bitters 

This script creates a crow-flight distance table for places named "Lebanon" in
the U.S.

"""
def distance_table(file):

    import csv, math

    #Pythagorean Theorem that takes in Coords
    def distance(xpt1, ypt1, xpt2, ypt2):
        dx=xpt2-xpt1 
        dy=ypt2-ypt1 
        dsq=dx**2 + dy**2
        result = math.sqrt(dsq)
        return result

    infile = open(file,'r')
    
    li=[]
    for fields in csv.reader(infile, delimiter=','):
        li.append(fields)
    print("\n")
    print("Distance Table for town named",li[1][2])
    print("----------------------------")
    print("\n")

    #print state initials as a horizontal row
    z=1
    for entry in range(z,len(li)):    
        print('{:^14.6}'.format(li[z][3]),end='')
        z=z+1  
    print("\n")

    state_letters_count=1
    x=1
    y=1
    i=1

    #iterates (n**2+n)/2 times 
    for entry in range(1,int((((len(li)-1)**2)+len(li)-1)/2)+1):
        val=round(distance(float(li[x][12]),float(li[x][13]),float(li[y][12]),float(li[y][13]))/1609,2)

        #tab on each iteration and print state initials
        if(val==0):
            print(li[state_letters_count][3]+i*" "+"{0:^11.2f}".format(val),end='')
            i+=14
            state_letters_count+=1
        else:
           print("{0:^14.2f}".format(val),end='')
        y=y+1 

        #restart iteration when it reaches the end of one list element 
        if(y==len(li)):        
            x=x+1
            y=x
            print("\n")
    print("\n")
        

distance_table('c:/Python projects/Distance Table/Town/Lebanon.csv')

