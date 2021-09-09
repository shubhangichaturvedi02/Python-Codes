from collections import Counter

no_of_test_cases = int(input("Enter No. Of Test Cases: "))

count = 0
result = list()
listOfValues = list()

while count<no_of_test_cases:
    tweets = []
    no_of_tweets = int(input("Enter No. Of tweets: "))
    
    for i in range(no_of_tweets):
        tweet = input("Enter your name and tweet Id(Format: dhoni tweet_id_10): ")
        tweets.append(tweet)
        
    names = [name.split()[0] for name in tweets]
    x = Counter(names)
    itemMaxValue = max(x.items(), key=lambda y: y[1])
    listOfNames = list()
    
    listOfKey = list()
    # Iterate over all the items in dictionary to find keys with max value
    for key, value in x.items():

        if value == itemMaxValue[1]:
            listOfKey.append(key)
        
    listOfValues.append(itemMaxValue[1])    
    listOfKey = sorted(listOfKey)
    result.append(listOfKey)
    count = count+1

for i in range(len(result)):
    for j in result[i]:
        print(j,"",listOfValues[i])