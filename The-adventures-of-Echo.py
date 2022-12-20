import random
print("""
Welcome to the Adventures of Echo
""")
inputv: str = input("press enter to continue: ")

if inputv == "":
    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

you wake up in a cage your options are:

1 : Go back to sleep 
2 : Cry out loud and wait 
3 : Bite your brother 
4 : Wait     
    """)

    inputv = input("chose a option: ")

    if int(inputv) == 1: 
        print("""

you doze off to sleep
You wake up to someone leting you out of your cage

your options are:
1 : 
        """)

        inputv = input("Chose an option:")
    
    if int(inputv) == 2:
        print("""You hear a faint voice int the distance
        
""")

    if int(inputv) == 3:
        print("""
You decide to wake up your brother by biteing him,
he doesn't like it and bites you too
""")
    
    if int(inputv) == 4: 
        print("""
You are patient and wait 
""")


else :
    print("ERROR")
    print()
        
       