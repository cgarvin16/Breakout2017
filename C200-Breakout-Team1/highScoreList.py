from operator import itemgetter
import pickle

# pickle
high_scores = [
    ('Liz', 1800),
    ('Desi', 5000),
    ('Mike', 3200),
    ('John', 2000),
    ('Gabi', 3150),
    ('John', 3500),
    ('Gabi', 3100),
    ('John', 3000),
    ('Liz', 2800),
    ('Desi', 2800),
]

high_scores.append(('Dave', 3300))
high_scores = sorted(high_scores, key=itemgetter(1), reverse=True)[:10]

with open('highScores.txt', 'w') as f:
    pickle.dump(high_scores, f)


# unpickle
high_scores = []

with open('highScores.txt', 'r') as f:
    high_scores = pickle.load(f)