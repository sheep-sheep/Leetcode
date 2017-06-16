1. BST Basic Operations:

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

# delete
# 1. only need to delete leaf, either right or left
# 2. need to delete non-leaf node, with one child
# 3. need to delete non-leaf node, with 2 children, will need to 
# find sucessor(min in right child), make sure the sucessor's right child is relocated.
def delete(root, val):
    def find(root, parent, val):
        if root:
            if val < root.val:
                return find(root.left, root, val)
            elif val > root.val:
                return find(root.right, root, val)
            else:
                return root, parent
        return None
    def isLeftChild(root, parent):
        return parent.left == root
    def isleaf(root):
        return (root.right is None) and (root.left is None)
    def getSucessorTree(root):
        curr = root
        while(True):
            parent = curr
            curr = curr.left
            if curr.left is None:
                break
        sucessor = curr
        if sucessor.right:
            parent.left = sucessor.right
        sucessor.right = root
        return sucessor

    curr, parent = find(root, root, val)
    if not curr: return
    # case 1
    if isleaf(curr):
        if isLeftChild(curr, parent):
            parent.left = None
        else:
            parent.right = None
    # case 3
    elif (curr.left and curr.right):
        sucessor = getSucessorTree(curr.right)
        if isLeftChild(curr, parent):
            parent.left = sucessor
        else:
            parent.right = sucessor
    # case 2
    else:
        if isLeftChild(curr, parent):
            parent.left = curr.right if curr.right else curr.left
        else:
            parent.right = curr.right if curr.right else curr.left
    return root

# BFS with Queue
# Use this queue you can print out all nodes at each level, i think is a level order traverse!
def bfs(root):
    from Queue import Queue
    q = Queue()
    res, final= [],[]
    q.put(root)
    while(not q.empty()):
        n = q.qsize()
        while n:
            node = q.get()
            res.append(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            n -= 1
        print res
        final.append(res)
        res=[]
