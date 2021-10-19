#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:13:06 2021

@author: bing
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:20:18 2021

@author: bing
"""



class Node():
    
    def __init__(self, num_lst):
        self.numbers = num_lst
    
    def set_numbers(self, new_lst):
        self.numbers = new_lst
    
    def get_numbers(self):
        return self.numbers
    
    def get_one_number(self, idx):
        if idx > len(self.numbers) - 1:
            return None
        else:
            return self.numbers[idx]
    
    def length(self):
        ##remove the following code and input yours
        return len(self.numbers)
    
    def get_children(self):
        middle = self.length() // 2
        left_child = self.numbers[:middle]
        right_child = self.numbers[middle:]
        return left_child, right_child
        
    def add_elements(self, numbers):
        if type(numbers) == int:
            numbers = [numbers]
        self.numbers.extend(numbers)

      
    def __str__(self):
        ##remove the following statements and put in your code
        return f"{self.numbers}"
    
    
    def merge(self, other_node):
        left = self.get_numbers()
        
        right = other_node
        result = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            # change the direction of this comparison
            # to change the direction of the sort
            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1

        if left:
            result.extend(left[left_idx:])
        if right:
            result.extend(right[right_idx:])
        return result

# Merge sort using Node class
def merge_sort(ls):
    node = Node(ls)
    if node.length() <= 1:
        return node
    left_child, right_child = node.get_children()
    left_child = merge_sort(left_child)
    right_child = merge_sort(right_child)
    return left_child.merge(right_child)



if __name__ == "__main__":
    ##Tests of Node class
    CHECK_ON = True
    if CHECK_ON:
        node = Node([5, 3, 4, 2, 1])
        print(node.numbers)
        print(node.get_numbers())
        node.set_numbers([3, 6, 2, 8, 1])
        print(node.get_numbers())
        print(node.get_one_number(1))
        print(node.length())
        print(node)
        left, right = node.get_children()
        print(left)
        print(right)
        node.add_elements([1, 2, 3])
        node.add_elements(10)
        print(node.get_numbers())
        node_1 = Node([1, 3, 5])
        node_2 = Node([2, 4, 6])
        result = node_1.merge(node_2)
        print(result)
        node_3 = Node([2, 4, 8])
        node_4 = Node([1, 3, 9, 10, 15])
        result = node_3.merge(node_4)
        print(result)
    
    ##Test of merge sort
    import random
    random.seed("Midterm")
    randomized_lists_merge = []
    print("Generating randomized lists for sorting...")
    LIMIT = 10
    randomized_lists_merge = [random.randint(0, i + 1) for i in range(LIMIT)]
    print("The randomly generated list is: ", randomized_lists_merge)
    print("Sorting")
    #root = Node(randomized_lists_merge)
    root = randomized_lists_merge
    merge_sorted_list = merge_sort(root)
    print("merge sort: ", merge_sorted_list)
    


        
        
    