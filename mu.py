def mu(function, string=True): #string input is default
	def anonymous(a=0): #anonymous function, with default parameter = 0
		def t(a=0): #used for recursion, t is shorthand for "this"
			return anonymous(a)
		
		try:
			if string: #if string input flag is set
				code = function.strip().strip(';:').split(';')
				
				codes = []
				lines = []
				posit = 0
				
				#Get Rid of Blank Lines (';;'), which are actually semicolons (';')
				while posit < len(code):
					if code[posit] == '' and len(codes) > 0:
						new = codes[len(codes)-1] + ';' + code[posit+1]
						codes.pop()
						codes.append(new)
						posit = posit + 2
						
					else:
						codes.append(code[posit])
						posit = posit + 1
				
				#Add Level of Indentation with ':' (see below)
				for part in range(len(codes)):
					codes[part] = ':' + codes[part].strip()
					
				#Add a wrapper function so we can directly call exec() on it
				codes = ['def output(a,t):'] + codes + ['return output(a,t)']
				
				#Various processing tasks
				for pos in range(len(codes)):
					tabs = 0
					updated = codes[pos]
					
					#deal with escape sequences in strings first
					for seq in [['\\','\\\\'],['\n','\\n'],['\t','\\t']]:
						updated = updated.replace(seq[0], seq[1])
					
					#convert ':' to tabs
					for char in updated:
						if char == ':':
							tabs = tabs + 1
						else:
							break
					
					#put code blocks in the same exec() call
					if tabs > 0:
						updated = '\t'*tabs + updated[tabs:]
						updated = lines[len(lines)-1] + '\n' + updated
						lines.pop()
					lines.append(updated)
					
			else: #Python triple quote string mode
				#split by '\n' itself, rather than ';'
				code = function.strip().split('\n')
				
				pos = 0
				tabs = 0
				
				#Tab standardization
				try:
					while code[1][pos:pos+1] == '\t':
						tabs += 1
						pos += 1
				except IndexError:
					tabs = 2
				
				try:
					exec(code[0].strip() + '\n' + '1==1')
				except SyntaxError:
					tabs -= 1
				#End Tab standardization
				
				#Re-add tabs properly
				code[0] = '\t'*tabs + code[0].lstrip('\t')
				code = [line[tabs-1:] for line in code]
				
				#Add wrapper function (see above)
				code = '\n'.join(code)
				lines = ['def output(a,t):\n' + code] + ['return output(a,t)']
				
			for line in lines:			
				#Deal with variable conflicts in recursion
				if line[0:7] == 'return ':
					locals()['temporary'] = locals()['a']
					globals()['a'] = locals()['a']
					out = eval(line[7:])
					locals()['a'] = locals()['temporary']
					return out
					
				exec(line)
		except IndexError: #Deal with empty functions
			print('ERROR: Function cannot be empty.')
					
	return anonymous #return the anonymous function