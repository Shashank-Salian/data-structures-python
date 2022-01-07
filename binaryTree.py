from queue import Queue


class Node:

	def __init__(self, val) -> None:
		self.val = val
		self.left = None
		self.right = None


"""
			A
		  /   \ 
		B	   C
	   / \	    \ 
	  D	  E		 F
"""


class BinaryTree:

	def breadthFirst(self, root):
		if root == None:
			return []
		res = []
		queue = Queue()
		queue.put(root)
		while queue.qsize() > 0:
			current = queue.get()
			res.append(current.val)

			if current.left != None:
				queue.put(current.left)
			if current.right != None:
				queue.put(current.right)
		return res

	# Depth first iteratively
	def depthFirstIt(self, root):
		if root == None:
			return []
		res = []
		stack = [root]
		while len(stack) > 0:
			current = stack.pop()
			res.append(current.val)

			if current.right != None:
				stack.append(current.right)
			if current.left != None:
				stack.append(current.left)
		return res

	# Depth first recursively
	def depthFirstRe(self, root):
		if root == None:
			return []
		leftValues = self.depthFirstRe(root.left)
		rightValues = self.depthFirstRe(root.right)
		# return (leftValues + [root.val] + rightValues) # In order
		# return (leftValues + rightValues + [root.val]) # Post order
		return ([root.val] + leftValues + rightValues)  # Pre order

	# Similar methods
	def printInOrder(self, root):
		if root:
			self.printInOrder(root.left)
			print(root.val, end="  "),
			self.printInOrder(root.right)

	def printPostOrder(self, root):
		if root:
			self.printPostOrder(root.left)
			self.printPostOrder(root.right)
			print(root.val, end="  ")

	def printPreOrder(self, root):
		if root:
			print(root.val, end="  ")
			self.printPreOrder(root.left)
			self.printPreOrder(root.right)

	# Check if element exists using breadth first method
	def includesBF(self, root, ele):
		if root == None:
			return False
		queue = Queue()
		queue.put(root)

		while queue.qsize() > 0:
			current = queue.get()
			if current.val == ele:
				return True

			if current.left:
				queue.put(current.left)
			if current.right:
				queue.put(current.right)

		return False

	# Check if element exists using depth first method
	def includesDP(self, root, ele):
		if root == None:
			return False

		if root.val == ele:
			return True

		return self.includesDP(root.left, ele) or self.includesDP(
		    root.right, ele)

	def sum(self, root):
		if root == None:
			return 0

		return root.val + self.sum(root.left) + self.sum(root.right)

	def sumIt(self, root):
		if root == None:
			return 0

		queue = Queue()
		queue.put(root)
		s = 0
		while queue.qsize() > 0:
			current = queue.get()
			s += current.val
			if current.left != None:
				queue.put(current.left)
			if current.right != None:
				queue.put(current.right)
		return s

	def minValRe(self, root):
		if root == None:
			return float('inf')

		return min(root.val, self.minValRe(root.left),
		           self.minValRe(root.right))

	def minValIt(self, root):
		if root == None:
			return None

		q = Queue()
		q.put(root)
		minVal = root.val
		while q.qsize() > 0:
			current = q.get()

			if current.val < minVal:
				minVal = current.val

			if current.left != None:
				q.put(current.left)
			if current.right != None:
				q.put(current.right)

		return minVal

	def maxRootToLeafRe(self, root):
		if root == None:
			return float('-inf')

		if root.left == None and root.right == None:
			return root.val

		maxChildPath = max(self.maxRootToLeafRe(root.left),
		                   self.maxRootToLeafRe(root.right))
		return root.val + maxChildPath


if __name__ == "__main__":
	a = Node(5)
	b = Node(12)
	c = Node(34)
	d = Node(45)
	e = Node(58)
	f = Node(0)

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f

	biTree = BinaryTree()

	print("\n----------DepthFirst----------\n")
	print(biTree.depthFirstRe(a))
	print(biTree.depthFirstIt(a))

	print("\n----------BreadthFirst----------\n")
	print(biTree.breadthFirst(a))

	print("\n\n----------In-order----------\n\n")
	biTree.printInOrder(a)

	print("\n\n----------Post-order----------\n\n")
	biTree.printPostOrder(a)

	print("\n\n----------Pre-order----------\n\n")
	biTree.printPreOrder(a)

	searchEle = int(input("\n\nEnter a element to search : "))
	print(
	    f"{searchEle} does{'' if biTree.includesBF(a, searchEle) else ' not'} exist"
	)
	print(
	    f"{searchEle} does{'' if biTree.includesDP(a, searchEle) else ' not'} exist"
	)

	print("\n\n----------Sum----------\n\n")
	print(biTree.sum(a))
	print(biTree.sumIt(a))

	print("\n\n----------Minimum Value----------\n\n")
	print(biTree.minValRe(a))
	print(biTree.minValIt(a))

	print("\n\n----------Max root to leaf Value----------\n\n")
	print(biTree.maxRootToLeafRe(a))
