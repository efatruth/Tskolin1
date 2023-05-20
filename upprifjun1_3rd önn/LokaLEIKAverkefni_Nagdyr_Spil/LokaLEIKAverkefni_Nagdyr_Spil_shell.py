Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
Traceback (most recent call last):
  File "C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py", line 6, in <module>
    from klasar.klasi1 import *
ModuleNotFoundError: No module named 'klasar'
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
Traceback (most recent call last):
  File "C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py", line 34, in <module>
    nagdyrin.append(nagdyr("mus",1))
  File "C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py", line 13, in __init__
    self.aflid = randint(2, 6, 2)
TypeError: randint() takes 3 positional arguments but 4 were given
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
[<__main__.nagdyr object at 0x0029ACF0>, <__main__.nagdyr object at 0x02C90CB0>, <__main__.nagdyr object at 0x02D122D0>, <__main__.nagdyr object at 0x02D12A90>, <__main__.nagdyr object at 0x02D12AB0>]
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
Traceback (most recent call last):
  File "C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py", line 9, in <module>
    class nagdyr:
  File "C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py", line 17, in nagdyr
    __repr__ = __str__
NameError: name '__str__' is not defined
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
Traceback (most recent call last):
  File "C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py", line 33, in <module>
    nagdyrin.append(nagdyr("mus",1))
TypeError: __init__() takes 1 positional argument but 3 were given
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
Traceback (most recent call last):
  File "C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py", line 38, in <module>
    print(nagdyrin.upplysingar())
AttributeError: 'list' object has no attribute 'upplysingar'
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
Traceback (most recent call last):
  File "C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py", line 39, in <module>
    print(nagdyr.upplysingar())
  File "C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py", line 16, in upplysingar
    return "nagdyr (" + str(self.tegundin) + ", " + str(self.staðdetning) + ", " + str(self.aflid) + ")"
AttributeError: 'nagdyr' object has no attribute 'staðdetning'
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
Traceback (most recent call last):
  File "C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py", line 39, in <module>
    print(nagdyr.upplysingar())
AttributeError: 'nagdyr' object has no attribute 'upplysingar'
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
Traceback (most recent call last):
  File "C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py", line 41, in <module>
    print(nagdyr.prenta())
  File "C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py", line 28, in prenta
    print(self.tegundin,"sem er staðsettur",self.stadsetningin,"og er með",self.aflið,"sem afl.")
AttributeError: 'nagdyr' object has no attribute 'aflið'
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
mus sem er staðsettur 1 og er með 6 sem afl.
None
hamstur sem er staðsettur 3 og er með 6 sem afl.
None
rotta sem er staðsettur 64 og er með 6 sem afl.
None
rotta sem er staðsettur 62 og er með 2 sem afl.
None
rotta sem er staðsettur 69 og er með 2 sem afl.
None
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
mus sem er staðsettur 1 og er með 2 sem afl.
hamstur sem er staðsettur 47 og er með 6 sem afl.
rotta sem er staðsettur 34 og er með 4 sem afl.
rotta sem er staðsettur 33 og er með 4 sem afl.
rotta sem er staðsettur 42 og er með 6 sem afl.
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
mus sem er staðsettur 1 og er með 2 sem afl.
hamstur sem er staðsettur 97 og er með 6 sem afl.
rotta sem er staðsettur 98 og er með 4 sem afl.
rotta sem er staðsettur 99 og er með 2 sem afl.
rotta sem er staðsettur 29 og er með 4 sem afl.
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
mus sem er staðsettur 1 og er með 6 sem afl.
hamstur sem er staðsettur 92 og er með 6 sem afl.
rotta sem er staðsettur 9 og er með 2 sem afl.
rotta sem er staðsettur 24 og er með 6 sem afl.
rotta sem er staðsettur 15 og er með 4 sem afl.
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
nagdyr (mus, 1, 6)
nagdyr (hamstur, 77, 4)
nagdyr (rotta, 44, 4)
nagdyr (rotta, 26, 2)
nagdyr (rotta, 18, 4)
mus sem er staðsettur 1 og er með 6 sem afl.
hamstur sem er staðsettur 77 og er með 4 sem afl.
rotta sem er staðsettur 44 og er með 4 sem afl.
rotta sem er staðsettur 26 og er með 2 sem afl.
rotta sem er staðsettur 18 og er með 4 sem afl.
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
nagdyr (mus, 1, 2)
nagdyr (hamstur, 8, 2)
nagdyr (rotta, 20, 6)
nagdyr (rotta, 26, 2)
nagdyr (rotta, 17, 6)
mus sem er staðsettur 1 og er með 2 sem afl.
hamstur sem er staðsettur 8 og er með 2 sem afl.
rotta sem er staðsettur 20 og er með 6 sem afl.
rotta sem er staðsettur 26 og er með 2 sem afl.
rotta sem er staðsettur 17 og er með 6 sem afl.
<bound method nagdyr.upplysingar of <__main__.nagdyr object at 0x02D43070>>
tegund nagdýrs er rotta
tegundun er: rotta
>>> 
 RESTART: C:\Users\HP\Documents\forritun bu\upprifjun1\LokaSkilaverkefni201117\LokaSkilaverkefni201117.py 
nagdyr (mus, 1, 2)
nagdyr (hamstur, 90, 2)
nagdyr (rotta, 23, 4)
nagdyr (rotta, 40, 4)
nagdyr (rotta, 57, 6)
mus sem er staðsettur 1 og er með 2 sem afl.
hamstur sem er staðsettur 90 og er með 2 sem afl.
rotta sem er staðsettur 23 og er með 4 sem afl.
rotta sem er staðsettur 40 og er með 4 sem afl.
rotta sem er staðsettur 57 og er með 6 sem afl.
nagdyr (rotta, 23, 4)
tegund nagdýrs er rotta
tegundun er: rotta
>>> 
