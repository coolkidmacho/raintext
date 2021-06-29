# Raintext
A small script for making rainbow colored text in python

Step: 1

Place the raintext.py file into any directory that it is needed.


Usage: 
```py
from raintext import rain

print(rain("Hello there."))
print(rain("How are you?"))
```
<img src="http://i.prntscr.com/I5kphhaFQ8mFw8OIgerl_g.png"
     alt="Screenshot 1"/><br><br>
An optional argument you could run with the could is `color_space: bool`, this will make the program apply colors to the spaces. This is good if you want uniformity between the lines. By default it is coloring spaces, you can disable this with the following code. This defaults to False.

Usage:
```py
from raintext import rain

print(rain("Hello there.", color_space=True))
print(rain("How are you?", color_space=True))
```
<img src="http://i.prntscr.com/yuRqVdMfRp6YIODqXtpcwQ.png"
     alt="Screenshot 2"/>

# Made by Coolkidmacho#0001 on discord
