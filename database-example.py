import sqlite3
conn = sqlite3.connect('Subjects.db')
modulelist = []
a = 'OOP'
c = conn.cursor()
for row in c.execute('SELECT modules FROM SUBJECTS'):
    modulelist.append(str(row))

print (modulelist)

# Save (commit) the changes
conn.commit()
