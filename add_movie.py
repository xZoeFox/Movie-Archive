def add():
    while True: # for Genre
        print("Action, Comedy, Horror, Romance, SciFi, Fantasy, Mystery")
        genre = input("Type genre: ") #Action, Comedy, Horror, Romance, SciFi, Fantasy, Mystery
        genre = f"{genre[0].upper()}{genre[1:len(genre)]}"
        if genre == "Action":
            break
        elif genre == "Comedy":
            break
        elif genre == "Horror":
            break
        elif genre == "Romance": 
            break
        elif genre == "SciFi": 
            break
        elif genre == "Fantasy":
            break
        elif genre == "Mystery":
            break
        else:
            print("Genre must be: Action, Comedy, Horror, Romance, SciFi, Fantasy, Mystery")
    while True: # for Title
        while True:
            title = input("Type title: ")
            title = f"{title[0].upper()}{title[1:len(title)]}"
            if title == "":
                print("You must enter title!")
            elif title[0] == " ":
                print("Warning: Blank Space!")
            else:
                break
        with open("movies.txt","r") as m:   
            result = 0
            for f in m:
                if title in f:
                    result = 1
                    break
            if len(title) <= 50:     
                if result == 0:
                    break
                else:
                    print(f"'{title}' already exists = {f}")
            else:
                print("Too long for Title!") 
    while True: # for Year
        try:
            year = int(input("Type year: "))
        except ValueError:
            print("Year must be number")
        else:
            if len(str(year)) == 4:
                break
            else:
                print("Wrong year!")
    with open("movies.txt","a") as m:
        m.write(f"{genre}: {title} ({year})\n")
        print(f"You entered \"{title}\" movie into the database!")