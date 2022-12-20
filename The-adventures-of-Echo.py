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

You doze off to sleep
You wake up to someone leting you out of your cage

your options are:
1 : Leave the cage  
2 : Stay in the cage 
        """)

        inputv = input("Chose an option:")

        if int(inputv) == 1 :
                print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You see nothing then suddenly a bright flash of light.
Once your eyes adjust to the light you can see again 
And you walk out a door to the what appears to be the living room.
You then see your owner putting your leash on.

""")
        inputv = input(":")
        if inputv == "":
                print("""
You both walk outside and you see a squirrel.
You bolt off after it pulling the leash out of your owners hands and hear them shout out ECHO!
You chase the squirrel for what feels like a coupple seconds.
Then you come to realize you dont know were you are or how long you have been chasseing it. 
                
                """)
        if 1 == 1 :
            print(""" 
            To be continued...
            
            """)

    if inputv == "2" :
        print("""
You hear a faint voice in the distance
    
""")

    if inputv == "3" :
        print("""
You decide to wake up your brother by bitting him,
he doesn't like it and bites you too
""")
    
    if inputv == "4" :
        print("""
You are patient and wait 
""")


else :
    print("ERROR")
    print()
        
       