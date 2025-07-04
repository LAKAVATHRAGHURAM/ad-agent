# graph_kg.py
import networkx as nx

# Create a simple knowledge graph
G = nx.DiGraph()

G.add_edge("fun", "Instagram", advice="Use emojis and casual tone")
G.add_edge("professional", "LinkedIn", advice="Be concise and formal")
G.add_edge("witty", "Twitter", advice="Use clever wordplay and hashtags")
G.add_edge("fun", "Facebook", advice="Use lighthearted language with visuals")

def get_justification_from_kg(tone, platform):
    try:
        advice = G[tone][platform]['advice']
        return f"Best practice for '{tone}' tone on {platform}: {advice}."
    except KeyError:
        return f"No specific advice found for '{tone}' tone on {platform}. Use general marketing best practices."

