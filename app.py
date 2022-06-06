from sys import platform
import os

username = "testuser"
project_name = input("Name of project: ").replace(" ", "_")
programming_language = input("Programming language: ").lower()

match platform:
    case "linux" | "linux2":
        user_path = f"/home/{username}"
        os.system("ls -lh")
    case "darwin":
        user_path = f"/Users/{username}"
        os.system("ls -lh")
    case "win32":
        user_path = f"/Users/{username}"
        os.system("dir")

full_path = f"{user_path}/{project_name}"

print(f"Directory is {user_path}")

print("DONE")

# rust (linux) -> f"cargo new {project_name} && cd {project_name} && code ."
# php (linux) -> f"mkdir {project_name} && cd {project_name} && touch index.php && code ."
# add variable before match called command_to_execute, then append in match statement, then run after match statement