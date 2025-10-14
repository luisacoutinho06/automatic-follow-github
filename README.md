# Automatic GitHub Follower Script
`Automatic-follow-github` is a Python automation script that allows you to **automatically follow GitHub users** based on specific actions, such as following users who follow you or other selected criteria. It saves your access token locally in a JSON file, so you don’t have to provide it every time.
I used AI only to improve the layout.

## Features
- Follow users automatically who follow you.
- Save GitHub Access Token and username to a JSON file for reuse.
- Fully configurable: you can separate scripts for setup and actions.
- Simple terminal-based interface.

## Prerequisites
- Python 3.8 or higher
- GitHub account
- Internet connection

## How to get the token
This is the link to access the token
```bash
https://github.com/settings/personal-access-tokens
```

This is the link to the documentation that explains how to do this
```bash
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token
```

The allowed permissions should look exactly like this:
<div align="center">
  <img width="840" height="358" alt="image" src="https://github.com/user-attachments/assets/dd53eb7a-7e56-4b16-b55b-2558d7e37b00" />
</div>

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/automatic-follow-github.git
cd automatic-follow-github
cd src
```

2. Install dependencies:
```bash
py -m pip install -r requirements.txt
```

3. Run the initial setup script to store your GitHub Access Token and username:
```bash
python main.py
```
