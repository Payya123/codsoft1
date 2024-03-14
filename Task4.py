from collections import defaultdict
import numpy as np

# Sample user-item ratings
ratings = {
    'Alice': {'A': 5, 'B': 3, 'C': 4, 'D': 4},
    'Bob': {'A': 3, 'B': 1, 'C': 2, 'D': 3},
    'Charlie': {'A': 4, 'B': 2, 'C': 3, 'D': 3},
    'David': {'B': 5, 'C': 4, 'D': 5}
}

# Function to calculate similarity between users
def similarity(user1, user2):
    # Get the common items rated by both users
    common_items = set(ratings[user1].keys()) & set(ratings[user2].keys())
    if not common_items:
        return 0

    # Calculate the cosine similarity between the ratings vectors of the common items
    numerator = sum(ratings[user1][item] * ratings[user2][item] for item in common_items)
    denominator = np.sqrt(sum(ratings[user1][item] ** 2 for item in common_items)) * np.sqrt(sum(ratings[user2][item] ** 2 for item in common_items))
    if denominator == 0:
        return 0
    return numerator / denominator

# Function to get top N recommendations for a user
def get_recommendations(user, n=2):
    similarities = [(other_user, similarity(user, other_user)) for other_user in ratings if other_user != user]
    similarities.sort(key=lambda x: x[1], reverse=True)
    recommendations = defaultdict(float)
    for other_user, sim in similarities:
        for item in ratings[other_user]:
            if item not in ratings[user] or ratings[user][item] == 0:
                recommendations[item] += ratings[other_user][item] * sim
    recommendations = list(recommendations.items())
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return [item for item, _ in recommendations[:n]]

# Example usage
user = 'Alice'
print(f"Recommendations for {user}: {get_recommendations(user)}")

