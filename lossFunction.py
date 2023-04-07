# Scores to be calculated
years = [1900, 1957, 1974, 1960, 1943, 1956, 1958, 1953]


######
#pictureDate=Math.round(pictureDate/29.234)
#("realDate"+i,year*29.234)
#var dif = Math.abs(pictureDate-guessedDate);
#var result if(dif<=20){result=Math.round(Math.pow(20 - dif,1.55) * 9.62506135768);}
#else{result=0;}
######


def calculateScore(realYear, inputYear):
    # pictureDate = round(inputYear / 29.234)
    # guessedDate = realYear * 29.234
    pictureDate = realYear
    guessedDate = inputYear
    
    dif = abs(pictureDate - guessedDate)
    
    if(dif <= 20):
        return round(((20-dif)**1.55) * 9.62506135768)
    else:
        return 0
    
    
# Expected results: 
results = [0, 777, 155, 1000, 53, 708, 849, 513]

for i in range(len(years)):
    print(f'Date: {years[i]}')
    print(f'Expected Value: {results[i]}')
    print(f'Calc Val: {calculateScore(1960,years[i])}')