# MATCH WITH MULTIPLE VALUES

day_type = "Saturday"

match day_type:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Invalid Day")

# Output:
# Weekend
