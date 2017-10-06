import matplotlib.pyplot as plt
f = open('database.txt','r')
page_number = []
page = f.readlines()
for x in range(len(page)):
    page_number.append(x)
print len(page_number)
print len(page)