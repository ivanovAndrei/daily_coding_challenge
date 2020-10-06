class Node():
    def __init__(self, val:int=None, left:'Node'=None, right:'Node'=None):
        self.value = val
        self.left = None
        self.right = None

    def printout(self):
        print(self.value)
        if self.left:
            self.left.printout()
        if self.right:
            self.right.printout()
    
    def add(self, val:int):
        if self.value:
            if val > self.value:
                if self.right:
                    self.right.add(val)
                else:
                    self.right = Node(val)
            if val < self.value:
                if self.left:
                    self.left.add(val)
                else:
                    self.left = Node(val)
        else:
            self.value = val

n = Node(5)
n.add(3)
n.add(10)
n.add(11)
n.printout()
