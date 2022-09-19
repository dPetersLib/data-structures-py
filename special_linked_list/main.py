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
        return
    
    def print_forward(self):
        return
    
    def print_backwards(self):
        return
