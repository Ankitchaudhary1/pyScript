import os
print ("Select an option")
print ("1 Battleship")
print ("2 Exam Statistics")
print ("3 Student to Teacher")
user_ans = int(input("Enter your choice: "))
if user_ans==1:
	os.system('python battleship.py')
elif user_ans==1:
	os.system('python exam_stats.py')
elif user_ans==1:
	os.system('python students_to_teacher.py')
else:
    os.system('python main.py')