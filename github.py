import requests
import matplotlib.pyplot as plt
from collections import Counter
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get GitHub token from environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# =========================
# Headers
# =========================

headers = {}

if GITHUB_TOKEN:
    headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

# =========================
# Get Username
# =========================

username = input("Enter GitHub username: ").strip()

# =========================
# API URLs
# =========================

profile_url = f"https://api.github.com/users/{username}"

repos_url = f"https://api.github.com/users/{username}/repos"

# =========================
# Fetch Profile Data
# =========================

try:

    profile_response = requests.get(
        profile_url,
        headers=headers,
        timeout=5
    )

    profile_response.raise_for_status()

    profile_data = profile_response.json()

except requests.exceptions.Timeout:

    print("Request timed out")
    exit()

except requests.exceptions.HTTPError:

    print("User not found")
    exit()

except requests.exceptions.RequestException as e:

    print("Error:", e)
    exit()

# =========================
# Fetch Repository Data
# =========================

try:

    repos_response = requests.get(
        repos_url,
        headers=headers,
        timeout=5
    )

    repos_response.raise_for_status()

    repos_data = repos_response.json()

except requests.exceptions.RequestException as e:

    print("Error fetching repositories:", e)
    exit()

# =========================
# Profile Information
# =========================

print("\n==============================")
print("      GITHUB PROFILE")
print("==============================")

print(f"Username          : {profile_data.get('login')}")
print(f"Name              : {profile_data.get('name')}")
print(f"Bio               : {profile_data.get('bio')}")
print(f"Followers         : {profile_data.get('followers')}")
print(f"Following         : {profile_data.get('following')}")
print(f"Public Repositories : {profile_data.get('public_repos')}")
print(f"Profile URL       : {profile_data.get('html_url')}")
print(f"Account Created   : {profile_data.get('created_at')}")

# =========================
# Repository Analysis
# =========================

total_stars = 0
total_forks = 0
languages = []
repo_names = []

for repo in repos_data:

    total_stars += repo["stargazers_count"]

    total_forks += repo["forks_count"]

    repo_names.append(repo["name"])

    if repo["language"]:
        languages.append(repo["language"])

if repos_data:

    most_starred_repo = max(
        repos_data,
        key=lambda repo: repo["stargazers_count"]
    )

    print("\n==============================")
    print("      REPOSITORY ANALYSIS")
    print("==============================")

    print(f"Total Stars       : {total_stars}")
    print(f"Total Forks       : {total_forks}")

    print(
        f"Most Starred Repo : "
        f"{most_starred_repo['name']}"
    )

    print(
        f"Stars on Top Repo : "
        f"{most_starred_repo['stargazers_count']}"
    )

# =========================
# Top 5 Repositories
# =========================

sorted_repos = sorted(
    repos_data,
    key=lambda repo: repo["stargazers_count"],
    reverse=True
)

print("\n==============================")
print("      TOP 5 REPOSITORIES")
print("==============================")

for i, repo in enumerate(sorted_repos[:5], start=1):

    print(
        f"{i}. {repo['name']} "
        f"(⭐ {repo['stargazers_count']})"
    )

# =========================
# Language Analysis
# =========================

language_count = Counter(languages)

print("\n==============================")
print("      LANGUAGE USAGE")
print("==============================")

for language, count in language_count.items():

    print(f"{language}: {count}")

# =========================
# Oldest and Newest Repo
# =========================

if repos_data:

    oldest_repo = min(
        repos_data,
        key=lambda repo: repo["created_at"]
    )

    newest_repo = max(
        repos_data,
        key=lambda repo: repo["created_at"]
    )

    print("\n==============================")
    print("      REPOSITORY AGE")
    print("==============================")

    print(
        f"Oldest Repo : "
        f"{oldest_repo['name']}"
    )

    print(
        f"Created At  : "
        f"{oldest_repo['created_at']}"
    )

    print()

    print(
        f"Newest Repo : "
        f"{newest_repo['name']}"
    )

    print(
        f"Created At  : "
        f"{newest_repo['created_at']}"
    )

# =========================
# Rate Limit Information
# =========================

print("\n==============================")
print("      RATE LIMIT INFO")
print("==============================")

print(
    "Requests Remaining :",
    profile_response.headers.get(
        "X-RateLimit-Remaining"
    )
)

print(
    "Rate Limit Reset   :",
    profile_response.headers.get(
        "X-RateLimit-Reset"
    )
)

# =========================
# Language Pie Chart
# =========================

if language_count:

    plt.figure(figsize=(8, 8))

    plt.pie(
        language_count.values(),
        labels=language_count.keys(),
        autopct="%1.1f%%"
    )

    plt.title(
        f"{username}'s Programming Languages"
    )

    plt.show()

else:

    print("\nNo programming languages found.")

# =========================
# End
# =========================

print("\nAnalysis Completed Successfully!")