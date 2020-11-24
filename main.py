from pyCpp import PyCpp

filename = 'main.cpp'

sec1 = PyCpp(filename)
sec1.compile()
output = sec1.run('3','4','hello','hi','geeks')
print("Result: ")
print(output)