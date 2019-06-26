data = []
count = 0
with open('reviews.txt', 'r') as f:
    for review in f:
        data.append(review.strip())
        count += 1 #快寫法 c = c+1
        if count % 1000 == 0:
        	print(len(data))
print(data[0])
print(len(data))

