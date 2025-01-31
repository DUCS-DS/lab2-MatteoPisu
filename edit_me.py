
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    if len(lst) <= 1:
        return True  

    increasing = True
    decreasing = True

    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]: 
            decreasing = False
        if lst[i] > lst[i + 1]: 
            increasing = False

    return increasing or decreasing  

if __name__ == "__main__":
    print(monotonic([1, 1, 3, 100]))  
    print(monotonic([11, 1, -9, -10]))  
    print(monotonic([2, 3, 2, 3]))  
    print(monotonic([1, 2, 2, 3]))  
    print(monotonic([5, 8, 5]))  
    print(monotonic([]))  
    print(monotonic([10]))  

