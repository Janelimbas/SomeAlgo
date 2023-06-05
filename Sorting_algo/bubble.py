#6/3/2023 Sat

#first way
# array = [0,3,1,4,9,6,8,7,2,5]
array = [0,3,1,4,9,5,6,65,35,65,867,4,467,12]
b=0
def sort(array):
  b=0
  length = len(array)
  toIterate = (length-3)*(length-2)
  while b<toIterate-8:
    for i in range(length):
      b = b + 1
      if array[i] > array[i+1]:
        a = array[i]
        array[i] = array[i+1]
        array[i+1] = a
      if array[i+1]==array[-1]:
        break
  print (array)

if __name__ == '__main__':
  sort(array)

#5/3/2023 Fri
# Second way
# array = [0,3,1,4,9,6,8,7,2,5]
# # array = [0,3,1,4,9,5]
# def sort(array):
#   length = len(array)
#   for j in range(length-1):
#     for i in range(length-j-1):
#       if not i+1 == len(array):
#         if array[i] > array[i+1]:
#           a = array[i]
#           array[i] = array[i+1]
#           array[i+1] = a
#   print (array)
#
# if __name__ == '__main__':
#     sort(array)