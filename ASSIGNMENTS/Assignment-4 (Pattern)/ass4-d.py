for i in range(1,6):
    for j in range(1,7-i):
        print("  ",end="")
    for j in range(1,i+1):
        print(j+i-1,end=" ")
    for j in range(i-1,0,-1):
        print(j+i-1,end=" ")
    print()

'''
          1 
        2 3 2 
      3 4 5 4 3
    4 5 6 7 6 5 4
  5 6 7 8 9 8 7 6 5
'''