liste = [0,1,2,3,4,5,6,7,8,9]
average = 0

for i in range(0,len(liste)):
    average += liste[i]

average = average/len(liste)
print('The average of the list values is : ', average)
