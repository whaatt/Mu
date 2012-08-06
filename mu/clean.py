def mu(function):
	def anonymous(a=0):
		def t(a):
			return anonymous(a)
			
		code = function.split(';')		
		lines = []
		
		for pos in range(len(code)):
			tabs = 0
			updated = code[pos]
			updated = updated.strip()
			for char in updated:
				if char == ':':
					tabs = tabs + 1
				else:
					break
			if tabs > 0:
				updated = '\t'*tabs + updated[tabs:]
				updated = lines[len(lines)-1] + '\n' + updated
				lines.pop()
			lines.append(updated)
			
		for line in lines:			
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