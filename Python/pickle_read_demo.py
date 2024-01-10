import pickle

file = open("student_data", "rb")
student = pickle.load(file)
file.close()
print(student)