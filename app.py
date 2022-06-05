from sys import platform

username = "testuser"

if platform == "linux" or platform == "linux2":
    default_directory = f"/home/{username}"
elif platform == "darwin":
    default_directory = f"/Users/{username}"
elif platform == "win32":
    default_directory = f"/Users/{username}"

print(f"Directory is {default_directory}")

# match platform:
#     case "Linux":
#         print("Do Linux commands")
#     case "Mac OS":
#         print("Do Mac OS commands")
#     case "Windows":
#         print("Do Windows commands")

print("DONE")