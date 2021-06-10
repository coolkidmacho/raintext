# Raintext
A small script for making rainbow colored text in python

Step: 1

Place the raintext.py file into any directory that it is needed.


Usage: 
```
from raintext import rain

text = rain("Hello there.")
text2 = rain("How are you?")
print(text)
print(text2)

```
<img src="http://i.prntscr.com/I5kphhaFQ8mFw8OIgerl_g.png"
     alt="Screenshot 1"/><br>
An optional arguament you could run with the could is color_space=False/True, this will make the program apply colors to the spaces. This is good if you want uniformity between the lines. By default it is coloring spaces, you can disable this with the following code.

Usage:
```
from raintext import rain

text = rain("Hello there.", color_space=False)
text2 = rain("How are you?", color_space=False)
print(text)
print(text2)


```
<img src="http://i.prntscr.com/yuRqVdMfRp6YIODqXtpcwQ.png"
     alt="Screenshot 2"/>

