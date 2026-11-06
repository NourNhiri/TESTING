months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
numMonths=[f"{i}. {month[0:3].upper()}" for i,month in enumerate(months,1) if len(month)<=5]
print(numMonths)
"""zo houd ik ook nog de originele maand namen. sorry dit maakte meer sense voor mij"""


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
numMonths=[f"{i}. {month[0:3].upper()}" for i,month in enumerate([m for m in months if len(m)<=5],1) ]
print(numMonths)