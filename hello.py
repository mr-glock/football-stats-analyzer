name = input("What is your name bro?")
team = (input("what is your favorite team?"))
superBowls = int(input(" soooo,how many super bowls have they won?"))
print("whats up",name,"!!" "your team is the",team,"and yall have won",superBowls,"super bowls congrats !!")
if superBowls == 0: print("you are not a champion!!")
elif superBowls <= 3  : print("you are a champion!!")
else : print("you are a winning franchise!!!")
wins = int(input("how many games did yall win last seaon?"))
if wins >=10 : print("thats a winning season!!")
elif wins <= 7 :print("thats a losing season!!")
else : print("thats a mid season not gonna lie")
if wins >= 10 and superBowls >= 1 :print("THIS IS AN ELITE TEAM!!")
else : print("yall arent elite yet")
if wins >= 10 and superBowls == 0 :print("so yall just cant get it done in the post season")
if wins <= 5 or superBowls == 0 :print( "that's a bad season")
if not (superBowls ==0 ) :print("your team has championship experience")
if (wins >= 10 and superBowls >=2 or wins >= 15): print("this is an ALL TIME TEAM!!!!")
if (wins >=13) :print("SUPERSTAR SEASON")
elif (wins >=10 ) :print("GREAT SEASON")
elif (wins >=6) :print("AVERAGE SEASON")
else  : print("BAD season")
rating = int(input("whats your team overall rating from 1-100?"))
if (rating >=90):print("SUPER TEAM")
elif (rating >=80):print("GOOD TEAM")
elif (rating >=70):print("DECENT TEAM")
else:print ("NEED SOME WORK")
if (rating >= 90 and wins >=10) : print("Yall are a dominant team!!!")
elif(rating >=90 and wins < 10):print ("Great roster but yall have to win more")
else:print("keep building")
if wins >=13 or rating >=95 :print("THIS TEAM IS DANGEROUS")
else : print("This team needs to improve")
def team_analysis():
    print("analyzing your team....")
team_analysis()
def team_message(team):
    print("your team is the",team)
team_message(team)
def team_summary(team, wins, rating):
    print("team:", team)
    print("wins:", wins)
    print("rating:", rating)
team_summary(team, wins, rating)
def team_score(wins, rating):
    score = wins + rating
    print("team score:", score)
    return score
score = team_score(wins, rating)
if score >= 100:
    print ("ELITE TEAM SCORE")
elif score >=90:
    print("GOOD TEAM SCORE")
else:
    print("TEAM NEEDS IMPOREMENT")
if score >= 100:
    print("my recommendation: SUPER BOWL CONTENDER")
elif score >=90:
    print("my recommendation: PLAYOFF CONTENDER")
else:
    print("my recommendation: NEEDS IMPROVEMENT")
if wins >= 12 and rating >=90:
    print("FINAL VERDICT: SUPER BOWL FAVORITE")
elif wins >=10 and rating >=80:
    print("FINAL VERDICT: PLAYOFF TEAM") 
elif wins >=8 and rating >=70:
    print("FINAL VERDICT: COMPETITIVE TEAM")
else:
    print("FINAL VERDICT: REBUILDNG")
question = input("What would you like to know about your team? ")
if question == "record":
    print("your team won" ,wins,"games" )
elif question == "rating":
    print("Your team is a" ,rating, "overall")
elif question == "score":
    print("Your team score is" , score)
elif question == "superbowl":
    print("Your team has won", superBowls, "superbowls")
else:
    print("My bad I dont understand the question yet")
def team_advice( wins, rating):
    if wins <8:
        print("You need to focus on winning more games.")
    elif rating <80:
        print("You need to improve your roster.")
    else:
        print("Your team is in good shape.")

team_advice(wins, rating) 
for i in range(5):
    print("GO FALCONS!")
for i in range(3):
    print("Win number", i)
for i in range(1,6):
     print("Game", i)
def game_report(wins, rating):
    if wins >=10:
        print("Winning team")
    elif rating >=85:
        print("Strong Roster")
    else:
        print("Team needs work")
    for i in range(1,4):
        print("Game",i)
game_report(wins, rating)
teams = ["falcons" , "bucs", "saints", "panthers"]
print(teams)
print(teams[0])
for team in teams:
   if team == "falcons":
       print("Thats my team")
   else:
       print("Thats not my team", team)
team = {
    "name": "falcons",
    "wins": 8,
    "rating":84

}
print(team)
print(team["name"])
print(team["wins"])
print(team["rating"])
team["wins"]=10
print(team)
team["superbowls"] =2
print(team)
del team["rating"]
print(team)
if "rating" in team:
    print("rating",team["rating"])
else:
    print("rating is not available")
def caculate_score(points, bonus):
    return points + bonus
