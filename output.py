Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>>  25 / 5
 
SyntaxError: unexpected indent
>>> 
>>> 25 / 5
5.0
>>> 10 /3
3.3333333333333335
>>> 10 //3
3
>>> print('Tim')
Tim
>>> naam = ""Tim de vries"
SyntaxError: invalid syntax
>>> naam = "Tim de vries"
>>> print(naam)
Tim de vries
>>> print(naam.upper)
<built-in method upper of str object at 0x00000267A0DC30F0>
>>> print(naam.upper())
TIM DE VRIES
>>> print([0,2])
[0, 2]
>>> print(naam[0:2)
      
SyntaxError: invalid syntax
>>> print(naam[0:2])

Ti
>>> print(naam[::-1)
      
SyntaxError: invalid syntax
>>> print(naam[::-1])
seirv ed miT
>>> leeftijd = 15
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Tim de vries ben je al 15 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
16
>>> leeftijd-=1
>>> leeftijd

15
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
	hoelang_al18jaar = leeftijd - 18
	print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
	print('Je bent precies ' + str(leeftijd) + ' jaar')

	
Over 3 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)
161
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
984
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))

Willekeurig getal tussen 0 en 1000: 984
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 14:49:23.459583
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 09 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')

'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'
>>> 