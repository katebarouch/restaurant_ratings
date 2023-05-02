def read_scores(filename):
    scores = {}
    scores_file = open(filename)
    for row in scores_file:
        data = row.rstrip().split(':')

        name = data[0]
        score = data[1]
        scores[name] = score
    scores_file.close()

    return scores

def print_scores(scores):
    for restaurant, rating in sorted(scores.items()):
        print(f'{restaurant} is rated at {rating}.')


def add_restaurant(scores):
    while True:
        end = input("Do you have a new restaurant rating? Enter yes or no. >")
        if end == 'no':
            break
        restaurant = input("What is the restaurant name? >")
        rating = input("What is your score? >")

        scores[restaurant] = int(rating)

    return scores


# Prompt user further- does restaruant already have score? Did they not give a restaurant name?s

scores = read_scores('scores.txt')
scores = add_restaurant(scores)
print_scores(scores)