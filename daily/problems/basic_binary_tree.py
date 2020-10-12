from daily.structures.binary_tree import Node

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
