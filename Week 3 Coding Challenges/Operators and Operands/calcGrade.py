#   SCRIPT: calcGrade.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: A python program that helps calculate the grades of students. A final letter grade is returned based off of an averaged
#               percentage computed across five subjects.

#Function that returns a particular letter grade based off the conditional score paramaters
def letterGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#Receives the scores as an input for each subject while also checking that the score is within 0 and 100!
print("Please enter the scores received for each subject:")
while True:
    try:
        firstSub = float(input("First subject: "))
        secondSub = float(input("Second subject: "))
        thirdSub = float(input("Third subject: "))
        fourthSub = float(input("Fourth subject: "))
        fifthSub = float(input("Fifth subject: "))

        if (firstSub or secondSub or thirdSub or fourthSub or fifthSub) < 0 or (firstSub or secondSub or thirdSub or fourthSub or fifthSub) > 100:
            raise ValueError
        break
    except ValueError:
        print("An above subject score is not within bounds! Please enter scores between 0 and 100!")

#Stores the inputs received into a list subSum
subSum = [firstSub, secondSub, thirdSub, fourthSub, fifthSub]

#Returns the average of sumSub (which was the total combined score of the five subjects)
avgScore = sum(subSum)/len(subSum)

#Passes in avgScore (which was the average of the subSum) into the letterGrade() function to return the final grade
finalGrade = letterGrade(avgScore)

#Prints the final grade as the output
print("The final grade is:", finalGrade)
