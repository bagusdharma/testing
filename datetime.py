from datetime import datetime
now = datetime.now()

print '%02d-%02d-%04d' % (now.month, now.day, now.year)
# will print the current date as mm-dd-yyyy
# %02d, %04d => banyak nya place ex : 0000, 00

print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

# latihan 

print ('%02d-%02d-%04d %02d:%02d:%02d') % (now.month, now.day, now.year,now.hour, now.minute, now.second)