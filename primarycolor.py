# Project 2 Chapter 3
color1 = str(input('Enter primary color:'))
color2 = str(input('Enter primary color:'))
                                                                                            
# Defining the color Purple
if color1 == 'red' and color2 == 'blue'or color1 == 'blue' and color2 == 'red':
    print('When you mix red and blue, you get purple.')
                                                                                            
# Defining the color Orange
elif color1 == 'red' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'red':
    print('When you mix ' + color1 + ' and ' + color2 + ', you get orange.')
                                                                                            
# Defining the color Green
elif color1 == 'blue' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'blue':
    print('When you mix blue and yellow, you get green.')

# Defining the color entered in not a Primary
else:
    print("You didn't input two primary colors.")
