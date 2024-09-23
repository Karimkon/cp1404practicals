import csv

def read_scores(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        subjects = next(reader)
        scores = {subject: [] for subject in subjects}
        for row in reader:
            for subject, score in zip(subjects, row):
                scores[subject].append(int(score))

    return scores

def print_scores(scores):
    for subject, score_list in scores.items():
        max_score = max(score_list)
        min_score = min(score_list)
        avg_score = sum(score_list) / len(score_list)
        print(f"{subject}: Max: {max_score}, Min: {min_score}, Avg: {avg_score:.2f}")

scores = read_scores('scores.csv')
print_scores(scores)
