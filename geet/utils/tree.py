'''
A simple tree structure for storing a directory snapshot.
'''


class Node():
    def __init__(self, data: str):
        self.data = data


class Tree(): 
    def __init__(self, name):
        self.name = name
        self.children = []

    def insert_child(self, object: any):
        self.children.append(object)

    def get_children(self):
        return self.children


# commmit_tree = Tree('A')
# print(commmit_tree.name)
# print(commmit_tree.get_children())
# commmit_tree.insert_child('B')
# commmit_tree.insert_child('C')
# print(commmit_tree.get_children())
