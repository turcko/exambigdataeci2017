import random as rn

dataFile = open("dataSet.txt", "w")

#I used this amount of data (nothing), but is only for test :D
for i in range(10000):
    year = rn.randint(1986, 2017)
    temperature = rn.randint(-10, 45) #Celcius degrees
    humidity = rn.randint(0, 100)

    data = str(year)+'	'+str(temperature)+'	'+str(humidity)+'\n'
    dataFile.write(data)

dataFile.close()
