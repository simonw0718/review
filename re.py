data = []
with open('reviews.txt', 'r') as f:
    for review in f:
        data.append(review.strip())
print(data[0])
print(len(data))

