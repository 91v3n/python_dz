# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

# x	y	z	xvy	xvyvz	⌐(xvyvz)	⌐x	⌐y	⌐x&⌐y	⌐z	⌐x&⌐y&⌐z	⌐(xvyvz) = ⌐x&⌐y&⌐z
# 0	0	0	0	0	    1	        1	1	1	    1	1	        1
# 0	0	1	0	1	    0	        1	1	1	    0	0	        1
# 0	1	0	1	1	    0	        1	0	0	    1	0	        1
# 0	1	1	1	1	    0	        1	0	0	    0	0	        1
# 1	0	0	1	1	    0	        0	1	0	    1	0	        1
# 1	0	1	1	1	    0	        0	1	0	    0	0	        1
# 1	1	0	1	1	    0	        0	0	0	    1	0	        1
# 1	1	1	1	1	    0	        0	0	0	    0	0	        1

x = int(input('правда или ложь для X '))
y = int(input('правда или ложь для Y '))
z = int(input('правда или ложь для Z '))

left = not (x or y or z)
right = (not x) and (not y) and (not z)

print (left == right)