Assignment #5-2, Brian Chenoweth, masc1367

class Token:
	def __init__(self, poo):
		self.value = poo
		def GetStringValue():
			return self.value
		def GetElementType(self):
			return "Unknown"
                        
class LitIntToken(Token):
	def GetElementType(self):
		return "Literal-Int"
                
                
class NameToken(Token):
	def GetElementType(self):
		return "Name"
