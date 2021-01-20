import platform
import os

# Just to clear the output
def clear_console():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")



class HashTable:
	def __init__(self):
		self.MAX = 100
		self.arr = [[] for i in range(self.MAX)]
	
	def get_hash(self, key):
		h = 0
		for i in key:
			h += ord(i)
		return h % self.MAX
	
	def print_all(self):
		for ele in self.arr:
			if len(ele) > 0:
				print(ele)
	
	def __setitem__(self, key, val):
		h = self.get_hash(key)
		found = False
		# To update the existing array
		# You loop through the linked list in that position
		for i, ele in enumerate(self.arr[h]):
			if len(ele) == 2 and ele[0] == key:
				self.arr[h][i] = (key, val)
				found = True
				break
		if not found:
			self.arr[h].append((key, val))
	
	def __getitem__(self, key):
		h = self.get_hash(key)
		for ele in self.arr[h]:
			if ele[0] == key:
				return ele[1]
	
	
	def __delitem__(self, key):
		h = self.get_hash(key)
		for i, ele in enumerate(self.arr[h]):
			if ele[0] == key:
				val = self.arr[h][i]
				del self.arr[h][i]
		return val



cmd = """\n
[1]  Insert item		[2]  Get item
[3]  Delete item		[4] Print all
[5]  Exit\n
Enter : """

note = """\n\033[92;1mNote: \033[m\033[95mEnter key value pairs with ':' and separate the elements with ','\033[m
Example: \033[36m
name: someone, age: 18\033[m\n
"""

# Validates user input to array of arrays with 2 elements where 0'th element is key and 1'st element is value
# (don't worry much about this function. This just here to ease user's life.)
def validate_input(st):
	coma_split = st.split(',')
	colon_split = []
	for e in coma_split:
		colon_split.append(e.split(':'))
	for ele in colon_split:
		ele[0] = ele[0].strip()
		ele[1] = ele[1].strip()
	del coma_split
	return colon_split


if __name__ == "__main__":
	hsh = HashTable()
	inp = 0
	while inp != 5:
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
			inp_str = input(f"{note}Enter the elements: \n")
			valid_arr = validate_input(inp_str)
			for arr in valid_arr:
				# This looks like a dictionary because of special methods in class __getitem__ and __setitem__
				hsh[arr[0]] = arr[1]
		
		elif inp == 2:
			inp_str = input("Enter the key: ")
			print(f"{hsh[inp_str]}\n\n")
		
		elif inp == 3:
			inp_str = input("Enter key to delete: ")
			del hsh[inp_str]
		
		elif inp == 4:
			print("\n")
			hsh.print_all()
		
