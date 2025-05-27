from datetime import datetime


dt = datetime(2024, 1, 15, 9, 3, 32, 744178)


extract_components = lambda dt: (dt.year, dt.month, dt.day, dt.time())


year, month, day, time = extract_components(dt)
print(dt)         
print(year)      
print(day)        
print(time)       
