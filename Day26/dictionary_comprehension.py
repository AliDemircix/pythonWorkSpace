# new_dict= {new_key:new_value for item in list}

# new_dict= {new_key:new_value for (key,value) in dict.items()}

#CONDITIONS

# new_dict= {new_key:new_value for (key,value) in dict.items() if test}

import random
import pandas as pd

names=["Ali","Alex","Carolina","Freddie","Alexsander"]

students_scores= {student:random.randint(1,100) for student in names} #{'Ali': 90, 'Alex': 12, 'Carolina': 25, 'Freddie': 3, 'Alexsander': 78}

passed_students = {student:score for (student,score) in students_scores.items() if score >=60 } #{'Ali': 70, 'Carolina': 88}
print(passed_students)

student_dict={
    "student":["Ali","Alex","Carolina"],
    "score":[42,25,12]
}


df=pd.DataFrame(student_dict)
# loop rows of a data frame
for (index,row)in df.iterrows():
    print(row)
    print(row.student)
    print(row.score)
