def remove():
    while True:
        try:
            delete = input("Delete the movie by Title (to see available commands type 'Help'): ")
            delete = delete.title()
        except IndexError:
            print("You must enter movie!") 
        else:
            break
    a_file = open("movies.txt", "r")

    lines = a_file.readlines()
    flag = 0
    index = -1
    movies = "".join(lines)
    if delete == "Clear":
        ask = input("Clear list Yes/No ?: ")
        ask = f"{ask[0].upper()}{ask[1:len(ask)]}"
        if ask == "Yes":
            m = open("movies.txt", "w+") 
            m = m.readlines 
            del m
        else:
            print("You have not cleared list!")
    elif delete == "Help":
        print("""\n
        *********************************************************************************************
        Delete movie by title, to delete all movies type 'Clear' or type 'List' to see list of movies
        *********************************************************************************************\n""")
        remove()
    else:
        if delete == "List":
            print(f"\n{movies}\n")
            remove()
        else:
            for line in lines:
                index += 1
                if delete in line:
                    flag = 1
                    break 
            a_file.close() 
        
            if flag == 0:
                print(f"{delete} not found!")
            else:
                answer = input(f"Are you sure you want to delete {line} Type: Yes , if you want to delete the movie: ")
                answer = f"{answer[0].upper()}{answer[1:len(answer)]}"
                if answer == "Yes":
                    print(f"{line} movie has been removed from line: {index+1}!")
                    del lines[index]
                else:
                    print(f"You have not removed {line}!")

            
            new_file = open("movies.txt", "w+")

            for line in lines:
                new_file.write(line)

            new_file.close

    
    




