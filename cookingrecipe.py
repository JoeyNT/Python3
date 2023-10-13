#Chapter 2: Project 1
n_cookies = int(input('Enter number of cookies:'))
butter = str(round(n_cookies * 0.02083333,2))
sugar = str(round(n_cookies * 0.03125,2))
flour = str(round(n_cookies * 0.05729167,3))
print ('You need ' + sugar +(' cups of sugar, ') + butter + (' cups of butter, and ') + 
flour +(' cups of flour.'))
