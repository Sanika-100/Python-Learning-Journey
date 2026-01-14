# BASIC MATCH STATEMENT

option = 3

match option:
    case 1:
        print("Create File")
    case 2:
        print("Read File")
    case 3:
        print("Update File")
    case 4:
        print("Delete File")
    case _:
        print("Invalid Option")

# Output:
# Update File