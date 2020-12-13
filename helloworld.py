def greeting():
    user=input("enter the time for morning  enter am and for evening and night enter pm")
    if user=="am"or user=="AM":
        print("good morning")
    elif user=="pm" or user=="PM":
        print("good evening")
    else:
        print("wrong input just enter am for morning  or pm for night and evening ")

greeting()
