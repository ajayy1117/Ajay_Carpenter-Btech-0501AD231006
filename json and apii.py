# #prog 8

# import json

# # Create list of 3 students
# students = [
#     {"name": "Rahul", "age": 20, "city": "Bhopal", "marks": 85},
#     {"name": "Priya", "age": 21, "city": "Indore", "marks": 92},
#     {"name": "Rohan", "age": 19, "city": "Jabalpur", "marks": 70}
# ]

# # Save data to students.json
# with open("students.json", "w") as f:
#     json.dump(students, f, indent=4)

# # Read file and print students with marks > 75
# try:
#     with open("students.json", "r") as f:
#         data = json.load(f)

#     print("Students with marks > 75:")
#     for student in data:
#         if student["marks"] > 75:
#             print(student)

# except FileNotFoundError:
#     print("Error: students.json file not found.")





# #prob 9

# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# try:
#     response = requests.get(url)

#     # Check status code
#     if response.status_code == 200:
#         users = response.json()

#         print("Users from Gwenborough:\n")

#         for user in users:
#             if user["address"]["city"] == "Gwenborough":
#                 print("Name    :", user["name"])
#                 print("Email   :", user["email"])
#                 print("Phone   :", user["phone"])
#                 print("Company :", user["company"]["name"])
#                 print("-" * 40)
#     else:
#         print("Error: Status Code =", response.status_code)

# except requests.exceptions.ConnectionError:
#     print("Error: Unable to connect to the API.")

# except requests.exceptions.Timeout:
#     print("Error: Request timed out.")

# except requests.exceptions.RequestException as e:
#     print("Request Error:", e)

# except Exception as e:
#     print("Unexpected Error:", e)
