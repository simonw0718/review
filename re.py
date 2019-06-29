data = []
count = 0
with open('reviews.txt', 'r') as f:
    for review in f:
        data.append(review)
        count += 1 #快寫法 c = c+1
        if count % 10000 == 0:
        	print(len(data))
print('第一筆commit是\n', '-------------\n', data[0], '-----------------\n')
total = len(data)
print('第一筆commit 長度是', len(data[0]))

length = 0
for comt in data:
	length += len(comt)

print('總共有', length, '個字元')
average = length / total
print('平均每筆data有', average, '個字元')

fil_data = []
for long_com in data:
	if len(long_com) >= 1000:
		fil_data.append(long_com)
print('超過1000字元的commit有', len(fil_data), '個')
