def special_list(values, print_backwards):
    #### DO NOT MODIFY BELOW ####
    d = MySpecialList()

    for value in values:
        d.append(value)
    return d.print_backwards() if print_backwards else d.print_forward()
    ### DO NOT MODIFY ABOVE


class Node():
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
    

class MySpecialList():
    my_list = []

    def append(self, data):
        list_lenght = len(self.my_list)
        
        next = None
        
        if list_lenght == 0:
            prev = None

        elif list_lenght > 0:
            last_item = self.my_list[-1]
            prev = last_item
            last_item.next = Node(data, prev, next)
            
        self.my_list.append(Node(data, prev, next))
        return self.my_list
    
    def print_forward(self):
        list = []
        for item in self.my_list:
            list.append(item.data)
        return list
    
    def print_backwards(self):
        reverse_list = []
        list_lenght = len(self.my_list)
        i = list_lenght - 1

        while i >= 0:
            reverse_list.append(self.my_list[i].data)
            i  -= 1

        return reverse_list

# print(special_list([1,2,3,4,5], False))
print(special_list([1,2,3,4,5], True))
