import streamlit as st
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
# Streamlit Configuration
# =========================
st.set_page_config(page_title="GitHub Profile Analyzer", layout="wide")

st.title("🐙 GitHub Profile Analyzer")
st.markdown("---")

# =========================
# Sidebar Inputs
# =========================
with st.sidebar:
    st.header("Settings")
    username = st.text_input("Enter GitHub username:", placeholder="e.g., torvalds")

# =========================
# Main Application
# =========================
if username:
    try:
        # Prepare headers
        headers = {}
        if GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

        # API URLs
        profile_url = f"https://api.github.com/users/{username}"
        repos_url = f"https://api.github.com/users/{username}/repos"

        # Fetch Profile Data
        profile_response = requests.get(profile_url, headers=headers, timeout=5)
        profile_response.raise_for_status()
        profile_data = profile_response.json()

        # Fetch Repository Data
        repos_response = requests.get(repos_url, headers=headers, timeout=5)
        repos_response.raise_for_status()
        repos_data = repos_response.json()

        # =========================
        # Display Profile Information
        # =========================
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Followers", profile_data.get('followers', 0))
        with col2:
            st.metric("Following", profile_data.get('following', 0))
        with col3:
            st.metric("Public Repos", profile_data.get('public_repos', 0))

        # Profile details
        st.subheader("Profile Information")
        profile_col1, profile_col2 = st.columns(2)

        with profile_col1:
            st.write(f"**Username:** {profile_data.get('login')}")
            st.write(f"**Name:** {profile_data.get('name', 'N/A')}")
            st.write(f"**Bio:** {profile_data.get('bio', 'N/A')}")

        with profile_col2:
            st.write(f"**Profile URL:** [View Profile]({profile_data.get('html_url')})")
            st.write(f"**Account Created:** {profile_data.get('created_at', 'N/A')[:10]}")
            st.write(f"**Location:** {profile_data.get('location', 'N/A')}")

        # =========================
        # Display Repository Information
        # =========================
        if repos_data:
            st.subheader("📊 Repository Statistics")

            # Language statistics
            languages = Counter()
            stars = []
            repo_names = []

            for repo in repos_data:
                if repo.get('language'):
                    languages[repo['language']] += 1
                stars.append(repo.get('stargazers_count', 0))
                repo_names.append(repo.get('name'))

            # Create columns for charts
            chart_col1, chart_col2 = st.columns(2)

            with chart_col1:
                if languages:
                    st.write("**Languages Used:**")
                    fig, ax = plt.subplots()
                    ax.bar(languages.keys(), languages.values(), color='steelblue')
                    ax.set_xlabel("Language")
                    ax.set_ylabel("Count")
                    plt.xticks(rotation=45, ha='right')
                    st.pyplot(fig)

            with chart_col2:
                if stars:
                    st.write("**Top Repositories by Stars:**")
                    top_repos = sorted(zip(repo_names, stars), key=lambda x: x[1], reverse=True)[:10]
                    repo_names_top = [r[0] for r in top_repos]
                    stars_top = [r[1] for r in top_repos]
                    fig, ax = plt.subplots()
                    ax.barh(repo_names_top, stars_top, color='coral')
                    ax.set_xlabel("Stars")
                    plt.tight_layout()
                    st.pyplot(fig)

            # Display repository table
            st.write("**Recent Repositories:**")
            repo_display = []
            for repo in repos_data[:10]:
                repo_display.append({
                    "Name": repo['name'],
                    "Stars": repo.get('stargazers_count', 0),
                    "Language": repo.get('language', 'N/A'),
                    "URL": repo.get('html_url', 'N/A')
                })

            st.dataframe(repo_display, use_container_width=True)

    except requests.exceptions.Timeout:
        st.error("❌ Request timed out. Please try again.")
    except requests.exceptions.HTTPError:
        st.error(f"❌ User '{username}' not found. Please check the username.")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error: {str(e)}")
else:
    st.info("👈 Enter a GitHub username in the sidebar to get started!")

# Footer
st.markdown("---")
st.caption("GitHub Profile Analyzer - Powered by Streamlit")
