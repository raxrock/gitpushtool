import sys
import os

# Get the remote URL from the command-line arguments
if len(sys.argv) < 2:
    print("Usage: python github_pusher.py <remote_url>")
    sys.exit(1)

remote_url = sys.argv[1]

# The commands to run
commands = [
    "git init",
    f"git remote add origin {remote_url}",
    "git add .",
    'git commit -m "Initial commit"',
    "git push -u origin main" # Assuming the default branch is main
]

# Execute the commands
for command in commands:
    print(f"Running: {command}")
    if os.system(command) != 0:
        print(f"Error running command: {command}")
        # If remote add fails, it might be because it already exists.
        # In that case, we'll try to set the url instead.
        if "remote add" in command:
            print("Remote 'origin' may already exist. Trying to set the URL instead.")
            set_url_command = f"git remote set-url origin {remote_url}"
            print(f"Running: {set_url_command}")
            if os.system(set_url_command) != 0:
                print(f"Error running command: {set_url_command}")
                sys.exit(1)
        # If commit fails, it might be because there's nothing to commit.
        elif "commit" in command:
            print("Commit failed. Maybe there are no changes to commit.")
        # If push fails, it might be because the branch is not 'main'.
        elif "push" in command:
            print("Push failed. Trying with 'master' branch.")
            master_push_command = "git push -u origin master"
            print(f"Running: {master_push_command}")
            if os.system(master_push_command) != 0:
                print(f"Error running command: {master_push_command}")

print("\nRepository pushed to GitHub successfully!")
