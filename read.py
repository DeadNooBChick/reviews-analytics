data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # %係求餘數
			print(len(data))
print('檔案讀取完成, 總共有: ', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度就是', sum_len/len(data))
