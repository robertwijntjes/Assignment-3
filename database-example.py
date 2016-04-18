import sqlite3
conn = sqlite3.connect('Subjects.db')
modulelist_gross = []
modulelist_net = []
a = 'OOP'
c = conn.cursor()
for row in c.execute('SELECT modules FROM SUBJECTS'):
    print (row)
    modulelist_gross.append(row)

for i in modulelist_gross:
    swapper = i
        

print (modulelist_gross)

# Save (commit) the changes
conn.commit()
print (modulelist_net)
