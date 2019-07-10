import time


data = []
count = 0
with open('reviews.txt', 'r') as f:
    for review in f:
        data.append(review)
        count += 1 #快寫法 c = c+1
        if count % 1000000 == 0:
            print(len(data))
print('讀完了,共有', len(data), '個資料')
print(data[0])


#文字計數
start_time = time.time() #使用time function紀錄系統時間
wc ={} # word_count
for d in data:
    words = d.split() # split預設就是空白建
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增新的key去WC字典
for word in wc:
    if wc[word] > 100000:
        print(word,wc[word])

end_time = time.time() #紀錄當時時間

print('花了', end_time - start_time, 'seconds')
print(len(wc))
print(wc['Simon'])


#查找文字
while True:
    word = input('想查啥')
    if word == 'q':
        break
    elif word not in wc:
        print('沒有這個字')
    else:
        print(word, '出現過的次數為', wc[word])    
print('感謝使用')