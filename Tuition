tuition = 8000.00

Round = lambda x, n: eval('"%.'+str(int(n))+'f" % '+repr(int(x)+round(float('.'+str(float(x)).split('.')[1]),n)))
for counter in range (1,2):
    tuition= round(tuition * 1.03,2)
    print ("In",counter, "year, the tuition will be $"+str(round(tuition,2))+"0.")
    new_tuition = round(tuition * 1.03,2)
for counter in range (2,6):
    print ("In",counter,"years, the tuition will be $"+str(Round(new_tuition,2))+".")
    new_tuition = round(new_tuition * 1.03,3)
