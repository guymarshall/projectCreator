from sys import platform

username = "testuser"

match platform:
    case "linux" | "linux2":
        default_directory = f"/home/{username}"
    case "darwin":
        default_directory = f"/Users/{username}"
    case "win32":
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