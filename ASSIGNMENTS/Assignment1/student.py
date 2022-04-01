# If there are 20 students who like football, 
# 30 students like badminton and 10 like both. 
# there are 20 who are not intrested if any of the games.
#  how many total number of students are there?
football=20
badminton=30
both=10
not_intrested=20

total_football=football-both
total_badminton=badminton-both

total_students=total_football + total_badminton + not_intrested
print("total students are= ",total_students)
