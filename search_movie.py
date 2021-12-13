def search():
    while True:
        try:
            find = input("Find movie (to see available commands type 'Help'): ")
            find = find.title()
        except IndexError:
            print("You must enter movie!") 
        else:
            break
    movies = open("movies.txt","r")
    movies = movies.readlines()
    movies = "".join(movies)
    if find == "List":
        print(f"\n{movies}")
    elif find == "Help":
        print("""\n
        *********************************************************************
        Find movie by title, genre, year or type 'List' to see list of movies
        *********************************************************************\n""")
        search()
    else:
        with open("movies.txt","r") as m:
            index = 0
            result = 0
            for f in m:
                index += 1
                if find in f:
                    result = 1
                    print(f"\n{f}Found on line: {index}")
                
            
            if result == 0:
                print(f"\n{find} not found!\n")


