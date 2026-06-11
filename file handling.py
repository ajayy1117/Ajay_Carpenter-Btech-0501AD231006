# #prob 6
# # Create report.txt and write student data
# with open("report.txt", "w") as f:
#     f.write("Rahul-85\n")
#     f.write("Priya-90\n")
#     f.write("Rohan-78\n")
#     f.write("Sneha-92\n")
#     f.write("Amit-65\n")

# try:
#     # Read file
#     with open("report.txt", "r") as f:
#         print("Students with marks > 80:")

#         for line in f:
#             name, marks = line.strip().split("-")

#             if int(marks) > 80:
#                 print(name, "-", marks)

# except FileNotFoundError:
#     print("Error: report.txt file not found.")

# finally:
#     print("File operation completed.")


# #prob 7
# import os

# # Create employees.txt with 3 employees
# with open("employees.txt", "w") as f:
#     f.write("Rahul\n")
#     f.write("Priya\n")
#     f.write("Rohan\n")

# # Read and print file
# print("Initial Employees:")
# with open("employees.txt", "r") as f:
#     print(f.read())

# # Append 2 more employees
# with open("employees.txt", "a") as f:
#     f.write("Sneha\n")
#     f.write("Amit\n")

# # Read updated file
# print("Updated Employees:")
# with open("employees.txt", "r") as f:
#     print(f.read())

# # Delete the file
# os.remove("employees.txt")

# # Verify deletion
# if not os.path.exists("employees.txt"):
#     print("File deleted successfully.")
# else:
#     print("File still exists.")