#Name: Zavier DePillo
#Email: depillzj@mail.uc.edu
#Assignment Title: Assignment 05
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: working with dictionaries and lists
#Citations:
#Anything else that's relevant:
from functionPackage.function import *

myTeams = {'Columbus':'Ohio State', 'Bloomington':'Indiana' , 'West Lafayette':'Purdue', 'Iowa City':'Iowa', 
'Orange City':'Northwestern', 'State College':'Penn State', 'Madison':'Wisconsin', 'Twin Cities':'Minnesota', 'New Brunswick':'Rutgers', 'Lincoln':'Nebraska', 'Ann Arbor':'Michigan', 'East Lansing':'Michigan State'}

print_teams(myTeams)

myTeamsList = sorted(list(myTeams.values()))
print(myTeamsList)
    
try:
    print_teams(myTeamsList)
except AttributeError:
    print("something went wrong")
    
inputSchool = input("Name of a Big 10 school:", )

if inputSchool in myTeamsList:
    print("User input is found in the list")
else: 
    print("User input is NOT found in the list")
    
inputSchool = input("Name of a Big 10 school:", )

if inputSchool in myTeamsList:
    print("User input is found in the list")
else: 
    print("User input is NOT found in the list")