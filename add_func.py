def add():
    genre = input("Type genre: ") #Action, Comedy, Horror, Romance, SciFi, Fantasy, Mystery
    title = input("Type title: ")
    year = input("Type year: ")
    with open("movies.txt","a") as m:
        m.write(f"{genre}: {title} ({year})\n")
        print(f"You entered \"{title}\" movie into the database!")



def search():
    find = input("Find movie by title: ") 
    with open("movies.txt","r") as m:
        index = 0
        result = 0
        for f in m:
            index += 1
            if find in f:
                result = 1
                break

        if result == 0:
            print(f"{find} not found!")
        else:
            print(f"{f} was found!")



while True:
    start = input("If you want to add a movie type add, or if u want search for a movie type search: ")
    if start == "add":
        add()
        print("If you want to leave this app, type exit !")
    elif start == "search":
        search()
        print("If you want to leave this app, type exit !")
    elif start == "exit":
        print("You have left the application!")
        break
    else:
        print("You entered the wrong command, try again!")
        print("If you want to leave this app, type exit !")
