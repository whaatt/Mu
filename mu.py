#inline specifies that the input is given in a single or double quoted string
#inline input flag is set by default and can be specified otherwise manually

#recurseName specifies what function name should be used for recursion
#the default recursion function name is this; can be specified manually

def mu(function, inline = True, recurseName = 'this', paramName = 'param'):
    #define our anonymous function
    #a is the parameter passed into
    #our anonymous function
    
    def anonymous(param = 0):
        #handle recursive function name
        def this(param = 0): return anonymous(param)
        locals()[recurseName] = locals()['this']
        del locals()['this'] #recurseName replaced
        
        locals()[paramName] = locals()['param']
        del locals()['param'] #paramName replaced
        
        try: #handle potential index error
            if inline : #if function not specified in triple quotes
                code = function.strip().strip(';:').split(';')
                
                segs = []
                lines = []
                position = 0
                
                #blank lines are actually demarcated with two
                #semicolons, which we define in the spec for Mu
                #to be converted to single semicolons; in other
                #words, semicolon is the escape character for an
                #arbitrary number of semicolons
                
                #iterate through lines
                while position < len(code):
                    if code[position] == '' and len(segs) > 0:
                        #pop the last segment and add semicolon and next line
                        newLast = segs[len(segs) - 1] + ';' + code[position + 1]
                        
                        segs.pop()
                        segs.append(new)
                        
                        #skip two lines for semicolon
                        position = position + 2
                        
                    else:
                        #append line to segments
                        segs.append(code[position])
                        position = position + 1
                
                #indent all segments [see next]
                for part in range(len(segs)):
                    segs[part] = ':' + segs[part].strip()
                    
                #add a wrapper function so we can directly call exec() on it
                #and have it return a valid function without any more hacks
                segs = ['def output(' + paramName + ', ' + recurseName + '):'] + segs
                segs += ['return output(' + paramName + ', ' + recurseName + ')']
                
                #various indentation and escape tasks
                for pos in range(len(segs)):
                    tabs = 0
                    newSeg = segs[pos]
                    
                    #convert escape sequences in strings that are not escapes
                    for seq in [['\\', '\\\\'], ['\n', '\\n'], ['\t', '\\t']]:
                        newSeg = newSeg.replace(seq[0], seq[1])
                    
                    #convert colons to tabs
                    for char in newSeg:
                        if char == ':': tabs = tabs + 1
                        else: break
                    
                    #put code blocks in the same exec() call
                    #lines contains blocks classified by tabs
                    
                    if tabs > 0:
                        newSeg = '\t' * tabs + newSeg[tabs:]
                        newSeg = lines[len(lines) - 1] + '\n' + newSeg
                        lines.pop()
                    
                    #add processed segment
                    lines.append(newSeg)
                    
            else: #triple quote string mode
                #split by newline rather than semicolon
                code = function.strip('\n').split('\n')
                
                #standardize our tabs because tabs only need to be
                #internally consistent within the triple quotes and
                #not with respect to the program as a whole
                
                while False not in [line[0:4] == '    ' or line[0] == '\t' for line in code]:
                    if code[0][0] == '\t': code = [line[1:] for line in code]
                    elif code[0][0:4] == '    ': code = [line[4:] for line in code]
                
                #add one tab back for wrapper function
                code = ['\t' + line for line in code]
                
                #add newlines back
                code = '\n'.join(code)
                
                #add a wrapper function so we can directly call exec() on it
                #and have it return a valid function without any more hacks
                lines = ['def output(' + paramName + ', ' + recurseName + '):\n' + code + '\n']
                lines += ['return output(' + paramName + ', ' + recurseName + ')']
                
            for line in lines:  
                if line[0:7] == 'return ':
                    #deal with variable conflicts in recursion
                    #save our function parameter variable
                    #at any given level of recursion or depth
                    
                    locals()['_paramTemp'] = locals()['paramName']
                    globals()['paramName'] = locals()['paramName']
                    recursiveOutput = eval(line[7:])
                    locals()['paramName'] = locals()['_paramTemp']
                    
                    #send output straight back up
                    return recursiveOutput
                
                #the magic
                exec(line)
                
        except IndexError: #deal with empty functions
            raise SyntaxError('Function cannot be empty.')
    
    #return our trickery
    return anonymous