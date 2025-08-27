import sys
import os
import subprocess
import time

def run_command(command):
    """Runs a shell command and returns the output and error."""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result

def is_git_repo():
    """Checks if the current directory is a Git repository."""
    return os.path.isdir('.git')

def get_main_branch_name():
    """Determines whether the main branch is 'main' or 'master'."""
    if run_command("git rev-parse --verify main").returncode == 0:
        return "main"
    elif run_command("git rev-parse --verify master").returncode == 0:
        return "master"
    else:
        # Default to main if neither is found
        return "main"

def handle_errors(result):
    """Analyzes the output of a git command to detect common errors."""
    stderr = result.stderr.lower()
    if "authentication failed" in stderr:
        print("\nError: Authentication failed. Please check your credentials or Personal Access Token.")
        print("You may need to update your remote URL with a valid token:")
        print("  git remote set-url origin https://<TOKEN>@github.com/username/repo.git")
        return True
    if "permission denied (publickey)" in stderr:
        print("\nError: SSH key permission denied. Ensure your SSH key is added to your GitHub account.")
        return True
    if "non-fast-forward" in stderr:
        print("\nError: The remote repository has commits you don't have locally.")
        print("Please pull the changes first. You can use 'git pull --rebase' to avoid a merge commit.")
        return True
    if "no upstream branch" in stderr:
        print("\nError: The current branch has no upstream branch set.")
        branch_name = get_main_branch_name()
        print(f"You can set it by running: git push -u origin {branch_name}")
        return True
    if "large files detected" in stderr:
        print("\nError: Large file detected. GitHub has a limit of 100MB per file.")
        print("Consider using Git LFS (Large File Storage) for large files.")
        return True
    if "conflict" in stderr:
        print("\nError: Merge conflict detected. Please resolve the conflicts manually before proceeding.")
        return True
    if "diverged" in stderr:
        print("\nError: Your branch and the remote branch have diverged.")
        print("You need to reconcile the differences, for example by running 'git pull --rebase'.")
        return True
    return False

def initial_push():
    """Initializes a new repository and pushes it to GitHub."""
    if is_git_repo():
        print("This directory is already a Git repository.")
    else:
        print("Initializing a new Git repository.")
        run_command("git init")

    remote_url = input("Enter the remote repository URL: ")
    commit_message = input("Enter the commit message (defaults to 'Initial commit'): ") or "Initial commit"

    run_command(f"git remote add origin {remote_url}")
    run_command("git add .")
    run_command(f'git commit -m "{commit_message}"')

    branch_name = get_main_branch_name()
    print(f"Pushing to {branch_name}...")
    result = run_command(f"git push -u origin {branch_name}")

    if handle_errors(result):
        return

    print("\nRepository pushed to GitHub successfully!")

def update_push():
    """Pushes updates to an existing repository."""
    commit_message = input("Enter the commit message (defaults to 'Update'): ") or "Update"

    run_command("git add .")
    run_command(f'git commit -m "{commit_message}"')

    branch_name = get_main_branch_name()
    print("Attempting to pull latest changes with rebase...")
    pull_result = run_command(f"git pull --rebase origin {branch_name}")
    if handle_errors(pull_result):
        return

    print(f"Pushing to {branch_name}...")
    push_result = run_command("git push")
    if handle_errors(push_result):
        return

    print("\nUpdates pushed to GitHub successfully!")

def feature_branch_push():
    """Creates a new feature branch and pushes it to GitHub."""
    branch_name = input("Enter the name for the new feature branch: ")
    if not branch_name:
        print("Branch name cannot be empty.")
        return

    commit_message = input("Enter the commit message: ")
    if not commit_message:
        print("Commit message cannot be empty.")
        return

    run_command(f"git checkout -b {branch_name}")
    run_command("git add .")
    run_command(f'git commit -m "{commit_message}"')

    print(f"Pushing new branch '{branch_name}' to GitHub...")
    result = run_command(f"git push -u origin {branch_name}")
    if handle_errors(result):
        return

    print(f"\nBranch '{branch_name}' pushed successfully.")
    print("You can now create a Pull Request on GitHub.")

def main():
    """Main function to display the menu and handle user input."""
    if not is_git_repo():
        print("This is not a Git repository. The only available option is to initialize a new one.")
        initial_push()
        return

    print("\nSelect the type of push you want to perform:")
    print("1. Initial Push (for a new repository on GitHub)")
    print("2. Update (push to an existing branch like main/master)")
    print("3. Feature Branch (create a new branch and push)")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        initial_push()
    elif choice == '2':
        update_push()
    elif choice == '3':
        feature_branch_push()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()