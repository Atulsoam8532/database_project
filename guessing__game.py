import random as r

def user():
    print("""
>-----------------------------------<
>           1. User                 <
>           2. Developer            <
>-----------------------------------<
        """ )
    print(
        "==================================================================================================================================================="
    )

    u = int(input("Are you a user or Developer[1,2]"))
    print(
        "==================================================================================================================================================="
    )
    if u == 1:
        start()
    elif u == 2:
        dev()
        user()



li = ["laptop","books","engineers","question","clue"]
let = r.choice(li)




h = list("-"*len(let))
def enterten():
    print(
"""
|----------------------------------|
|we will not consider your choice  |
|----------------------------------|
|you will be getting a random word |
|----------------------------------|"""""
    )
    print()
    print(f"""
|----------------------------------|
|       guess this word            |
|       {"- "*len(let)}            |
|----------------------------------|"""

    )
    print()
    print(f"According to hyphen you get to know that your word length is {len(let)}")
    print()
    print("you only have 10 chance but don't worry i will give you 11")


def inpu():
    cou = 11
    while cou>0:

        i = input("Enter your silly word")
        if i == let:
            print("you did a very good job")
            break
        else:

            coun = 0
            m = []
            for i in i:
                if i in list(let):
                    coun+=1
                    m.append(i)
                elif i not in list(let):
                    cou -=1

            print(f"Only {coun} letters match and matching latter is (Me nhi dikhaunga)\nI will not show ")
            print()
            print("If you want to see say [Yes/NO]")
            print()
            b = input("put it here").lower()
            print()
            if b == "yes":
                if coun > 0:
                    print(f"you will not be able to guess {list(m)}")
                    w = let.index(i)
                    del h[w]
                    h.insert(w, i)
                    print("".join(h))
                    print()
                else:
                    print("No matching Idiot")
                    print()
            elif b == "no":
                print()
                print(f"Go away idiots {list(m)}")
                continue
            else:
                print("you idiot")
                continue
            print(f"For you kind information only{cou} chance left")
            if cou == 0:
                print("you lost")
def clue():
    if len(let)== 4:
        print("CLUE-","I am not happy to give you")
    elif len(let) == 5:
        print("CLUE-","without this you can not pass your exam")
    elif len(let) == 8:
        print("Some time you feel it hard")
    elif len(let) == 9:
        print("CLUE-","you are almost there")
    elif len(let) == 6:
        print("CLUE-","because of this you are able to study")


print()
def start():

    print("""
    >__________________________<
    >       Are you ready      <
    >__________________________<
    """
          )
    print(
        "==================================================================================================================================================="
    )
    gue = input("Guess the lenhgth of the word[1,2,3,4,5,6,7,8,9,10]:- ")
    print(
        "==================================================================================================================================================="
    )
    if gue == "6" or gue == "5" or gue == "7" or gue == "8" or gue == "9" or gue == "10" or gue == "4":
        enterten()
        print()
        clue()
        print()
        inpu()

    elif gue >"10":
        print(f"don't be excite we have only {len(li)}words")
        print()
        print(f"and the size of word is more than 5")
        enterten()
        clue()
        inpu()
    else:
        print("[Error]- idiot be in your sence('')")
def dev():
    us = "Atul8"
    pa = "Atul@85"
    u = input("Enter your Username")
    p = input("Enter your password")
    if u == us and p == pa:
        print(f"Welcome {us} ")
        c = input("You want to add some words in game[yes,no]").lower()
        if c == "yes":
            q = int(input("How much word you want to add"))
            for i in range(q):
                ch = input("Enter the word")
                li.append(ch)
            print("Added successfully")
            cl = input("Enter the clue")
            che()

        elif c == "no":
            print(li)
    else:
        print("invalid entry")
        err()

def err():
    d = input("You want to login or not[Yes.no]").lower()
    if d == "yes":
        dev()
    elif d == "no":
        start()
    else:
        print("invalid input")
        err()
def che():
    s = input("You want to see your words[yes,no]").lower()
    if s == "yes":
        print(li)

    elif s == "no":
        print("Thank you")

    else:
        print("Invalid input")
        che()
def main():
    user()
    start()


main()