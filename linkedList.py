"""
head is the beginning of the linked list.
data is the element stored by the user.
next is the reference to the next element.
"""

import platform
import os

# Just to clear console
def clear_console():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")



class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next



class LinkedList:
	def __init__(self):
		self.head = None
	
	def insert_at_begining(self, data):
		node = Node(data, self.head)
		self.head = node
	
	def insert_at_end(self, data):
		if self.head is None:
			self.head = Node(data, None)
			return
		
		itr = self.head
		while itr.next:
			itr = itr.next
		
		itr.next = Node(data, None)

	def count(self):
		count = 0
		itr = self.head
		while itr:
			count += 1
			itr = itr.next
		return count

	def remove_at(self, index):
		if index < 0 or index >= self.count():
			raise Exception("Invalid Index")
		
		if index == 0:
			self.head = self.head.next
			return
		
		count = 0
		itr = self.head

		while itr:
			if count == index - 1:
				itr.next = itr.next.next
				break
			itr = itr.next
			count += 1
	
	def insert_at(self, index, data):
		if index < 0 or index >= self.count():
			raise Exception("Invalid index")

		if index == 0:
			self.insert_at_begining(data)
			return
		
		count = 0
		itr = self.head
		while itr:
			if count == index - 1:
				node = Node(data, itr.next)
				itr.next = node
				break
			
			itr = itr.next
			count += 1
	
	def insert_after_value(self, val, data):
		if self.head is None:
			return
		
		if self.head == val:
			self.head.next = Node(data, self.head.next)
			return

		itr = self.head
		while itr:
			if itr.data == val:
				node = Node(data, itr.next)
				itr.next = node
				break
			itr = itr.next
	
	def remove_val(self, data):
		if self.head is None:
			return
		
		if self.head.data == data:
			self.head = self.head.next
			return
		itr = self.head
		while itr:
			if itr.next.data == data:
				itr.next = itr.next.next
				break
			itr = itr.next

	
	def print(self):
		if self.head is None:
			clear_console()
			print("Empty Linked List\n\n")
			return
		itr = self.head
		llstr = ''
		while itr:
			llstr += str(itr.data) + "--->"
			itr = itr.next
		llstr += "None\n\n"
		clear_console()
		print(llstr)

exit_no = 9
cmd = f"""[1]  Insert at the beggining		[2]  Insert at the end
[3]  Count				[4]  Print
[5]  Remove at index			[6]  Insert at index
[7]  Insert after value			[8]  Remove by value
[{exit_no}]  Exit\n
Enter : """

if __name__ == "__main__":
	ll = LinkedList()
	inp = 0
	while inp != exit_no:
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
			str_ele = input("Enter elements: ")
			ele = str_ele.split(' ')

			for i in ele:
				ll.insert_at_begining(int(i))
			ll.print()
		elif inp == 2:
			str_ele = input("Enter elements: ")
			ele = str_ele.split(" ")

			for i in ele:
				ll.insert_at_end(int(i))
			ll.print()
		elif inp == 3:
			clear_console()
			print("Length of Linked List is: " + str(ll.count()) + "\n\n")
		elif inp == 4:
			ll.print()
		elif inp == 5:
			i = int(input("Enter the index to remove: "))
			ll.remove_at(i)
			ll.print()
		elif inp == 6:
			i = int(input("Enter the index to add: "))
			data = int(input("Enter the element: "))
			ll.insert_at(i, data)
			ll.print()
		elif inp == 7:
			val = int(input("Enter the value to search: "))
			data = int(input("Enter the data to insert after the value: "))
			ll.insert_after_value(val, data)
			ll.print()
		elif inp == 8:
			val = int(input("Enter the value to remove: "))
			ll.remove_val(val)
			ll.print()
		
	
