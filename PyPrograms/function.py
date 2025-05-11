def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses = ['Maths','Programming']
info = {'name':'John','class':'first','age':28}

print(student_info(*courses,**info))
