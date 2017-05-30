import random

# define the function
# set returns based on the number passed in
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

# the number you are passing in
r = random.randint(1,9)
# set a var for the return
# call the function and pass in your random number
fortune = getAnswer(r)
# console display of the answer
print(fortune)
# show the number that was passed in
print("the number passed in was " + str(r))