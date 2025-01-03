speed = [48,47,54,50,42,68,39,46]
result = list(filter(lambda value: value >50,speed))
print(f'Recorded values: {speed}')
print(f'Speed too high: {result}')