from collections import deque

import platform
import os

# Just to clear the output
def clear_console():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")


class Stack():
	def __init__(self):
		self.container = deque()
	

	def append(self, item):
		self.container.append(item)
	

	def pop(self):
		return self.container.pop()
	

	def pop_left(self):
		return self.container.popleft()
	

	def remove(self, item):
		self.container.remove(item)


	def extend(self, items):
		self.container.extend(items)
	

	def peek(self):
		return self.container[-1]
	

	def is_empty(self):
		return len(self.container) == 0
	
	
	def size(self):
		return len(self.container)
	
	def print(self):
		print(str(self.container)[6:-1] + "\n\n")


cmd = f"""[1]  Append		[2]  Pop
[3]  Pop left		[4]  Remove
[5]  Extend		[6]  Peek
[7]  Is empty		[8]  size
[9]  Print		[10]  Exit\n
Enter : """

if __name__ == "__main__":
	stk = Stack()
	inp = 0
	while inp != 10:
		inp = 0
		try:
			inp = int(input(cmd))
		except (KeyboardInterrupt, EOFError):
			clear_console()
			print("Exiting...\n")
			break
		except ValueError:
			clear_console()
			print("Enter a number...\n\n")
			inp = 0
			continue
		
		if inp == 1:
			item = int(input("Enter a number to append: "))
			clear_console()
			stk.append(item)
			stk.print()
		elif inp == 2:
			clear_console()
			print(f"Item: {stk.pop()} is popped from stack.\n\n")
		elif inp == 3:
			clear_console()
			print(f"Item: {stk.pop_left()} is popped from stack.\n\n")
		elif inp == 4:
			item = int(input("Enter the item you want to remove : "))
			stk.remove(item)
			clear_console()
			stk.print()
		elif inp == 5:
			item = input("Enter the items to extend : ").split(' ')
			item = list(map(int, item))
			stk.extend(item)
			clear_console()
			stk.print()
		elif inp == 6:
			print(f"{stk.peek()}\n\n")
		elif inp == 7:
			clear_console()
			print(f"Stack is {'' if not stk.is_empty() else 'not'} empty.\n\n")
		elif inp == 8:
			clear_console()
			print(f"The size of the stack is : {stk.size()}\n\n")
		elif inp == 9:
			clear_console()
			stk.print()