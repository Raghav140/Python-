print("Welcome Warrior")
for i in range(1,3):
    print("*",end="")
print("\n")
#Entering User data 
Nam=str(input("Enter Name:"))
print("Select Wepon: Sword (1), Archer (2),Greatsword (3),Mage (4)") 
Wepc=int(input("Enter Weapon class number:"))
print("********************************")
favf=str(input("Enter Your Fav. food:"))
print("********************************")
age=int(input("Enter Your Age:"))
print("********************************")
#initialize stats
wepatk=int(1) 
chdef=int (1)
specatk= int (1)
#Display 
if age<=20:
    print("Welcome",Nam)
    print (f"Age {age}")
    if Wepc == 1:
        print("Congo for being selected as a Swordersman")
        wepatk+=10
        chdef+=20
        specatk+=40
    elif Wepc == 2:
        print("Congo for being selected as a Archer")
        wepatk+=7
        chdef+=10
        specatk+=30
    elif Wepc == 3:
        print("Congo for being selected as a Greatswordsman")
        wepatk+=15
        chdef+=30
        specatk+=50
    elif Wepc == 4:
        print("Congo for being selected as a Mage")
print("*******************************************")
stat=str(input("Do you want to see your stats:"))
if stat == "yes":
     print("User Your stats are Below")
     print("***************************************")
     print("Weapon Dmg:",wepatk)
     print("Character Defense:",chdef)
     print("Special Attack Dmg:",specatk)
elif age>=20:
     print("**************************************")
     print("too big for gaming")
     print("Here your normie stats")
     print("Attack:",wepatk)
     print("Defense:",chdef)
     print("Normie attack dmg:",specatk)
else:
   print("ok bye")
