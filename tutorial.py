# int
lesson_number = 1

print(lesson_number, type(lesson_number))

# string

lesson_name = "python tutorial"

print(lesson_name, type(lesson_name))

# list

tweet_lenghts = [140, 80, 20, 105]

print(tweet_lenghts, type(tweet_lenghts))

# tuple

tweet_lenghts_immutable = (140, 80, 20, 105)

print(tweet_lenghts_immutable, type(tweet_lenghts_immutable))

# dict

tweets_by_user = {
    'John': [1, 15],
    'Mary': [2, 5]
}

print(tweets_by_user, type(tweets_by_user))

print(tweets_by_user['John'])

x = ['test']

if type(x) == int:
    print("This is int")
elif type(x) == str:
    print("This is str")
else:
    print("I don't know")

for tweet in tweet_lenghts:
    print(tweet)
    print("test")
