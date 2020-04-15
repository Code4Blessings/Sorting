import random

[0,1,            5, 8, 4, 2, 9, 6, 3, 7]

def selection_sort( arr ):
    
# # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
    #     #TO-DO: find next smallest element
    #     #(hint, can do in 3 loc)

    # TO-DO: swap
    return arr
    

    #Set the smallest # equal to the 0 index#



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #Establish the length of array to establish the items within the ar
    length = len(arr)
    for i in range(length - 1):
        #Loop over the array equivalent to for
        for j in range(length - 1):
            if arr[j] > arr[j+1]:
            #Swap indices
                bubble = i
                arr[j] = arr[j+1]
                arr[j+1] = bubble

        return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr

#Loop through an array and find the smallest #(i).
    # for i in range(0, len(arr)-1):
    #     return min(i)
    #Loop through the array again and search for the next smallest #(j)
    #If j < i, swap
        # for j in range(0, len(arr)-1):
        #     if j < i:
        #         return min(j)
    #What's the code for how to stop looping?
 
