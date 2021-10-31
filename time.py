currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait")

'''
Name error
currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)
'''

currentTimeInt = int(current_time_str)
waitTimeInt = int(wait_time_str)

'''
Logic Error: finalTimeInt in hours (0-23)
finalTimeInt = (currentTimeInt + waitTimeInt) % 24
'''
finalTimeInt = currentTimeInt + waitTimeInt

'''
Name error
print(finalTimeInt)
'''
print(finalTime_Int)  

# Added parenthesis to line 2
