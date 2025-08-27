# GitHub Pushtool

A Python script to simplify pushing your code to a GitHub repository. This script provides a menu with different push options and helps you handle common Git errors.

## Features

- **Interactive Menu**: Choose from different push workflows.
- **Initial Repository Setup**: Easily initialize a new Git repository and push it to GitHub.
- **Direct Updates**: Push updates directly to your main branch (`main` or `master`).
- **Feature Branches**: Create and push new feature branches, a best practice for collaborative projects.
- **Error Handling**: Detects and provides guidance for common Git errors, such as authentication failures, non-fast-forward pushes, and more.

## Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## Usage

1.  Open your terminal or command prompt.
2.  Navigate to your project directory.
3.  Run the script:

```bash
python github_pushtool.py
```

4.  Follow the on-screen prompts to select the desired push action.

## Workflows

### 1. Initial Push

Use this option when you are setting up a new repository on GitHub. The script will guide you through initializing the repository, adding a remote URL, and making your first push.

### 2. Update

Use this option for making direct updates to your main branch (`main` or `master`). The script will help you pull the latest changes before pushing to avoid common errors.

### 3. Feature Branch

Use this option to create a new branch for your work and push it to GitHub. This is the recommended approach for collaborative projects as it keeps the main branch clean and allows for code reviews through Pull Requests.