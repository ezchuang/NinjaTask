class node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

node_0 = node(0)
node_1 = node(1)
node_0.next = node_1

pointer_b = node_0
pointer_c = node_0

print("==== compare ====")
print(pointer_b == pointer_c)
print(pointer_b is pointer_c)

print("==== node ====")
print(node_0.val)
print(node_0.next)
print(node_0.next.val)

print("==== pointer ====")
print(pointer_b)
print(pointer_c)

print(pointer_b.val)
print(pointer_b.next)
print(pointer_b.next.val)
print(pointer_b.next.next)
