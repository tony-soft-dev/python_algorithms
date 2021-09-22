import math
def binary_search(arr, target):
	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = math.floor((high + low) / 2)
		guess = arr[mid]

		if guess == target:
			return mid
		if guess > target:
			high = mid - 1
		else:
			low = mid + 1

	return None


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('do you know what an integer is?')

answer = input()

if (answer == 'no'):
	print('sucks...')
else:
	print('enter an integer here:')
	try:
		inp = int(input())
		print(binary_search(arr, inp))
	except Exception as e:
		print('ah ah ah... ypou didnt say the magic word')
	else:
		pass
	finally:
		print('completo')




