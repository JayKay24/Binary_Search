def binary_search(a_list, item):
    """
    Binary search algorithm.
    """
    first = 0
    last = len(a_list)-1
    found = False
    count = 0
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            count += 1
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    return count - 4
    

class BinarySearch(list):
    """
    This class inherits from the list class and takes two integers as parameters,
    a and b. a is the length of the list to be created and  b is the step or
    difference between consecutive values and initializes an instance variable
    length.
    It defines a method search which implements the binary search algorithm and
    takes in the value you are to find as its argument. It returns a dictionary
    object which contains count, the number of times the function iterated and
    index, which is the index of the item in the list.
    """
    def __init__(self, a, b):
        num = b
        for i in range(a):
            self.append(num)
            num += b
        self.length = len(self)
        self.sort() # Sort the list to implement binary search algorithm.
        
    def search(self, value):
        """
        Implement the binary search algorithm and return a dictionary 
        containing the number of times the function iterated to find the
        index of value.
        """
        found_dict = {}
        
        found_dict['count'] = binary_search(self, value)
        try:
            found_dict['index'] = self.index(value)
        except ValueError:
            found_dict['index'] = -1
        
        return found_dict
        