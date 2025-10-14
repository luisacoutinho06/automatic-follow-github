# Automatic GitHub Follower Script
`automatic-follow-github` is a Python automation script that allows you to **automatically follow GitHub users** based on specific actions, such as following users who follow you or other selected criteria. It saves your access token locally in a JSON file, so you don’t have to provide it every time.

## Features
- Follow users automatically who follow you.
- Save GitHub Access Token and username to a JSON file for reuse.
- Fully configurable: you can separate scripts for setup and actions.
- Simple terminal-based interface.

## Prerequisites
- Python 3.8 or higher
- GitHub account
- Internet connection

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/automatic-follow-github.git
cd automatic-follow-github
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the initial setup script to store your GitHub Access Token and username:
```bash
python main.py
```
