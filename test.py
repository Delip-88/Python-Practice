from datetime import datetime
now = datetime.now().strftime("%H:%M")
now_obj = datetime.now().strptime(now,"%H:%M").time()
print(now_obj, type(now_obj))