#class to hold authorization tokens
class Tokens:
	def __init__(self):
		self.token_list = []
		self.num_tokens = 0
		self.current_token = 0
	
	#add new token to list
	def add_token(self, token):
		self.token_list.append(token)
		self.num_tokens += 1

	#get next token
	def next_token(self):
		token = self.token_list[self.current_token]
		self.current_token += 1
		if (self.current_token == self.num_tokens):
			self.current_token = 0
		return token

EB_tokens = Tokens()
EB_tokens.add_token('CAFHP4AMQ6TFSGNXPAN4')
EB_tokens.add_token('MBDUEYBOHQDWCMW6K6NL')
EB_tokens.add_token('FFQRRNFRZHPHNQ7DTT7T')
EB_tokens.add_token('4LPIC5HJYXE6YAB27M6I')
