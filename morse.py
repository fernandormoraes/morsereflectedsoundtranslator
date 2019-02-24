import sys  

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}  

def decrypt(s):     
	return ''.join(CODE_REVERSED.get(i) for i in s.split())  

filemorse = str(sys.argv[1]) 
print(filemorse)  
lin = open(filemorse).read().replace('\n', ' ') 
out = open(filemorse, 'w') 
replacements = {'dah':'-', 'di':'.', 'dit':'.', '-':''} 
for i in replacements.keys():     
	lin = lin.replace(i, replacements[i]) 
out.write(lin) 
out.close 
print(decrypt(lin))  
