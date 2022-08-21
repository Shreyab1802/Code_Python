class Node:
    def __int__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if (self.data is None):
            self.data = data
        else:
            if self.data < data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif self.data > data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

root = Node('g')
root.insert('a')
root.insert('b')
root.insert('a')
root.insert('c')
root.insert('d')

print(root)
