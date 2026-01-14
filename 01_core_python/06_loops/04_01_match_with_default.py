# MATCH WITH DEFAULT CASE

status_code = 404

match status_code:
    case 200:
        print("Success")
    case 400:
        print("Bad Request")
    case 401:
        print("Unauthorized")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status Code")

# Output:
# Not Found
