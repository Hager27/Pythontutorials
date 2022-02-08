#removing an array element
colors =["Green","Yellow","Red","Blue","Indigo","Violet","Orange"]
print(colors)
del colors[4]
print(colors)
colors.remove("Blue")
print(colors)
colors.pop(3)
print(colors)

# the following is my output
##['Green', 'Yellow', 'Red', 'Blue', 'Indigo', 'Violet', 'Orange']
#['Green', 'Yellow', 'Red', 'Blue', 'Violet', 'Orange']
#['Green', 'Yellow', 'Red', 'Violet', 'Orange']
#['Green', 'Yellow', 'Red', 'Orange']
