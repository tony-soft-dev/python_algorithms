def quicksort(arr):
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]	# --> sub-array of all the elements less than the pivot
		less = [i for i in arr[1:] if i <= pivot]	# --> sub-array of all the elements greater than the pivot

		greater = [i for i in arr[1:] if i > pivot]

		return quicksort(less) + [pivot] + quicksort(greater)

arr = [5, 3, 8, 9, 2, 5, 7, 18, 12, 11]

print(quicksort(arr)) 