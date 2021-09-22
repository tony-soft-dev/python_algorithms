def find_smallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i

	return smallest_index

def selection_sort(arr):
	new_arr = []
	for i in range(len(arr)):
		smallest = find_smallest(arr)
		new_arr.append(arr.pop(smallest))
	return new_arr

arr = [5, 3, 7, 2, 9, 10, 34, 12]

print(selection_sort(arr))