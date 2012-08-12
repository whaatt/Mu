def mu(___function___):
	def ___anonymous___(a=0):
		def t(a):
			return ___anonymous___(a)
			
		___code___ = ___function___.split(';')
		
		___codes___ = []
		___lines___ = []
		___posit___ = 0
		
		while ___posit___ < len(___code___):
			if ___code___[___posit___] == '' and len(___codes___) > 0:
				___new___ = ___codes___[len(___codes___)-1] + ';' + ___code___[___posit___+1]
				___codes___.pop()
				___codes___.append(___new___)
				___posit___ = ___posit___ + 2
				
			else:
				___codes___.append(___code___[___posit___])
				___posit___ = ___posit___ + 1
		
		for ___part___ in range(len(___codes___)):
			___codes___[___part___] = ':' + ___codes___[___part___].strip()
			
		___codes___ = ['def ___output___(a,t):'] + ___codes___ + ['return ___output___(a,t)']
		
		for ___pos___ in range(len(___codes___)):
			___tabs___ = 0
			___updated___ = ___codes___[___pos___]
			
			for ___seq___ in [['\\','\\\\'],['\n','\\n'],['\t','\\t']]:
				___updated___ = ___updated___.replace(___seq___[0], ___seq___[1])
			
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
				
			exec(___line___)
					
	return ___anonymous___