'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.
'''
def count_positives_sum_negatives(arr):
    
    leng = len(list([x for x in arr if x > 0])) # get length
    sm = sum(x for x in arr if x < 0) # get sum
    
    return [leng, sm] if len(arr) > 0 else [] #return if arr not empty or [] 