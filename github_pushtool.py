import sys
import os
import time

def run_command(command):
    print(f"Running: {command}")
    return os.system(command)

def run_command_with_retries(command, retries=3, delay=5):
    for i in range(retries):
        print(f"Running: {command} (Attempt {i+1}/{retries})")
        if os.system(command) == 0:
            return True
        print(f"Command failed. Retrying in {delay} seconds...")
        time.sleep(delay)
    return False

def is_git_repo():
    return os.path.isdir('.git')

def handle_remote(remote_url):
    remotes = os.popen('git remote').read().split()
    if 'origin' in remotes:
        print("Remote 'origin' already exists. Setting URL.")
        if run_command(f"git remote set-url origin {remote_url}") != 0:
            print("Error setting remote URL.")
            sys.exit(1)
    else:
        print("Adding remote 'origin'.")
        if run_command(f"git remote add origin {remote_url}") != 0:
            print("Error adding remote.")
            sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python github_pushtool.py <remote_url> [commit_message]")
        sys.exit(1)

    remote_url = sys.argv[1]
    commit_message = sys.argv[2] if len(sys.argv) > 2 else "Update"

    if not is_git_repo():
        if run_command("git init") != 0:
            print("Error initializing git repository.")
            sys.exit(1)

    handle_remote(remote_url)

    if run_command("git add .") != 0:
        print("Error adding files.")
        # This is probably not a fatal error, so we can continue.

    if run_command(f'git commit -m "{commit_message}"') != 0:
        print("Commit failed. Maybe there are no changes to commit.")

    if not run_command_with_retries("git push -u origin main"):
        print("Push to 'main' failed after multiple attempts. Trying with 'master' branch.")
        if not run_command_with_retries("git push -u origin master"):
            print("Push to 'master' also failed after multiple attempts.")
            sys.exit(1)

    print("\nRepository pushed to GitHub successfully!")

if __name__ == "__main__":
    main()
