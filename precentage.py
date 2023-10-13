#Chapter 2: Projecct 2
n_males = int(input('Enter number of males:'))
n_females = int(input('Enter number of females:'))
total_m_f = n_males + n_females
percent_male = round((n_males / total_m_f) * 100,0)
percent_male_round = str(int(percent_male))
percent_female = str(int((n_females / total_m_f) * 100 ))
print( 'Percent males: ' + percent_male_round + '%')
print('Percent females: ' +percent_female + '%')
