# Git Auto Commit Versioning

This Python script automates the process of calculating the next version number based on the last commit message, appending it to a new commit message, and performing a Git commit and push.

## Prerequisites
- Python 3
- Git installed and configured
- A Git repository initialized and set up

## Usage

### Command-Line Usage
1. **Clone or download the repository** to your local machine.
2. **Navigate to the directory** containing the script in your terminal.

### Running the script
To run the script, use the following command:

### Setup
```bash 
 curl https://raw.githubusercontent.com/0xAungkon/pygit-commit-versioning/main/gitautov > ./gitautov; python3 ./gitautov
```

### Examples
```bash
./gitautov -rel -m 'Test4' # Release Push
./gitautov -m 'Test4' # Regular Push
```

