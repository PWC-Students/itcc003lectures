# Python Programming - 04/14/2023 Lecture
# ------------------------------- Non Mutators
#Accessing
# print(nativeLanguages)
# print(nativeLanguages[0])
# print(nativeLanguages[5])
# print(nativeLanguages[7])

#Negative index accessing
# print(nativeLanguages[-6])

#Getting the length
# print(len(nativeLanguages))

#Slicing
# listName[firstIndex:lastIndex]
# firstIndex is inclusive
# lastIndex is exclusive
nativeLanguages = ["Java", "Python", "Javascript",
                   "C", "PHP", "Ruby", "C++"]
# print(nativeLanguages[0:3]) # gets the elements from index 0, 1 and 2 ONLY
# print(nativeLanguages[4:7]) # gets the elements from index 4, 5 and 6 ONLY

#Looping thru a List
for nativeLanguage in nativeLanguages:
    print(nativeLanguage)

# ------------------------------- Mutators
# print(nativeLanguages)
# nativeLanguages[0] = "React"
# print(nativeLanguages)
# nativeLanguages[6] = "Laravel"
# print(nativeLanguages)

# Tuples --- Immutable(it means that the original tuple can't be changed)
#Non Mutators will still work with Tuples, same as how it is implemented in Lists
frameWorks = ("React", "Laravel", "Bootstrap", "Springboot", "CakePHP", "BASIC")

frameWorks[0] = "DashForge CSS"
print(frameWorks)




























