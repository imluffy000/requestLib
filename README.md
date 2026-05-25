# GitHub Profile Analyzer

A Python application to fetch and analyze GitHub user profiles and repositories using the GitHub API. This project demonstrates how to securely handle API credentials and interact with external APIs in Python.
 ## Access here :  https://analysemygit.streamlit.app/ ##
## Project Overview

This project was created to learn and practice:
- Making API requests using the `requests` library
- Handling authentication with API tokens
- Data visualization with `matplotlib`
- Environment variable management with `python-dotenv`
- Error handling and exception management
- Working with JSON data structures

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Variables

A `.env` file has been created with your GitHub token. Make sure it contains:

```
GITHUB_TOKEN=your_github_token_here
```

**⚠️ Important:** The `.env` file is added to `.gitignore` to keep your token safe from being committed to version control.

## Usage

Run the CLI script:

```bash
python github.py
```

Enter a GitHub username when prompted to fetch and display:
- User profile information (name, bio, followers, following, etc.)
- Public repository count and account creation date
- Repository statistics and language analysis

## Features

- **Profile Fetching** - Retrieves user profile data from GitHub API
- **Repository Analysis** - Gathers information about all public repositories
- **Language Statistics** - Counts programming languages used across repositories
- **Error Handling** - Gracefully handles API errors, timeouts, and invalid users
- **Secure Credentials** - Token stored safely in `.env` file, not in source code

## Files

- `github.py` - Main CLI script that fetches and displays GitHub profile data
- `.env` - Environment variables file containing GitHub API token (not tracked by git)
- `.gitignore` - Specifies files to exclude from version control (includes `.env`)
- `requirements.txt` - Python package dependencies
- `README.md` - This file

## Security

Your GitHub token is stored in `.env` which is:
1. Loaded via `python-dotenv`
2. **NOT** tracked by git (in `.gitignore`)
3. **NOT** committed to version control
4. Safely accessed via `os.getenv("GITHUB_TOKEN")`

## API Documentation

This project uses the GitHub REST API v3:
- User endpoint: `GET /users/{username}`
- Repositories endpoint: `GET /users/{username}/repos`
- Authentication: Bearer token in Authorization header

## Learning Outcomes

Through this project, you'll understand:
- RESTful API concepts and HTTP requests
- API authentication and token management
- JSON parsing and data manipulation
- Exception handling in Python
- Environment variables and configuration management
- Data visualization with matplotlib

## Prerequisites

- Python 3.7 or higher
- GitHub account with a personal access token
- Internet connection for API requests

## Troubleshooting

**Issue:** "User not found" error
- Solution: Check that the username is spelled correctly

**Issue:** Rate limit exceeded
- Solution: Add your GitHub token to `.env` for higher rate limits (5000/hour instead of 60/hour)

**Issue:** Connection timeout
- Solution: Check your internet connection and try again

## Rate Limits

- **Unauthenticated requests:** 60 requests/hour
- **Authenticated requests:** 5000 requests/hour
- Using a personal access token is strongly recommended for better rate limits
