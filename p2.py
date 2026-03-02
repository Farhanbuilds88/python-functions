##program 2 length of list using function
cities=["rawalpindi","islamabad","karachi","peshawar","lahore"]
actors=["saaed","fahad","sharukh","salman"]
def actor_len(actors):
    print(len(actors))
    for j in actors:
        print(actors,end=" ")
def print_len(cities):
    print(len(cities))
    for k in cities:
        print(cities,end=" ")

print("the length of list1 is:",len(cities))
print(cities)
print("the length of second list is:",len(actors))
print(actors)

countries=["pakistan","india","bangladesh","srilanka","nepal"]
def len_countries(countries):
    print(len(countries))
    for country in countries:
        print(country, end=" ")

print("the length of third list is",len(countries))
print(countries)

universities=["fast","air","pias","bahria","numl","Gik"]
def universities_len(universities):
    print(len(universities))
    for z in universities:
        print(universities,end=" ")
print("the length of last list is",len(universities))
print(universities)