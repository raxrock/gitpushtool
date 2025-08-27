# GitHub Push Tool


A Python script to simplify pushing your code to a GitHub repository. This script can be used to initialize a new repository or to push changes to an existing one.

## Features

- **Initializes a new Git repository** if one doesn't already exist.
- **Adds or updates the remote URL** for 'origin'.
- **Adds all files**, commits them, and pushes to GitHub.
- **Custom commit messages** can be provided as an argument.
- **Retries pushing** to the 'main' and 'master' branches if the initial push fails.

## Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## Usage

1.  Open your terminal or command prompt.
2.  Navigate to your project directory.
3.  Run the script with the following command:

```bash
python github_pusher.py <remote_url> "[your_commit_message]"
```

### Arguments

-   `<remote_url>`: **(Required)** The URL of your GitHub repository (e.g., `https://github.com/your-username/your-repo.git`).
-   `"[your_commit_message]"`: **(Optional)** The commit message to use. If not provided, it will default to "Update".

## Examples

### Initial Push

To initialize a new repository and push for the first time:

```bash
python github_pusher.py https://github.com/your-username/your-repo.git "Initial commit"
```

### Subsequent Pushes

To push changes to an existing repository with a custom commit message:

```bash
python github_pusher.py https://github.com/your-username/your-repo.git "Add new feature"
```

To push changes with the default commit message ("Update"):

```bash
python github_pusher.py https://github.com/your-username/your-repo.git
```
