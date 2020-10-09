class Node():
    def __init__(self, val:int=None, left:'Node'=None, right:'Node'=None):
        self.value = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value) if self.value else "None"
    
    def add(self, val:int):
        if self.value:
            if val >= self.value:
                if self.right:
                    self.right.add(val)
                else:
                    self.right = Node(val)
            if val <= self.value:
                if self.left:
                    self.left.add(val)
                else:
                    self.left = Node(val)
        else:
            self.value = val

    def traverse(self, root):
        current_level = [root]
        while current_level:
            print(' '.join(str(node) for node in current_level))
            next_level = list()
            for n in current_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            current_level = next_level

    def count_unival(self)->int:
        if not self.left and not self.right:
            return 1
        else:
            left = 0 if not self.left else self.left.count_unival()
            right = 0 if not self.right else self.right.count_unival()
            return left + right

n = Node(5)
n.add(3)
n.add(10)
n.add(11)
n.add(2)
n.add(1)
n.add(4)
n.add(11)
n.traverse(n)
print(n.count_unival())
