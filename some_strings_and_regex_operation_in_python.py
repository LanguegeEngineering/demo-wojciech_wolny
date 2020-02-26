# -*- coding: utf-8 -*-
"""Some_strings_and_regex_operation_in_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AsejQBaQ9iQ0HNQ2vB7S0x8YKOz1MJ4C

### Easy string manipulation
"""

x = 'a string'
y = "a string"
if x == y:
    print("they are the same")

fox = "tHe qUICk bROWn fOx."

"""To convert the entire string into upper-case or lower-case, you can use the ``upper()`` or ``lower()`` methods respectively:"""

fox.upper()

fox.lower()

"""A common formatting need is to capitalize just the first letter of each word, or perhaps the first letter of each sentence.
This can be done with the ``title()`` and ``capitalize()`` methods:
"""

fox.title()

fox.capitalize()

"""The cases can be swapped using the ``swapcase()`` method:"""

fox.swapcase()

line = '         this is the content         '
line.strip()

"""To remove just space to the right or left, use ``rstrip()`` or ``lstrip()`` respectively:"""

line.rstrip()

line.lstrip()

"""To remove characters other than spaces, you can pass the desired character to the ``strip()`` method:"""

num = "000000000000435"
num.strip('0')

line = 'the quick brown fox jumped over a lazy dog'
line.find('fox')

line.index('fox')

line[16:21]

"""The only difference between ``find()`` and ``index()`` is their behavior when the search string is not found; ``find()`` returns ``-1``, while ``index()`` raises a ``ValueError``:"""

line.find('bear')

line.index('bear')

line.partition('fox')

"""The ``rpartition()`` method is similar, but searches from the right of the string.

The ``split()`` method is perhaps more useful; it finds *all* instances of the split-point and returns the substrings in between.
The default is to split on any whitespace, returning a list of the individual words in a string:
"""

line_list = line.split()
print(line_list)

print(line_list[1])

"""A related method is ``splitlines()``, which splits on newline characters.
Let's do this with a Haiku, popularly attributed to the 17th-century poet Matsuo Bashō:
"""

haiku = """matsushima-ya
aah matsushima-ya
matsushima-ya"""

haiku.splitlines()

"""Note that if you would like to undo a ``split()``, you can use the ``join()`` method, which returns a string built from a splitpoint and an iterable:"""

'--'.join(['1', '2', '3'])

"""A common pattern is to use the special character ``"\n"`` (newline) to join together lines that have been previously split, and recover the input:"""

print("\n".join(['matsushima-ya', 'aah matsushima-ya', 'matsushima-ya']))

pi = 3.14159
str(pi)

print ("The value of pi is " + pi)

"""Pi is a float number so it must be transform to sting."""

print( "The value of pi is " + str(pi))

"""A more flexible way to do this is to use *format strings*, which are strings with special markers (noted by curly braces) into which string-formatted values will be inserted.
Here is a basic example:
"""

"The value of pi is {}".format(pi)

"""### Easy regex manipulation!"""

import re

line = 'the quick brown fox jumped over a lazy dog'

"""With this, we can see that the ``regex.search()`` method operates a lot like ``str.index()`` or ``str.find()``:"""

line.index('fox')

regex = re.compile('fox')
match = regex.search(line)
match.start()

"""Similarly, the ``regex.sub()`` method operates much like ``str.replace()``:"""

line.replace('fox', 'BEAR')

regex.sub('BEAR', line)

"""The following is a table of the repetition markers available for use in regular expressions:

| Character | Description | Example |
|-----------|-------------|---------|
| ``?`` | Match zero or one repetitions of preceding  | ``"ab?"`` matches ``"a"`` or ``"ab"`` |
| ``*`` | Match zero or more repetitions of preceding | ``"ab*"`` matches ``"a"``, ``"ab"``, ``"abb"``, ``"abbb"``... |
| ``+`` | Match one or more repetitions of preceding  | ``"ab+"`` matches ``"ab"``, ``"abb"``, ``"abbb"``... but not ``"a"`` |
| ``.`` | Any character | ``.*`` matches everything | 
| ``{n}`` | Match ``n`` repetitions of preeeding | ``"ab{2}"`` matches ``"abb"`` |
| ``{m,n}`` | Match between ``m`` and ``n`` repetitions of preceding | ``"ab{2,3}"`` matches ``"abb"`` or ``"abbb"`` |
"""

bool(re.search(r'ab', "Boabab"))

bool(re.search(r'.*ma.*', "Ala ma kota"))

bool(re.search(r'.*(psa|kota).*', "Ala ma kota"))

bool(re.search(r'.*(psa|kota).*', "Ala ma psa"))

bool(re.search(r'.*(psa|kota).*', "Ala ma chomika"))

zdanie = "Ala ma kota."
wzor = r'.*' #pasuje do każdego zdania
zamiennik = r"Ala ma psa."

re.sub(wzor, zamiennik, zdanie)

wzor = r'(.*)kota.'
zamiennik = r"\1 psa."

re.sub(wzor, zamiennik, zdanie)

wzor = r'(.*)ma(.*)'
zamiennik = r"\1 posiada \2"

re.sub(wzor, zamiennik, zdanie)

