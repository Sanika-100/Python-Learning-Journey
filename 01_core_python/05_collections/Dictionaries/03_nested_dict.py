# NESTED DICTIONARIES

projects = {
    "project1": {
        "name": "AI Chatbot",
        "status": "Completed"
    },
    "project2": {
        "name": "Data Analyzer",
        "status": "In Progress"
    }
}

print(projects["project2"]["name"])
# Output: Data Analyzer

# Loop nested dictionary
for key, value in projects.items():
    print(key)
    for sub_key, sub_value in value.items():
        print(sub_key, ":", sub_value)

#Output
# Data Analyzer
# project1
# name : AI Chatbot
# status : Completed
# project2
# name : Data Analyzer
# status : In Progress
