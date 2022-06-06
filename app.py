from sys import platform
import os

username = "testuser"
project_name = input("Name of project: ").replace(" ", "_")

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

# rust (linux) -> f"cargo new {project_name} && cd {project_name} && code ."
# php (linux) -> f"mkdir {project_name} && cd {project_name} && touch index.php && code ."
# add variable before match called command_to_execute, then append in match statement, then run after match statement