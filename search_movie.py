def search():
    while True:
        try:
            find = input("Find movie (if you want to see movie list type: List): ")
            find = f"{find[0].upper()}{find[1:len(find)]}"
        except IndexError:
            print("You must enter movie!") 
        else:
            break
    movies = open("movies.txt","r")
    movies = movies.readlines()
    movies = "".join(movies)
    if find == "List":
        print(f"\n{movies}")
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


