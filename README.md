**Commands:**
write - prints something, number or string or boolean (booleans like python booleans)
var - makes a variable
if - if statement
fun - creates a function
class - creates a class (you can add Python self.thing)
while - while keyword
prompt - takes input
install - install something (python libraries)
**Examples:**
write()
```sno
write('Hello! Sno Code!')
>>> Hello! Sno Code
```
var
```sno
var devs = "ZDev1 & KobeFF"
write(devs)
>>> ZDev1 & KobeFF
```
prompt
```sno
var name = prompt('What is your name? ')
write('Hey ' + name + '!')
>>> What is your name? ZDev1
>>> Hey ZDev1!
```
if
```sno
var name = "ZDev1"
if name == "ZDev1":
  write('you are ZDev1!')
else:
  write('Who are you?')
```
*lol*
fun
```sno
fun function():
  write('this')
  write('in')
  write('function')
function()
>>> this
>>> in
>>> function
```
> class
> ```sno
> class Player:
>   fun __init__(self):
>     self.name = prompt('What is your name?\n> ')
>     self.age = prompt('How old are you?\n> ')
>   fun  greet(self):
>     print(f'Hey, {self.name}!\nYou are {self.age}!')
> player = Player()
> player.greet()
> >>> What is your name?
>     > ZDev1
> >>> How old are you?
>     > 11
> >>> Hey, ZDev1!
>     You are 11!
> ```
> while
> ```sno
> var s = 0
> while s != 0:
>   s += 1
>   write(s)
> >>> 1
> >>> 2
> >>> 3
> >>> 4
> >>> 5
> >>> 6
> >>> 7
> >>> 8
> >>> 9
> >>> 10
> ```
> install
> ```sno
> install random
> var num = random.randint(1,100)
> write(num)
> >>> 73
> ```
