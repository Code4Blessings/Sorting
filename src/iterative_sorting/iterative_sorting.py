import random

#Selection sort is when you take the smallest element in an unsorted array and bring it over to the sorted side, then go back to the unsorted side and bring the next smallest element in the unsorted array and then keep repeating the process until the last index is reached in the unsorted array.

def selection_sort( arr ): 
    #1. In the initial unsorted array, iterate over it until the smallest element is reached
    for i in range(0, len(arr) - 1):
        #print(arr)
        #2. Store smallest element in a sorted variable
        cur_index = i
        smallest_index = cur_index
        #3. Loop over the rest of the unsorted array
        for j in range(cur_index, len(arr)):
            #4.if the any element is smaller than the current, smaller element, move to the sorted variable
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr  

        
test_list = random.sample(range(0, 40), 10)
selection_sort(test_list)

# TO-DO:  implement the Bubble Sort function below

#Bubble Sort
#Bubble sort works by comparing each element to it's neigbor
#If the second index is smaller than the first index, swap the two indices


def bubble_sort(arr):
    

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


  
  
