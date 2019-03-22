

print("""This is the Battle Operations Calculator Advanced System or B.O.C.A.S. .
      please enter information when prompted to calculate your odds of success
      in any given battle situation

      If you are attacking please enter "A" if defending enter "D" """)

AttackOrDefend = input(" ")

if( AttackOrDefend == "A"):
    print("Defence Mode Initalized")
    print("How many total troops lives does the Axis have in this Battle")
    AxisTroops = input(" ")
    AxisTroops = int(AxisTroops)
    print("How many total troops lives do the Allies have in this Battle")
    AlliedTroops = input(" ")
    AlliedTroops = int(AlliedTroops)
    print("How Many of your troops can only attack with 1")
    AlliedOnes = input(" ")
    AlliedOnes = int(AlliedOnes)
    print("How Many of your troops can only attack with 2 or less")
    AlliedTwos = input(" ")
    AlliedTwos = int(AlliedTwos)
    print("How Many of your troops can only attack with 3  or less")
    AlliedThrees = input(" ")
    AlliedThrees = int(AlliedThrees)
    print("How Many of your troops can only attack with 4 or less")
    AlliedFours = input(" ")
    AlliedFours = int(AlliedFours)
    print("How Many enemy troops can only attack with 1")
    AxisOnes = input(" ")
    AxisOnes = int(AxisOnes)
    print("How Many enemy troops can only attack with 2 or less")
    AxisTwos = input(" ")
    AxisTwos = int(AxisTwos)
    print("How Many of enemy troops can only attack with 3  or less")
    AxisThrees = input(" ")
    AxisThrees = int(AxisThrees)
    print("How Many of enemy troops can only attack with 4 or less")
    AxisFours = input(" ")
    AxisFours = int(AxisFours)

    while True:
        AlliedDamage = (AlliedFours*0.66) + (AlliedThrees*0.5) + (AlliedTwos*0.33) + (AlliedOnes*0.16)
        AxisDamage = (AxisFours*0.66) + (AxisThrees*0.5) + (AxisTwos*0.33) + (AxisOnes*0.16)
        AlliedDamage = int(round(AlliedDamage))
        AxisDamage = int(round(AxisDamage))
        AlliedTroops = AlliedTroops - AxisDamage
        AxisTroops = AxisTroops - AlliedDamage
        if(AlliedTroops <= 0):
            print("The Axis won the battle with "+ str(AxisTroops)+ " left over")
            break;
        if(AxisTroops <= 0):
            print("The Allies won the battle with "+ str(AlliedTroops)+ " left over")
            break;
        for x in range(AlliedDamage):
            if(AxisOnes > 0):
                AxisOnes -= 1
            elif(AxisOnes == 0):
                AxisTwos -= 1
            elif(AxisTwos == 0):
                AxisThrees -= 1
            elif(AxisThrees == 0):
                AxisFours -= 1

        for x in range(AxisDamage):
            if(AlliedOnes > 0):
                AlliedOnes -= 1
            elif(AlliedOnes == 0):
                AlliedTwos -= 1
            elif(AlliedTwos == 0):
                AlliedThrees -= 1
            elif(AlliedThrees == 0):
                AlliedFours -= 1

if( AttackOrDefend == "D"):
    print("Defence Mode Initalized")
    print("How many total troops lives does the Axis have in this Battle")
    AxisTroops = input(" ")
    AxisTroops = int(AxisTroops)
    print("How many total troops lives do the Allies have in this Battle")
    AlliedTroops = input(" ")
    AlliedTroops = int(AlliedTroops)
    print("How Many of your troops can only attack with 1")
    AlliedOnes = input(" ")
    AlliedOnes = int(AlliedOnes)
    print("How Many of your troops can only attack with 2 or less")
    AlliedTwos = input(" ")
    AlliedTwos = int(AlliedTwos)
    print("How Many of your troops can only attack with 3  or less")
    AlliedThrees = input(" ")
    AlliedThrees = int(AlliedThrees)
    print("How Many of your troops can only attack with 4 or less")
    AlliedFours = input(" ")
    AlliedFours = int(AlliedFours)
    print("How Many enemy troops can only attack with 1")
    AxisOnes = input(" ")
    AxisOnes = int(AxisOnes)
    print("How Many enemy troops can only attack with 2 or less")
    AxisTwos = input(" ")
    AxisTwos = int(AxisTwos)
    print("How Many of enemy troops can only attack with 3  or less")
    AxisThrees = input(" ")
    AxisThrees = int(AxisThrees)
    print("How Many of enemy troops can only attack with 4 or less")
    AxisFours = input(" ")
    AxisFours = int(AxisFours)

    while True:
        AlliedDamage = (AlliedFours*0.66) + (AlliedThrees*0.5) + (AlliedTwos*0.33) + (AlliedOnes*0.16)
        AxisDamage = (AxisFours*0.66) + (AxisThrees*0.5) + (AxisTwos*0.33) + (AxisOnes*0.16)
        AlliedDamage = int(round(AlliedDamage))
        AxisDamage = int(round(AxisDamage))
        AlliedTroops = AlliedTroops - AxisDamage
        AxisTroops = AxisTroops - AlliedDamage
        if(AxisTroops <= 0):
            print("The Allies won the battle with "+ str(AlliedTroops)+ " left over")
            break;
        if(AlliedTroops <= 0):
            print("The Axis won the battle with "+ str(AxisTroops)+ " left over")
            break;
        for x in range(AlliedDamage):
            if(AxisOnes > 0):
                AxisOnes -= 1
            elif(AxisOnes == 0):
                AxisTwos -= 1
            elif(AxisTwos == 0):
                AxisThrees -= 1
            elif(AxisThrees == 0):
                AxisFours -= 1

        for x in range(AxisDamage):
            if(AlliedOnes > 0):
                AlliedOnes -= 1
            elif(AlliedOnes == 0):
                AlliedTwos -= 1
            elif(AlliedTwos == 0):
                AlliedThrees -= 1
            elif(AlliedThrees == 0):
                AlliedFours -= 1
                                
                
            
            
        






    

    
