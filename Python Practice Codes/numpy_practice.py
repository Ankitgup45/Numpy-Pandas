#Student Marks Analysis
import numpy as np

Marks = np.array([
    [85, 78, 90],
    [60, 65, 70],
    [95, 88, 92],
    [45, 50, 55],
    [72, 80, 75]
])
#print(Marks)
#print(Marks[2,1])# tells location
#print(Marks.shape) #tells size
#print(Marks.ndim) #tells how many dimensions
#print(Marks.dtype) #tells the data type of element
#print(Marks[0]) # returns first students marks
#print(Marks[-1])# returns last students marks
#print(Marks[:,0] >60)# returns more than 60 marks from first column
#print(Marks[0,:])# returns all values from first rows means all marks for first student
math_marks = Marks[:, 0]
print(math_marks[math_marks > 75])
