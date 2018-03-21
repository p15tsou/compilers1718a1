def getchar(words,pos):
	""" returns char at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None

	return words[pos]
	

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
		
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char
			
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary

# Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων...
td = { 'q0':{ '0':'q4','1':'q1','2':'q3','3':'q2','4':'q2','5':'q2','6':'q2','7':'q2','8':'q2','9':'q2'},
       'q1':{ '0':'q2','1':'q2','2':'q2','3':'q2','4':'q2','5':'q2','6':'q2','7':'q2','8':'q2','9':'q2','.':'q5',':':'q5'},
       'q3':{ '0':'q2','1':'q2','2':'q2','3':'q2','.':'q5',':':'q5'},
       'q2':{ '.':'q5',':':'q5' },
       'q5':{ '0':'q6','1':'q6','2':'q6','3':'q6','4':'q6','5':'q6' },
       'q6':{ '0':'q7','1':'q7','2':'q7','3':'q7','4':'q7','5':'q7','6':'q7','7':'q7','8':'q7','9':'q7' },
       'q4':{ '0':'q2','1':'q2','2':'q2','3':'q2','4':'q2','5':'q2','6':'q2','7':'q2','8':'q2','9':'q2'}
     } 

# the dictionary of accepting states and their
# corresponding token

# Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής...
ad = { 'q7':'TIME_TOKEN'
        
     }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print('unrecognized input at pos',position+1,'of',text)
		break
	
	print("token:",token,"string:",text[:position])
	break
	
	# remaining text for next scan
	text = text[position:]

