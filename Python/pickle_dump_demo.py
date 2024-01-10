import pickle

student = [{'name' : 'John Doe', 'age' : 25, 'grade' : 'A'},
           {'name' : 'Omkar Pathak', 'age' : 23, 'grade' : 'A+'}]

file = open('student_data','wb')
pickle.dump(student, file)
file.close()