# 1. Write a program to swap two numbers.

### Swap two numbers

# a = 10 
# b = 20 

# ## 1. with third variable
# c = a    #ca  ab  bc
# a = b 
# b = c
# print(a , b)

# ##2. without using third varible
# a = 10 
# b = 20 

# a = a + b   ## 10 + 20 = 30  # a = 30
# b = a - b   ## 30 - 20 = 10  # b = 10
# a = a - b   ## 30 - 10 = 20  # a = 20

# print(a, b)

# ##3. without using third varible
# a = 10 
# b = 20 

# a = a * b   10*20=200
# b = a / b   200/20 = 10
# a = a / b   200/10 = 20

# print(a, b)

# ##4.python feature

# a = 10 
# b = 20 

# a, b = b, a
# print(a, b)

# --------------------------------------------------------------------------------------------------#


# 2. How to check number is prime or not. //Prime numbers are natural numbers that are divisible by only 1 and the number itself.// 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,

# def primeNumber(num):  #In this program if number is 2 then it will show it is not prime number which is wrong
#     if(num%2!=0): 
#         print("This is prime number")
#     else:
#         print("This is not a prime number")

# primeNumber(8)

# num=2
# if num>1:
#     for i in range(2,int(num/2)+1):
#         if(num%i==0):
#             print(num,"is not a prime number")
#             break
#     else:
#         print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")


# --------------------------------------------------------------------------------------------------#

# 3. How to find factorial of a number

# 6!=6*5*4*3*2*1 = 720
# 0!=1
# 1!=1



#Built in function
# import math
# def factorial(n):
#     return(math.factorial(n))
# print(factorial(6)) #720



#Using Itertaive Approach
# def factorial(n):
#      res=1

#      for i in range(1,n+1):   
#         res=res*i
#      return res

# print(factorial(6)) #720


#Using Itertaive Approach
# def factorial(n):
#     if n<0:
#         return 0
#     elif (n==0 or n==1):
#         return 1
#     else:
#         fact=1

#         while (n>1):
#             fact=fact*n
#             n=n-1
#         return fact
# print(factorial(3))


# One line Solution (Using Ternary operator): 
# def factorial(n):
#     # single line to find factorial
#     return 1 if (n==1 or n==0) else n * factorial(n - 1)
# print(factorial(3))

# --------------------------------------------------------------------------------------------------#

# 4. Print Fibonacci series.

#a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

# Function for nth fibonacci
# number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1
 

 #Space Optimized method

# def fibonacci(n):
#     a = 0
#     b = 1

#     if n < 0:
#         print("Incorrect input")      
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return b
#     else:
#         for i in range(1, n):
#             c = a + b
#             a = b
#             b = c
#         return b
 
# print(fibonacci(10)) #55  //0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144  //count from 0  /10 th no is 55





# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))

# # first two terms
# n1, n2 = 0, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1

# --------------------------------------------------------------------------------------------------#

# 5. How to find the sum of elements in an array?


# Iterating through the array and adding each element to the sum variable and finally displaying the sum
# def sumOfArray(arr):
#     sum=0
#     for i in arr:
#         sum=sum+i
#     return sum

# print(sumOfArray([10,20,30.2])) #60.2


# #Using the built-in function sum().
# arr=[10,20,30.2]
# print(sum(arr))   #60.2

# --------------------------------------------------------------------------------------------------#

#6. How to find maximum and minimum elements in an array?


#Using inbuilt function min(arr) 
# arr = [10, 89, 9, 56, 4, 80, 8]
# print (min(arr))
# print (max(arr))


#Sort the array using inbuilt sort()function
# Minimum element is at index 0 and maximum is at index -1
# arr = [10, 89, 9, 56, 4, 80, 8]
# arr.sort()
# print (arr[0])
# print (arr[-1])


# Naive solution to find the minimum and maximum number in a list

# def findMinAndMax(nums):
#     # initialize minimum and maximum element with the first element
#     max = min = nums[0]
 
#     # do for each element in the list
#     for i in range(1, len(nums)):
 
#         # if the current element is greater than the maximum found so far
#         if nums[i] > max:
#             max = nums[i]
 
#         # if the current element is smaller than the minimum found so far
#         elif nums[i] < min:
#             min = nums[i]
 
#     print('The minimum element in the list is', min)
#     print('The maximum element in the list is', max)

# nums = [5, 7, 2, 4, 9, 6]
# findMinAndMax(nums)
 

# def findMaxMin(nums):
#     max = min = nums[0]
#     for i in range(0,len(nums)):
#          if (nums[i] > max):
#            max = nums[i]
#          elif(nums[i] < min):
#             min = nums[i]
#     print("max num",max)
#     print("min no",min)

# nums = [5, 7, 2, 4, 9, 6]
# findMaxMin(nums)


