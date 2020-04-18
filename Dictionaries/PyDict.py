class PyDict:
	
	def __init__(self, dict):
		
		if dict:
			
			self.dict = dict
			
		else:
			
			self.dict = {}
			
	def add(self, key, val):

		if self.dict.get(key):
			
			return None
		
		else:
			
			self.dict.update({key : val})
			
	def change(self, key, val):

		if self.dict.get(key):
			
			self.dict.update({key : val})
	
	def remove(self, key):

		if self.dict.get(key):
			
			self.dict.pop(key)
		
		return (key, self.dict.get(key))
	
	def find(self, key):

		return self.dict.get(key)
	
	def size(self):
		
		self.total = 0
		
		for key in self.dict:
			
			self.total = self.total + 1
			
		return self.total
	
	def show(self):
	
		return (self.dict.keys(), self.dict.values())
			
