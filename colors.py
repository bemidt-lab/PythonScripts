best_colors = { 
    "favorite": "blue",
    "least favorite": "yellow",
    "okayest": "green"
}
print(best_colors["favorite"])
best_colors["favorite"] = "turquoise"
print(best_colors["favorite"])

print(best_colors)

new_favorite = best_colors.get("favorite")
print(new_favorite)

blind_to = best_colors.get("not", "I can't see that one")
print(blind_to)

print(best_colors.keys()) 
print(best_colors.values())
print(best_colors.items())