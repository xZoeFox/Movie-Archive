def add():
    while True: # for Genre
        try:
            genre = input("Type genre: ") #Action, Comedy, Horror, Romance, SciFi, Fantasy, Mystery
            genre = f"{genre[0].upper()}{genre[1:len(genre)]}"
            genre_list = ["Action", "Comedy", "Horror", "Romance", "Sci-fi", "Fantasy", "Mystery", "Thriller", "Drama", "Crime", "Animated"]
            if genre in genre_list:
                break
            else:
                print("\nGenre must be: Action, Comedy, Horror, Romance, Sci-fi, Fantasy, Mystery, Thriller, Drama, Crime, Animated\n")
        except IndexError:
            print("You must enter genre!")
    while True: # for Title
        try:
            while True:
                title = input("Type title: ")
                title = title.title()
                if title[0] == " ":
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
        except IndexError:
            print("You must enter title!")
    while True: # for Year
        try:
            year = int(input("Type year: "))
        except ValueError:
            print("Year must be number")
        except IndexError:
            print("You must enter year!")
        else:
            if len(str(year)) == 4:
                break
            else:
                print("Wrong year!")
    with open("movies.txt","a") as m:
        m.write(f"{genre}: {title} ({year})\n")
        print(f"You entered \"{title}\" movie into the database!")