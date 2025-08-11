import random

choice = random.randint(1,6)

user = input("Roll the dice (y/n): ")
if user.lower() == "y":
 print("You Rolled the Dice :"choice)
 if choice == 1:
        print("[     ]")
        print("[  o  ]")
        print("[     ]")
 elif choice == 2:
        print("[o    ]")
        print("[     ]")
        print("[    o]")
 elif choice == 3:
        print("[o    ]")
        print("[  o  ]")
        print("[    o]")
 elif choice == 4:
        print("[o   o]")
        print("[     ]")
        print("[o   o]")
 elif choice == 5:
        print("[o   o]")
        print("[  o  ]")
        print("[o   o]")
 elif choice == 6:
        print("[o   o]")
        print("[o   o]")
        print("[o   o]")
else:
 print("Error")