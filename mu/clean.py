def mu(function):
	def anonymous(a=0):
		def t(a):
			return anonymous(a)
			
		code = function.split(';')
		
		codes = []
		lines = []
		posit = 0
		
		while posit < len(code):
			if code[posit] == '' and len(codes) > 0:
				new = codes[len(codes)-1] + ';' + code[posit+1]
				codes.pop()
				codes.append(new)
				posit = posit + 2
			else:
				codes.append(code[posit])
				posit = posit + 1
		
		for pos in range(len(codes)):
			tabs = 0
			updated = codes[pos]
			updated = updated.strip()
			for seq in [['\\','\\\\'],['\n','\\n'],['\t','\\t']]:
				updated = updated.replace(seq[0], seq[1])
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