# --------------------------------------------------------------------------------------------------#
# 7. How to find the length of the list?

# a=[10,20,30]
# print(len(a)) #3


#using for loop
# def findLength(list):
#     counter=0

#     for i in str:
#         counter = counter+1
#     return counter

# str=[1,2,3,4,58,9]
# print(findLength(str)) #6

# --------------------------------------------------------------------------------------------------#

# 8. How to swap first and last elements in the list

# a=[10,20,20,40,50]
# a[0],a[len(a)-1]=a[len(a)-1],a[0]   or #a[0],a[-1]=a[-1],a[0]
# print(a) #[50,20,20,40,10]


#Using pop function
# def swapList(list):
     
#     first = list.pop(0)  
#     last = list.pop(-1)

#     list.insert(0, last) 
#     list.append(first)      
#     return list 

# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))  #[24, 35, 9, 56, 12]

# --------------------------------------------------------------------------------------------------#

# 9. How to swap any two elements in the list?

# def swapPositions(list, pos1, pos2):
     
#     list[pos1], list[pos2] = list[pos2], list[pos1]  #list[0],list[2]=list[2],list[0]
#     return list

# list = [23, 65, 19, 90]
# pos1, pos2  = 1, 3
# print(swapPositions(list, pos1-1, pos2-1))  # pos1-1=1-1= 0 , pos2-1=3-1=2   [19, 65, 23, 90]

# --------------------------------------------------------------------------------------------------#

# 10. How to remove the Nth occurrence of a given word list? 

# Function to remove Ith word

#Instead of making a new list, delete the matching element from the list itself. 
# Iterate the elements in the list and check if the word to be removed matches the element and the occurrence number,
#  If yes delete that item and return true. If True is returned, print List otherwise, print “Item not Found”.
 

# def removeWord(list,word,N):
#     counter=0
#     for i in range(0,len(list)):
#         if list[i] == word:
#          counter = counter+1

#         if counter==N:
#              del(list[i])
#              return list
           
#     return "Item not updated"

# list=['geeks', 'for', 'geeks','for','new','geeks']
# word="geeks"
# N = 2  #2 nd occurance of 'geeks' will be removed
# print(removeWord(list,word,N))   #['geeks', 'for', 'for', 'new', 'geeks']



# def RemoveIthWord(list, word, N):
#     count = 0
     
#     for i in range(0, len(list)):
#         if (list[i] == word):
#             count = count + 1
             
#             if(count == N):
#                 del(list[i])
#                 return True
                 
#     return False
 
# list = ['geeks', 'for', 'geeks','for','new','geeks']
# word = 'geeks'
# N = 2  #2 nd occurance of 'geeks' will be removed
 
# flag = RemoveIthWord(list, word, N)
 
# if (flag == True):
#     print("Updated list is: ", list)
# else:
#     print("Item not Updated")      #Updated list is: ['geeks', 'for', 'for', 'new', 'geeks']


# --------------------------------------------------------------------------------------------------#

# 11. How to search an element in the list?

# lst=[ 1, 6, 3, 5, 3, 4 ]
# #checking if element 7 is present in the given list or not
# i=7
# # if element present then return exist otherwise not exist
# if i in lst:
#     print("exist")
# else:
#     print("not exist")



# def searchEle(list,n):
#     for i in range (0,len(list)):
#         if list[i] == n:
#             print("Exist")
#             break
#     else:
#      print("Not exist")

# a = [1,2,4,8,10,400,3,900]
# searchEle(a,900)

# --------------------------------------------------------------------------------------------------#

# 12. How to clear the list?

# a=[10,20,4,8]
# for item in list(a):
#    a.remove(item)

# print(a) #[]

 

# a=[10,20,30]
# a.clear()
# print(a) #[]

# b=[10,20,30]
# del b[:]
# print(b) #[]

# c=[10,20,30]
# c *= 0
# print(c) #[]

# ---------------------------------------------------------------------------------------------------#

# 13. How to reverse a list?


# list = [10,20,30]
# i = len(list) - 1 
# # Iterate till 1st element and keep on decrementing i
# newList=[]
# while i >= 0 :
#     newList.append(list[i])
#     i -= 1
# print(newList)  #[30, 20, 10]





# list = [10,20,30,40,5000,20]
# newList=[]
# for i in range( len(list) - 1, -1, -1) :  #start,stop,step
#     newList.append(list[i])
# print(newList)   #[20, 5000, 40, 30, 20, 10]



# a = [10,20,30]
# a.reverse()
# print(a)  #[30, 20, 10]


# a = [10,20,30]
# b=a[::-1]
# print(b)  #[30, 20, 10]



# Operating System List
# systems = ['Windows', 'macOS', 'Linux']

