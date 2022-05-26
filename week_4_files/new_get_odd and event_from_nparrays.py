arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# arr1
arr1_event_num = arr1[arr1 % 2 == 0]
arr1_odd_num = arr1[arr1 % 2 == 1]
print('arr1 odd numbers', arr1_odd_num, '\t', 'arr1 event numbers', arr1_event_num, '\n')

#arr2
arr2_event_num = arr2[arr2 % 2 == 0]
arr2_odd_num = arr2[arr2 % 2 == 1]
print('arr2 odd numbers', arr2_odd_num, '\t''arr2 event numbers', arr2_event_num)
