# ['write', 'var', 'if ', 'fun ', 'class ', 'while ', 'install ']
import os
def main():
 #opens files
 openshell = input('<<Would you like to use Sno Code shell? y/n>>')
 if openshell == 'y':
   exec(open('snoshellMain.py').read())
 makefile = input('<<Would you like to make a file? y/n>>')
 if makefile == 'y':
   name = input('<<What would you like to name your file?>>')
   f= open(name + ".sno","w+")
   f.close()
   main()
 directory = input('<<directory>>')
 IF_input = input('<<name of sno code file>>') + '.sno'
 print('the Sno Code file', IF_input, 'has now be opened')
 IF = open(os.path.join(directory)+ IF_input, "rt")
 OF = open("out.py", "wt")
 #list of the "commands"
 clist = ['write', 'var', 'if ', 'fun ', 'class ', 'while ', 'install ']
 #changes words
 for line in IF:
	 if 'write' in line:
		 OF.write(line.replace('line', 'print'))
	 if 'var ' in line:
		 OF.write(line.replace('var ', ''))
	 if 'if ' in line and 'else if' not in line:
		 OF.write(line.replace('if ', 'if '))
	 if 'else if' in line:
		 OF.write(line.replace('else if', 'elif'))
	 if 'else: ' in line:
		 OF.write(line.replace('else: ', 'else:'))
	 if 'fun ' in line and 'define run ' not in line:
		 OF.write(line.replace('fun ', 'def '))
	 if 'class ' in line:
		 OF.write(line.replace('class ', 'class '))
	 if 'while ' in line:
		 OF.write(line.replace('while ','while '))
	 if 'install ' in line:
		 OF.write(line.replace('install ','import '))
	 if 'for ' in line:
		 OF.write(line.replace('for ','for '))
	 if '*' in line:
		 OF.write(line.replace('*','#'))
 #closes files
 IF.close()
 OF.close()
 #runs python file
 exec(open("out.py").read())
 main()

main()
