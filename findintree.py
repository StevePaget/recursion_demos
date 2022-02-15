class Node():
    def __init__(self,data):
        self.data = data
        self.children = []

    def addChild(self,newNode):
        self.children.append(newNode)

n1 = Node("A")
n2 = Node("D")
n3 = Node("G")
n4 = Node("X")
n5 = Node("C")
n6 = Node("P")
n7 = Node("W")
n8 = Node("L")
n1.addChild(n2)
n1.addChild(n4)
n2.addChild(n3)
n4.addChild(n5)
n4.addChild(n6)
n4.addChild(n8)
n6.addChild(n7)

def find(target, currentnode):
    found = False
    if currentnode.data == target:
        found = True
    else:
        # go through each child
        for child in currentnode.children:
            if find(target, child):
                found = True
    return found


print(find("C", n1))