# # Printing Elements in Reversed Order
# for o in reversed(systems):   #reversed() function.
#     print(o)  

# ---------------------------------------------------------------------------------------------------#
# 14. How to clone or copy a list?


# list = [10,20,30,40,5000,20]
# newList=[]
# for i in range (0,len(list)):
#     newList.append(list[i])
# print(newList)   #[10, 20, 30, 40, 5000, 20]




# a=[10,20,30]
# b=a.copy()
# print(b)  #[10, 20, 30]



#This method is considered when we want to modify a list and also keep a copy of the original. 
# In this, we make a copy of the list itself, along with the reference. 
# This process is also called cloning. 
# This technique takes about 0.039 seconds and is the fastest technique. 

# Using the Slice Operator
# def Cloning(li1):
#     li_copy = li1[:]
#     return li_copy
 
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = Cloning(li1)
# print("Original List:", li1) # Original List: [4, 8, 2, 10, 15, 18]
# print("After Cloning:", li2) #After Cloning: [4, 8, 2, 10, 15, 18]



#Using extend function
# a=[10,20]
# b=[]
# b.extend(a)
# print(b)  #[10, 20]

# ---------------------------------------------------------------------------------------------------#

# 15. How to count occurrences of an element in a list?

#By using count method
# a=[10,20,30,40,20,20]
# print(a.count(20))  #3


#By using for loop
# def countOf(list,x):
#     count=0

#     for ele in list:
#         if(ele==x):
#             count=count+1
#     return count

# list=[3,10,20,3,30,3567,3,3]
# print(countOf(list,3))  #4

# ---------------------------------------------------------------------------------------------------#

# 16. Find the sum of the elements in list

# def sumofList(list):
#     sum=0
#     for i in list:
#         sum=sum+i
#     return sum

# list=[10,20,30,40]
# print(sumofList(list))


# def sumofList(list):
#     sum=0
#     for i in range(0,len(list)):  #length of list is 4 , so range(0,4) so it doesn't take 0 to 4 it will take 0 to 3.
#         sum=sum+list[i]
#     return sum

# list=[10,20,30,40]
# print(sumofList(list)) #100



#Using sum() method
# list=[10,20,30,40]
# print(sum(list)) #100

# ---------------------------------------------------------------------------------------------------#

# 17. How to multiply all the numbers in the list? 


# def multiplyAll(list):
#     multi=1

#     for i in list:
#         multi=multi*i
#     return multi

# list=[2,3,4]
# print(multiplyAll(list))  #24



# list using math.prod
# import math                  #import numpy
# list1 = [1, 2, 3]
# result1 = math.prod(list1)   #numpy.prod
# print(result1) #6

# ---------------------------------------------------------------------------------------------------#

# 18. How to find the smallest and largest numbers on the list?
# same answer as of answer number 6 

# ---------------------------------------------------------------------------------------------------#
# 19. How to find the second largest number in a list?

# using sort method
# a=[40,10,20,30,100,50,400]
# a.sort()
# print(a)
# print(a[-2]) #100


# a=[40,10,20,30,100,50,400]
# a.remove(max(a)) #Removing first largest number from the list
# print(a)  #[40, 10, 20, 30, 100, 50]
# print(max(a)) #100

# ---------------------------------------------------------------------------------------------------#

# 20. How to check string is palindrome or not?

#Palindrome - The characters read the same backward as forward. for eg radar,civic,level,madam



# a="civic"
# d=a[::-1]

# if(a==d):
#     print("String is palindrome")    #String is palindrome
# else: 
#     print("String is not palindrome")




# x = "malayalam"
 
# w = ""
# for i in x:
#     w = i + w
 
# if (x == w):
#     print("Yes")  #Yes
# else:
#     print("No")




# def isPalindrome(str):
#     return str == str[::-1]

# print(isPalindrome("civic")) #True
# print(isPalindrome("Civic")) #False


#Takes the input from user
# def isPalindrome(str):
#     return str == str[::-1]

# str = input("Please enter string")
# print(isPalindrome(str))

# ---------------------------------------------------------------------------------------------------#
# 21. How to reverse words in a string?

# a="Welcome"
# print(a[::-1],end="\n")  #emocleW




# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str   /// if str =str+i  //output will be Welcome
#     return str

# s = "Geeksforgeeks"
# print(reverse(s))




# def reverseString(str):
#     i = len(str)-1
#     str1=""
#     while i >= 0:
#         str1  = str1 + str[i]
#         i = i-1
#     return str1

# str  = "Welcome"
# print(reverseString(str))  #emocleW


# def reverse(string):
#     string = string[::-1]
#     return string
  
# s = "Geeksforgeeks"
# print(reverse(s))    #skeegrofskeeG




