A regular LinkedList data structure is typically constructed of nodes that contain a data value and a pointer to the next node.
It is your task, however, to implement a special type of Linkedlist data structe called MySpecialList. In this case, each node keeps track of the next node as well as the previous node. This is important because you will need to print the list values forward and backwards using this special data structure.
The initial code contains a skeleton of the MySpecialList class and a completed Node class. Your job is to implement the following functions:
1. append(self, data) which appends the given value to the end of your data structure
2. print_forward(self) which returns the values of your data structure in regular form (from front to end).
3. print_backwards(self) which returns the values of your data structure inn reverse order (from end to front).

Examples
Input: 
        values = [1,2,3,4,5]
        print_backwards = False
Output = [1,2,3,4,5]

Input:
        values = [1,2,3,4,5]
        print_backwards = True
Output = [5,4,3,2,1]
