a = [[1,2,3],
     [4,5,6]]

#One way to traverse a 2d list (nested if loops)
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        print(a[i][j],end=' ')
#    print()


#Another way to traverse a 2d list : more 'pythonic'
#def print_2dlist(lst):
#    for row in a:
#        for element in row:
#            print(element,end='')
#        print()


# Add all elements in 2d list
#sum = 0
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        sum += a[i][j]
#print(sum)

#
#sum = 0
#for row in a:
#    for element in row:
#        sum+= element
#print(sum)


#Changing elements 2d list
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        a[i][j] +=1       
#print_2dlist(a)

#Create a 2d list
#DOES NOT WORK x = [[0] *5]*8


#To make an m x n list
m = 5
n = 8
x = [[0] *n for i in range(m)]

print(x)
        
    
