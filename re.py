data = []
count = 0
with open('reviews.txt', 'r') as f:
    for review in f:
        data.append(review.strip())
        count += 1 #快寫法 c = c+1
        if count % 10000 == 0:
        	print(len(data))
print(data[0])
total = len(data)
print(len(data[0]))

length = 0
for comt in data:
	length += len(comt)

print(length)
average = length / total
print(average)