print(caculate_score(25, 10))
def calculate_total(price, tax, tip):
    return price + tax + tip
print(calculate_total(20, 2, 3))
def check_score(score):
    if score >= 70:
        return("pass")
    else:
        return("fail")
print(check_score(70))
def get_grade(score):
    if score >=90:
        return("A")
    elif score >= 80:
        return("B")
    elif score >= 70:
        return("C")
    elif score >= 60:
        return("D")
    else:
        return("F")
print(get_grade(82))
def check_eligibility(gpa):
    if gpa >= 3.0:
        return("ElIGIBLE")
    else:
        return("NOT ELIGIBLE")
print(check_eligibility(3.5))
def check_application(gpa, projects):
    if gpa >= 3.0 and projects >= 2:
        return("STRONG CANIDATE")
    elif gpa >= 3.0 and projects < 2:
        return("NEED MORE PROJECTS")
    elif gpa <3.0:
        return("IMPROVE GPA")
print(check_application(3.5, 1))
def evaluate_canidate(gpa, projects, experience):
    if gpa >= 3.5 and projects >= 3 and experience >= 2:
        return("EXCELLENT CANIDATE")
    elif gpa >= 3.0 and projects >= 2 and experience >= 1:
        return("INTERVIEW REAdy")
    else:
        return("KEEP PREPARING")
print(evaluate_canidate(3.4, 1, 2))
scores = [85, 72, 91, 64, 78]
count = 0
for score in scores:
    if score >= 80:
     count += 1
print(count)
total = 0
for score in scores:
    total += score
print(total)
average = total/len(scores)
print(average)
highest = 0
for score in scores:
    if score > highest:
        highest = score
print(highest)
lowest = 100
for score in scores:
    if score < lowest:
        lowest = score
print(lowest)
count = 0
for score in scores:
    if score > average:
        count +=1
print(count)
passing_scores = []
for score in scores:
    if score >= 70:
        passing_scores.append(score)
print(passing_scores)
failing_scores = []
for score in scores:
    if score < 70:
        failing_scores.append(score)
print(failing_scores)
excellent_scores = []
for score in scores:
    if score >= 85:
        excellent_scores.append(score)
print(excellent_scores)
below_average =[]
for score in scores:
    if score < average:
        below_average.append(score)
print(below_average)
bouns_score = []
for score in scores:
    bouns_score.append(score + 5)
print(bouns_score)
high_scores = []
for score in scores:
    if score >= 80:
        high_scores.append(score + 5)
print(high_scores)
students = [
    [85,90,78],
    [72, 88,91],
    [64, 70, 75],
]
student_number = 1
for student in students:
    total = 0

    for score in student:
        total += score

    average = total/len(student)
    print(f"student {student_number}: , {average:.2f}")

    student_number += 1
scores = [85, 72, 91, 78, 64, 90, 77, 96, 69, 83]

highest = max(scores)
lowest = min(scores)

print("highest:", highest)
print("lowest:", lowest)

numbers = [12, 45, 7, 89, 23]

print(sum(numbers))
scores = [85, 92, 78, 95 ]

total = sum(scores)
count = len(scores)
average = total / count

print("total:", total)
print("count:",count)
print("average:",average)

if average >= 95:
    print("outstanding")
elif average >= 85:
    print("excellent")
elif average >= 75:
    print("good")
else:
    print("AVERAGE NEEDS IMPROVEMENT")
name = input("enter your name:")
score1 = int(input("enter first score"))
score2 = int(input("enter second score"))
score3 = int(input("enter third score"))
total = score1 + score2 + score3
average = total / 3
print("name:", name)
print("average:",average)
if average >= 90:
    print ("A")
elif average >= 80:
    print ("B")
elif average >= 70:
    print("C")
else:
    print("NEEDS IMPROVEMENT")
number = 0
while number < 5:
    number = int(input("enter a number 5 or higher"))
print("You made it")
scores = []
for i in range(3):
    score = int(input("enter yout score here:"))
    scores.append(score)
total = sum(scores)
average = total /len(scores)
highest = max(scores)
lowest = min(scores)
print("scores:" ,scores)
print("average:",round(average, 2))
print("highest:", highest)
print("lowest:", lowest)
def get_grade(average):
    if average >= 90:
        return("A")
    elif average >= 80:
        return("B")
    elif average >= 70:
        return("C")
    else:
        return ("NEEDS IMPROVEMENT")
def get_status(average):
    if average >= 70:
        return("PASSING")
    else:
        return ("FAILING")
grade = get_grade(average)
status = get_status(average)
print("grade:", grade)
print("status:", status)
def score_analyzer(scores):
    average = sum(scores)/len(scores)
    highest = max(scores)
    lowest = min(scores)

    return average , highest, lowest
average , highest, lowest = score_analyzer(scores)





        
    
    
     


    


       
