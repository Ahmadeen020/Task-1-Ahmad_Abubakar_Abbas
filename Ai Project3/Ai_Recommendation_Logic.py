# AI Recommendation System

# Available items and their categories
items = {
    "Python for Beginners": ["programming", "python", "technology"],
    "Cybersecurity Basics": ["cybersecurity", "security", "technology"],
    "Machine Learning Fundamentals": ["ai", "machine learning", "technology"],
    "UI/UX Design Guide": ["design", "ui/ux", "creativity"],
    "Blockchain Essentials": ["blockchain", "crypto", "technology"],
    "Data Science Handbook": ["data science", "analytics", "technology"]
}

print("=== AI Recommendation System ===")

# Get user interests
user_input = input(
    "Enter your interests separated by commas:\n"
).lower()

user_preferences = [
    interest.strip()
    for interest in user_input.split(",")
]

recommendations = []

# Compare user interests with item categories
for item, categories in items.items():
    score = 0

    for preference in user_preferences:
        if preference in categories:
            score += 1

    if score > 0:
        recommendations.append((item, score))

# Sort recommendations by highest score
recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)

# Display results
print("\n=== Recommended Items ===")

if recommendations:
    for item, score in recommendations:
        print(f"{item} (Match Score: {score})")
else:
    print("No matching recommendations found.")