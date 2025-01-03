scores = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]
def process_scores(score):
    min_val = min(score)
    max_val = max(score)
    score_list = list(score)
    
    score_list.remove(min_val)
    score_list.remove(max_val)
    
    return sum(score_list)

final_score = list(map(process_scores, scores))
print(final_score)

