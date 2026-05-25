# GitHub Profile Analyzer

A Python application to fetch and analyze GitHub user profiles and repositories with both CLI and Streamlit frontend options.

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

### Option 1: CLI (Command Line Interface)

Run the original CLI version:

```bash
python github.py
```

Then enter a GitHub username when prompted.

### Option 2: Streamlit Frontend (Recommended)

Run the interactive web interface:

```bash
streamlit run app.py
```

This will open a browser window with an interactive dashboard where you can:
- Enter a GitHub username in the sidebar
- View profile statistics (followers, following, repos)
- See language distribution charts
- View top repositories by stars
- Browse recent repositories in a table

## Files

- `github.py` - Original CLI script
- `app.py` - Streamlit web interface
- `.env` - Environment variables (secrets stored here)
- `.gitignore` - Prevents `.env` from being committed
- `requirements.txt` - Python dependencies

## Security

Your GitHub token is stored in `.env` which is:
1. Loaded via `python-dotenv`
2. **NOT** tracked by git (in `.gitignore`)
3. **NOT** committed to version control
4. Safely accessed via `os.getenv("GITHUB_TOKEN")`

## Notes

- The GitHub API has rate limits (60 requests/hour for unauthenticated, 5000/hour for authenticated requests)
- Using a personal access token increases your rate limit significantly
