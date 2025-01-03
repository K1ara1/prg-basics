scores = [37,51,44,23,78,92,39,84,83,51]
def min_pts(limit):
   return lambda pts: pts>=limit
for limit in [70,40,30]:
    filtered_scores = list(filter(min_pts(limit),scores))
    print(f"Min {limit} pts: {filtered_scores}")