# str1="Welcome"
# # print(str1[:-1]) #Welcom
# # print(str1[3:-1:-2]) #om
# # print(str1[len(str1):-1:-1]) #print nothing
# str2=""  
# for i in range(len(str1)-1,-1,-1):
#   str2=str2+str1[i]
# print(f"Reverse String is:{str2}") #Reverse String is:emocleW




# string = "geeks quiz practice code"
# # reversing words in a given string
# s = string.split()[::-1]
# # print(s) #['code', 'practice', 'quiz', 'geeks']
# l = []
# for i in s:
#     # apending reversed words to l
#     l.append(i)
# # printing reverse words
# print(" ".join(l))  #code practice quiz geeks

# ---------------------------------------------------------------------------------------------------#
#22. How to find a substring in a string?

# a="welcome"
# print(a[0:3]) #wel
# print(a.find("w")) #0


# word = 'geeks for geeks'
# print(word.find('for')) #6
# print(a.find("e",2)) #6


# s = 'Johny Johny Yes Papa'
# result = s.find('Johny', 1)
# print(result)  #6


# ---------------------------------------------------------------------------------------------------#

# 23. How to find the length of a string?
# a="Welcome"
# print(len(a)) #7


# def findLengthStr(str):
#     counter=0

#     for i in str:
#         counter = counter+1
#     return counter

# str="Hello"
# print(findLengthStr(str)) #5

# ---------------------------------------------------------------------------------------------------#

# 24. How to check if the string contains any special character?

# n="Geeks$For$Geeks"
# n.split()  #It will stored in an array
# # print(n.split()) #['Geeks$For$Geeks']
# # print(n[0]) #G
# flag=0
# s='[@_!#$%^&*()<>?/\|}{~:]' # special character set
# for i in range(len(n)):
#     # checking if any special character is present in given string or not
#     if n[i] in s:
#       flag += 1   # if special character found then add 1 to the flag
#     # print(n[i],end="") #$$ 
 
# # if flag value is greater than 0 then print no
# # means special character is found in string     
# if flag:
#     print("string has special character")         #string has special character
# else:
#     print("string don't have any special character")


# ---------------------------------------------------------------------------------------------------#

# 25. How to check for URL in a string?

# pip install urlextract

# from urlextract import URLExtract
# extractor = URLExtract()
# urls = extractor.find_urls("Let's have URL stackoverflow.com as an example.")
# print(urls) # prints: ['stackoverflow.com']

# ---------------------------------------------------------------------------------------------------#

#Question -  Check if a Substring is Present in a Given String
# MyString1 = "A geek in need is a geek indeed"
 
# if "need" in MyString1:
#     print("Yes! it is present in the string")
# else:
#     print("No! it is not present")



# string = "geeks for geeks"  # or string=input() -> taking input from the user
# substring = "geeks"  # or substring=input()
 
# # splitting words in a given string
# s = string.split()
# print(s) #['geeks', 'for', 'geeks']
 
# # checking condition
# # if substring is present in the given string then it gives output as yes
# if substring in s:
#     print("yes")
# else:
#     print("no")




# a = "c5re8de1ngc7e"
# results={}

# for item in a:
#    results[item] = a.count(item)
# print(results)   #{'c': 2, '5': 1, 'r': 1, 'e': 3, '8': 1, 'd': 1, '1': 1, 'n': 1, 'g': 1, '7': 1}
     

# a = "c5re8de1ngc7e"
# results={}

# for item in a:
#     if (item in results): #if key is already present in dict then dont count   
#         continue

#     results[item] = a.count(item)   #Write this program without count

# print(results)  #{'c': 2, '5': 1, 'r': 1, 'e': 3, '8': 1, 'd': 1, '1': 1, 'n': 1, 'g': 1, '7': 1}
        




a='c5re8de1ngc7e'


# a='c5re8de1ngc7e'

# results = {}
# for item in a:
#     if(item in results): ## check if key present or not, if present then do not count again
#         continue
    
#     results[item] =  a.count(item)

# print(results)


# ##a='develop325ment56'
# results = {}
# i=0
# while i<len(a):
#     if(a[i] in results )
#     if a.count(a[i])>1:
#         results[a[i]] = a.count(a[i])
#     i+=1

# print(a[i],a.count(a[i]))

####==========================================================

a="c5re8de1n9c7e";   
arr=[];
for i in a:arr.append(i);
    
# -------------------------
brr={}

for i in range(0,len(arr)):
    iCounter=0
    
    if arr[i] in brr:
        continue
    
    for j in range(i,len(arr)):
        if arr[i] not in brr:
            if(arr[i]==arr[j]):
                iCounter+=1   
        
    # if arr[i] not in brr:

    if(iCounter > 1):
        brr[arr[i]]=iCounter    
    
print(brr)