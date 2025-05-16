import sys
import os

# Ensure the parent directory is in the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import seaborn as sns

from db.models import Journal
from db.engine import SessionLocal

session = SessionLocal()

# Helper: Get all journals
journals = session.query(Journal).all()

# 1. Author Collaboration Network (simple co-authorship count)
def plot_author_collaboration():
    from itertools import combinations
    import networkx as nx

    G = nx.Graph()
    for journal in journals:
        authors = journal.creator if isinstance(journal.creator, list) else []
        for a1, a2 in combinations(authors, 2):
            G.add_edge(a1, a2)
    plt.figure(figsize=(10, 10))
    nx.draw_spring(G, with_labels=True, node_size=50, font_size=8)
    plt.title("Author Collaboration Network")
    plt.tight_layout()
    plt.show()

# 2. Top Mentioned Locations (Bar chart and Word Cloud)
def plot_top_locations():
    locations = [j.location for j in journals if j.location and len(j.location) > 3]
    loc_counts = Counter(locations)
    top_locs = loc_counts.most_common(20)
    df = pd.DataFrame(top_locs, columns=['Location', 'Mentions'])

    plt.figure(figsize=(10, 6))
    sns.barplot(y='Location', x='Mentions', data=df)
    plt.title("Top Mentioned Locations")
    plt.tight_layout()
    plt.show()

    # Word cloud
    text_blob = ' '.join(locations)
    wc = WordCloud(width=800, height=400, background_color='white').generate(text_blob)
    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title("Location Word Cloud")
    plt.tight_layout()
    plt.show()

# 3. Publication Timeline (Time series)
def plot_publication_timeline():
    dates = [j.date_published for j in journals if j.date_published]
    df = pd.DataFrame({'Date': pd.to_datetime(dates)})
    df['Year'] = df['Date'].dt.year
    year_counts = df['Year'].value_counts().sort_index()
    plt.figure(figsize=(10, 5))
    year_counts.plot(marker='o')
    plt.title("Publications Over Time")
    plt.xlabel("Year")
    plt.ylabel("Number of Publications")
    plt.tight_layout()
    plt.show()

# 4. Keyphrase Word Cloud
def plot_keyphrase_wordcloud():
    keyphrases = []
    for j in journals:
        if isinstance(j.keyphrases, list):
            keyphrases.extend(j.keyphrases)
        elif isinstance(j.keyphrases, str):
            keyphrases.extend([k.strip() for k in j.keyphrases.split(',') if k.strip()])
    text_blob = ' '.join(keyphrases)
    wc = WordCloud(width=800, height=400, background_color='white').generate(text_blob)
    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title("Keyphrase Word Cloud")
    plt.tight_layout()
    plt.show()

# 5. Author Contribution Distribution
def plot_author_contributions():
    author_counts = [len(j.creator) if isinstance(j.creator, list) else 1 for j in journals]
    plt.figure(figsize=(8, 6))
    plt.hist(author_counts, bins=range(1, max(author_counts)+2), edgecolor='black')
    plt.title("Number of Authors per Publication")
    plt.xlabel("Number of Authors")
    plt.ylabel("Number of Publications")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("1. Author Collaboration Network")
    plot_author_collaboration()
    print("2. Top Mentioned Locations")
    plot_top_locations()
    print("3. Publication Timeline")
    plot_publication_timeline()
    print("4. Keyphrase Word Cloud")
    plot_keyphrase_wordcloud()
    print("5. Author Contribution Distribution")
    plot_author_contributions()
