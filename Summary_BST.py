BST Basic Operations:

# Insert Recursive
def insert(curr, parent, val):
    if curr is None:
        if val < parent.val:
            parent.left = Node(val)
        else:
            parent.right = Node(val)
    else:
        if val < curr.val:
            insert(curr.left, curr, val)
        else:
            insert(curr.right, curr, val)

# Insert Stack
def insert_stack(root, val):
    curr = root
    parent = None
    while(True):
        parent =curr
        if val < curr.val:
            curr = curr.left
            if curr is None: # get leaf
                parent.left = Node(val)
                break
        else:
            curr = curr.right
            if curr is None:
                parent.right = Node(val)
                break
		
# InOrder Traverse Recursive
def traverse_recurr(root, res):
    if root:
        traverse_recurr(root.left, res)
        res.append(root.val)
        traverse_recurr(root.right, res)

# InOrder Traverse DFS
def traverse_stack(root):
    stack = []
    res = []
    while(True):
        while(root):
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
    return res
 
# Find Recursively
def find(root, val):
    if root:
        if val < root.val:
            return find(root.left, val)
        elif val > root.val:
            return find(root.right, val)
        else:
            return root
    return None

# Find Stack
def find_stack(root, val):
    while(True):
        if root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        else:
            return None
