from sys import platform
import os

username = "testuser"
project_name = input("Name of project: ").replace(" ", "_")
programming_language = input("Programming language: ").lower()

match platform:
    case "linux" | "linux2":
        user_path = f"/home/{username}"
        new_file_command = "touch"
        os.system("ls -lh")
    case "darwin":
        user_path = f"/Users/{username}"
        new_file_command = "touch"
        os.system("ls -lh")
    case "win32":
        user_path = f"/Users/{username}"
        new_file_command = "type nul >"
        os.system("dir")

full_path = f"{user_path}/{project_name}"

commands = {
    "rust": f"cargo new {project_name} && cd {project_name} && code .",
    "php": f"mkdir {project_name} && cd {project_name} && {new_file_command} index.php && code .",
    "python": f"mkdir {project_name} && cd {project_name} && {new_file_command} app.py && code ."
}

chosen_command = commands.get(programming_language)

final_command_to_run = f"cd {user_path} && {chosen_command}"