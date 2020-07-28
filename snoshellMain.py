# ['write', 'var', 'if ', 'fun ', 'class ', 'while ', 'install ']
v = ""
while 1:
 oopen = open('snoshell.py', 'w')

 x = input('>>> ')

 def replace1():
  global x
  if 'write' in x:
	  x = x.replace('write', 'print')
  if 'var ' in x:
	  x = x.replace('var ', '')
  if 'if ' in x and 'else if' not in x:
	  x = x.replace('if ', 'if ')
  if 'else if' in x:
	  x = x.replace('else if', 'elif')
  if 'else:' in x:
	  x = x.replace('else:', 'else:')
  if 'func ' in x:
	  x = x.replace('func ', 'def ')
  if 'class ' in x:
	  x = x.replace('class ', 'class ')
  if 'while ' in x:
	  x = x.replace('while ','while ')
  if 'install ' in x:
	  x = x.replace('install ','import ')
  if 'for ' in x:
	  x = x.replace('for ','for ')
  if '*' in x:
	  x = x.replace('*','#')
  if 'prompt' in x:
	  x = x.replace('prompt','input')
  if '' in x:
    pass
 replace1()
 v += x
 v += '\n'
 oopen.write(v)
 output = input('want to have output yet? y/n>>')
 if output == 'y':
  v = ''
  x = ''
  oopen.close()
  exec(open('snoshell.py', 'r').read())
  exec(open("main.py").read())
