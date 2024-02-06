def sum_of_products(list1, list2):
    if len(list1) != len(list2):
        print("error")
        return None
    result = sum(a * b for a, b in zip(list1, list2))
    return result
if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
     list1 = list(map(int, input().split()))
     list2 = list(map(int, input().split()))
    # used Geeks for Geeks to figure out the iteration, zip(), and map() funciton
     result = sum_of_products(list1, list2)
     if result is not None:
        print(result)
