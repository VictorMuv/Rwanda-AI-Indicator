import requests
import matplotlib.pyplot as plt

def fetch_commit_counts(query):
    url = f'https://api.github.com/search/commits?q={query}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        commit_counts = {}
        for item in data['items']:
            year = item['commit']['author']['date'][:4]
            commit_counts[year] = commit_counts.get(year, 0) + 1
        return commit_counts
    else:
        print('Failed to fetch commit data.')
        return {}

def visualize_commit_trend():
    query = 'location:Rwanda+(AI+OR+ML+OR+"Deep+Learning"+OR+NLP+OR+"Data+Science")'
    commit_counts = fetch_commit_counts(query)

    years = list(commit_counts.keys())
    counts = list(commit_counts.values())

    # Sort the years in chronological order
    years.sort()

    plt.plot(years, counts)
    plt.xlabel('Year')
    plt.ylabel('Commit Counts')
    plt.title('Commit Trends for AI and Data Science Projects in Rwanda')
    plt.xticks(rotation=45)
    plt.show()

# Call the function to visualize the commit trend
visualize_commit_trend()
