"""Robert Prattico, 1630733
Friday, May 18
R. Vincent, instructor
Final Project

The Ultimate Team Builder

Description: FIFA Ultimate Team is a popular video game module from the FIFA video game
series. In this module, users can create their own Soccer teams of real life players and use
them in games against other users’ own teams. This program generates the best or worst team of
players based on the parameters inputted by the user. The category of parameters users can build
their team from are geography (the country, league or team in which a player plays), nationality,
physical attributes, and technical skills."""


import csv

#Files: these are the files that contain the data necessary to run the program

file1=open('Sports positions.csv', 'r')
readfile1=csv.reader(file1)

file2= open('FIFA16ratings.csv', 'r')
readfile2=csv.reader(file2)

file3=open("countries.txt", "r")
readfile3=file3.read()

file4=open("leagues.txt","r")
readfile4=file4.read()

file5=open("teams.txt", "r")
readfile5=file5.read()

file6=open("attributes.txt","r")
#this dictionary is used to make sure that the attribute chosen by the user exists in the database
line = file6.readline()
cnt = 7
attributedict={}
while line:
    cnt+=1
    attributedict[line.strip()]=cnt
    line = file6.readline()

#Functions
#
def sportposition(file, sport):#function to return the positions of the sport
    global positionlist #this variable is used throughout the program
    positionlist=[]
    y=x.index(sport)
    for row in file:
        if row[y]=='':
            continue
        else:
            positionlist.append(row[y])
    return positionlist


def countrysearch(file, category, R):#this functions shrinks the data to players that fit the desired category
    countrymen=[]
    for row in file:
        if category==row[R]:
            countrymen.append(row)
    else:
        return countrymen

def keywithmaxval(d):
     #create a list of the dict's keys and values, return the key with the max value 
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def keywithminval(d):
     #create a list of the dict's keys and values return the key with the min value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(min(v))]

#5. Filling the Gaps

def substitute(i):
    #if a position is missing, ask for another
    print("\n")
    newi=input("You are missing a {}.Replace with:".format(i))
    return newi

def FindBestPlayer(countrymen, team, i, Q):
    player= None #no player initially
    while player == None:
        positionratings={}
        rowdict={}
        for row in countrymen:
            if row[4]==i and row[3] not in team:
                positionratings[row[3]]=row[Q] #append the player with his ratings
                rowdict[row[3]]=countrymen.index(row)#appnd the player with his row index
        if not positionratings: #if the dict is empty, this means there are no players in that position; find another
            i=substitute(i)
        else:
            player=keywithmaxval(positionratings)
            out=rowdict[player]
            countrymen.remove(countrymen[out])#if the player has already chosen to be on the team, remove him so that he is not selected again
    return player

def FindWorstPlayer(countrymen, team, i, Q):
    #repeat of FindBestPlayer but returns min value(ie worst player)
    player= None
    while player == None:
        positionratings={}
        rowdict={}
        for row in countrymen:
            if row[4]==i and row[3] not in team:
                positionratings[row[3]]=row[Q]
                rowdict[row[3]]=countrymen.index(row)
        if not positionratings:
            i=substitute(i)
        else:
            player=keywithminval(positionratings)
            out=rowdict[player]
            countrymen.remove(countrymen[out])
    return player           
        
def BestTeamBuilder(countrymen, Q=0):
    #runs FindBestPlayer for every position of the sport
    team=[]
    for i in positionlist:
        player=FindBestPlayer(countrymen, team, i, Q)
        team.append(player)
    return team

def WorstTeamBuilder(countrymen, Q=0):
    #runs FindWorstPlayer for every position of the sport
    team=[]
    for i in positionlist:
        player=FindWorstPlayer(countrymen, team, i, Q)
        team.append(player)
    return team

#4. The Physical Attribute

