#encoding=utf-8

di = {"a":21, "c":5, "b":71}

sorted_key = sorted(di.items(), reverse=True)
sorted_value = sorted(di.items(), key=lambda x:x[1])

print(dict(sorted_key))
print(dict(sorted_value))
