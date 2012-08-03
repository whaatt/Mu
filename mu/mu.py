def mu(function):
	def anonymous(a):
		def t(a):
			return anonymous(a)
			
		code = function.split(';')
		
		for line in code:
			line = line.strip()
			if line[0:7] == 'return ':
				locals()['temporary'] = locals()['a']
				globals()['a'] = locals()['a']
				out = eval(line[7:])
				locals()['a'] = locals()['temporary']
				return out
			try:
				locals()['temporary'] = locals()['a']
				globals()['a'] = locals()['a']
				eval(line)
				locals()['a'] = locals()['temporary']
			except SyntaxError:
				locals()['temporary'] = locals()['a']
				globals()['a'] = locals()['a']
				exec(line)
				locals()['a'] = locals()['temporary']
	
	return anonymous