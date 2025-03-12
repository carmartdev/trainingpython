# Chapter 1

print("Hello, World!")
# print "Hello, World" was the old form that is not used anymore but is used with python 2

print(2+2) # 4

print(2++2) # output will be 2+(+2)=4
# print(02) this will raise an error in python3

print(int("02")) # will output 2

print(00) # will output 0
#for presenting it with the leading zero:

print(f"{2:02}") # Formats the number 2 with a minimum width of 2 characters and a leading zero


#Qestion1: How many seconds is 42 minutes and 42 seconds?
minute = input("How many minutes?") # 42
second = input("How many seconds?") # 42
print(f"{(int(minute) * 60) + int(second)} seconds") # 2562

#Question2: How many kilmeters is 10 miles?
mile = 1.61
print(f"{mile * 10}")

#Question3: If you go from point A to point B which is 10 kilometer away in 42 minutes and 42 seconds, how many miles per hour was your speed?
pointb = 10 / mile
time = ((42*60)+42)/3600
print(pointb / time)
