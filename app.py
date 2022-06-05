from sys import platform
import os

username = "testuser"

match platform:
    case "linux" | "linux2":
        default_directory = f"/home/{username}"
        os.system("ls -lh")
    case "darwin":
        default_directory = f"/Users/{username}"
        os.system("ls -lh")
    case "win32":
        default_directory = f"/Users/{username}"
        os.system("dir")

print(f"Directory is {default_directory}")

print("DONE")