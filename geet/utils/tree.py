'''
A simple tree structure for storing a directory snapshot.
'''


class Tree():
    def __init__(self):
        self.children = []

    def add_child(self, data: str) -> None:
        self.children.append(data)

    def get_children(self) -> list:
        return self.children


class BlobNode():
    def __init__(self, hash: str, content: list):
        self.hash = hash
        self.content = content


# t = Tree()
# t2 = Tree()
# print(t.get_children())
# t.add_child(33)
# t.add_child(1)
# t.add_child(t2)
# print(t.get_children())
