def mu(___function___):
	def ___anonymous___(a=0):
		def t(a):
			return ___anonymous___(a)
			
		___code___ = ___function___.split(';')		
		___lines___ = []
		
		for ___pos___ in range(len(___code___)):
			___tabs___ = 0
			___updated___ = ___code___[___pos___]
			___updated___ = ___updated___.strip()
			for ___char___ in ___updated___:
				if ___char___ == ':':
					___tabs___ = ___tabs___ + 1
				else:
					break
			if ___tabs___ > 0:
				___updated___ = '\t'*___tabs___ + ___updated___[___tabs___:]
				___updated___ = ___lines___[len(___lines___)-1] + '\n' + ___updated___
				___lines___.pop()
			___lines___.append(___updated___)
			
		for ___line___ in ___lines___:			
			if ___line___[0:7] == 'return ':
				locals()['___temporary___'] = locals()['a']
				globals()['a'] = locals()['a']
				___out___ = eval(___line___[7:])
				locals()['a'] = locals()['___temporary___']
				return ___out___
			
			try:
				locals()['___temporary___'] = locals()['a']
				globals()['a'] = locals()['a']
				eval(___line___)
				locals()['a'] = locals()['___temporary___']
			except SyntaxError:
				locals()['___temporary___'] = locals()['a']
				globals()['a'] = locals()['a']
				exec(___line___)
				locals()['a'] = locals()['___temporary___']
	
	return ___anonymous___