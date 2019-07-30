def MenuPrint(Start):
    x=Start*1
    print("-------MENU-------")
    print("----(1)Budget------")
    print("--(2)Travel Style--")
    print("-----(3)Region-----")
    print("")
    return ("LETS GET STARTED")
def Budget():
    print("Budget Options per Person")
    print("Option 1: $0-$1500")
    print("Option 2: $1501-$2500")
    print("Option 3: $2501-$3500")
def TravelStyle():
    print("Your Travel Style Options")
    print("")
    print("Option 1. Adventure Albums: For travelers seeking active and adventure! Take extreme travel to a whole new level!")
    print("")
    print("Option 2. Relax & Refresh: For travelers seeking to clear their mind. Get away from the hustle and bustle of your life by finding relaxation on a beach or secluded in the mountains!")
    print("")
    print("Option 3. Mainstream Madness: For travelers seeking family time while enjoying well known exhibits and landmarks!")
def Region():
    print("Option 1: Europe")
    print("Option 2: Asia")
    print("Option 3: South America")
    print("Option 4: Africa")      

#welcome message
print("Welcome to your travel customization program from Houston! Please follow along with the menu and we will come up with the best week long travel recommendations for you!")
print("")

#traveler's name input
numberofpeople=int(input("Enter the number of people that will be traveling in the group"))
travelerinformation=[]
for i in range (numberofpeople):
        c=input("Please enter traveler's name")
        travelerinformation.append(c)
        i+=1
print("The name(s) of the traveler(s) are", travelerinformation)
print("")

#menu options
Start=int(input("Are you ready to start customizing your surprise travel itinerary to ANYWHERE? Enter 1 for yes and 2 for no."))
print("")
if (Start==1):
    MenuScreen=MenuPrint(Start)
    print(MenuScreen)
    menuSelection=int(input("Enter one of the following menu options (1,2 or 3)"))
    print("")
else:
    print("Visit us another time! Have a good day!")
    
#budget options
if (menuSelection==1):
    Budget()
    BudgetSelection=int(input("Choose your budget option. 1, 2 or 3"))
    if (BudgetSelection==1 or BudgetSelection==2 or BudgetSelection==3):
        print("")
        TravelStyle()
        TravelStyleSelection=int(input("Choose your travel style option. 1, 2 or 3"))
        print("")
        Region()
        RegionSelection=int(input("Choose your region option. 1, 2, 3 or 4"))
        print("")
        print("The options you have chosen are, budget:",BudgetSelection,",travel style:",TravelStyleSelection, ",region:",RegionSelection)
#travel style options
elif (menuSelection==2):
    TravelStyle()
    TravelStyleSelection=int(input("Choose your travel style option. 1, 2 or 3"))
    if (TravelStyleSelection==1 or TravelStyleSelection==2 or TravelStyleSelection==3):
        print("")
        Budget()
        BudgetSelection=int(input("Choose your budget option. 1, 2 or 3"))
        print("")
        Region()
        RegionSelection=int(input("Choose your region option. 1, 2, 3 or 4"))
        print("")
        print("The options you have chosen are, budget:",BudgetSelection,",travel style:",TravelStyleSelection, ",region:",RegionSelection)
#region options 
elif (menuSelection==3):
    Region()
    RegionSelection=int(input("Choose your budget option. 1, 2 or 3"))
    if (RegionSelection==1 or RegionSelection==2 or RegionSelection==3):
        print("")
        Budget()
        BudgetSelection=int(input("Choose your budget option. 1, 2 or 3"))
        print("")
        TravelStyle()
        TravelStyleSelection=int(input("Choose your option. 1, 2, 3 or 4"))
        print("")
        print("The options you have chosen are, budget:",BudgetSelection,",travel style:",TravelStyleSelection, ",region:",RegionSelection)

if (BudgetSelection==1 and RegionSelection==1):#Prague
        with open('pragueMainstream.txt','r') as f:
            f_contents=f.read()
            print(f_contents)


