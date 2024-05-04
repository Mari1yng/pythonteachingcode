name = input("YOUR NAME GOES HERE: ")
mean_temp_text = open('mean_temp.txt', 'a+')
mean_temp_text.write('\nRio de Janeiro,Brazil,30.0,18.0')

mean_temp_text.seek(0,0)
headings = mean_temp_text.readline()
headings = headings.split(',')

city_temp = mean_temp_text.readline().strip('\n')

while city_temp:
    city_temp = city_temp.split(',')
    print(headings[2] ,'for',city_temp[0], 'is', city_temp[2], "Celcius")
    city_temp = mean_temp_text.readline().strip('\n')
mean_temp_text.close()
