# Start with current index = 0

# For all indices EXCEPT the last index:

# a. Loop through elements on right-hand-side of current index and find the smallest element

# b. Swap the element at current index with the smallest element found in above loop

# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        #TO-DO: find next smallest element
        #(hint, can do in 3 loc) 

        
        


        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)-1):
        bubble = arr[i]
        if arr[i] > arr[i+1]:
        #Swap indices
            arr[i] = arr[i+1]
            arr[i+1] = bubble

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
