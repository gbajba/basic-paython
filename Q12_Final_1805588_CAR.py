
#Ghida'a Nasser Bajba
#1805588
#CAR


sen=input("Enter a Sentence: ");
i=0
count=1

while i< len(sen):
    if sen[i]== " ":
        count = count +1
    i=i+1
print("Number of words: ",count)