def attributebuilder(refine, category):
    team=[]
    high=["oldest","tallest","heaviest","fastest","stronger"]
    low=["youngest","shortest","lightest","slowest","weaker"]
    B=attributedict[category]
    #the following are prompts to specify what extreme of the attribute the user wants
    if B==8:
        print("\n")
        level=input("Would you like the oldest players or youngest players?")
    elif B==9:
        print("\n")
        level=input("Would you like the tallest players or shortest players?")
    elif B==10:
        print("\n")
        level=input("Would you like the heaviest players or lightest players?")
    elif B==11:
        print("\n")
        level=input("Would you like the fastest players or slowest players?")
    else:
        print("\n")
        level=input("Would you like the players who are stronger or weaker in this attribute?")
    if level in high:
        #BestTeamBuilder is run, row B is used instead of row Q
        team=BestTeamBuilder(refine, B)
    elif level in low:
        #WorstTeamBuilder is run, row B is used instead of row Q
        team=WorstTeamBuilder(refine, B)
    return team

def morefilters(refine):
    print("\n")
    more= input("Would you like to add a physical attribute?")#executes task based on whether or not user wants a physical attribute
    if more=="yes":
        print("\n")
        qualist=input("Would you like to see the attribute directory?")
        while qualist=="yes":
            print("\n", "Attribute Directory:", "\n", open("attributes.txt","r").read(), "\n")
            qualist=input("Would you like to see the attribute directory again?")
        if qualist=="no":
            print("\n")
            addattribute=input("Add a physical attribute:")
            while addattribute not in open("attributes.txt","r").read():#if the attribute does not exist
                print("\n")
                addattribute=input("Sorry, that attribute is not in the directory. Add a physical attribute:") 
            refined=attributebuilder(refine, addattribute)
            return refined
    else:#if the user does not want a physical attribute
        print("\n")
        quality=input("Would you like to build the best or worst team with this category?")
        if quality=="best":
            return BestTeamBuilder(refine)
        elif quality=="worst":
            return WorstTeamBuilder(refine)

#Procedure
#1. Introduction

print("Welcome to the Ultimate Team Builder!")
print("Build your sports team from any criteria and attributes you want!\n")
print("Here are the sports you can build your team from:\n")
for i in range(6):
    x=readfile1.__next__()
    print(x)
    print("\n")
    break
        
#2. The Template

sport=str(input("Select a sport:"))
synonyms=('sport 1', 'soccer', 'Soccer', 'European Football', 'soccer ', 'calcio')#removing case sensitivity
if sport in synonyms:
    sport="Soccer"
    print("\n")
    print("Here are the positions of the sport:")
    positionlist= sportposition(readfile1, sport)
    for a in positionlist:#print list of sport positions
        print(a)
    print("\nFormation: 4-3-3\n")
else:
    while sport not in synonyms:
        sport=input("There is not enough data for this sport. Select another sport:")#redirect user to another sport


#3. The Geographical Theme

direct=input("Select a geographical theme. Do you wish to see the directory?")
print("\n")
while direct=="yes":
    print("Country directory:\n")
    print(readfile3, "\n")
    print("League directory:\n")
    print(readfile4, "\n")
    print("Team directory:\n")
    print(readfile5, "\n")
    direct=input("Do you wish to see the directory again?")
while direct=="no":
    category=input("Select a geographical theme:")
    if category in readfile3: #if the theme is a country
        refine=countrysearch(readfile2, category, 7)
        FinalXI=morefilters(refine)
        break
    elif category in readfile4:#if the theme is a league
        refine=countrysearch(readfile2, category, 6)
        FinalXI=morefilters(refine)
        break
    elif category in readfile5:#if the theme is a team
        refine=countrysearch(readfile2, category, 5)
        FinalXI=morefilters(refine)
        break
    else:#if the theme does not exist
        direct=input("That geographical theme is not in the directory. Do you wish to see the directory again?")
        print("\n")
        while direct=="yes":
            print("Country directory:\n")
            print(readfile3, "\n")
            print("League directory:\n")
            print(readfile4, "\n")
            print("Team directory:\n")
            print(readfile5, "\n")
            direct=input("Do you wish to see the directory again?")

#Steps 4 and 5 are located in the Functions
#6. The Final XI

print("\nYour team is:\n")
for teammember in FinalXI:#print the final team
    print(teammember)
    



       
        
    



  

    
