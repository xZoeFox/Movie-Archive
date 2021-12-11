from add_movie import add
from search_movie import search
from remove_movie import remove 


while True:
    start = input("If you want to add a movie type add, if you want search for a movie type search, or if you want delete movie type remove: ")
    if start == "add":
        add()
        print("If you want to leave this app, type exit !")
    elif start == "search":
        search()
        print("If you want to leave this app, type exit !")
    elif start == "remove":
        remove()
        print("If you want to leave this app, type exit !")
    elif start == "exit":
        print("You have left the application!")
        break
    else:
        print("You entered the wrong command, try again!")
        print("If you want to leave this app, type exit !")

