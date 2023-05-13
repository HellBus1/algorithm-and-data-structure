def findCommonValuesBetweenThreeSortedArrays(arr1 = [], arr2 = [], arr3 = []):
  arr1_length, arr2_length, arr3_length = len(arr1), len(arr2), len(arr3)
  iter1, iter2, iter3 = 0, 0, 0

  results = []

  while (iter1 < arr1_length) and (iter2 < arr2_length) and (iter3 < arr3_length):
    val1, val2, val3 = arr1[iter1], arr2[iter2], arr3[iter3]
    
    if (val1 == val2) and (val2 == val3):
       results.append(val1)
       iter1 += 1
       iter2 += 1
       iter3 += 1
    
    if val1 < val2:
       iter1 += 1
      
    if val2 < val3:
       iter2 += 1

    else:
       iter3 += 1

  if(len(results) == 0):
     return -1
  
  return ' '.join(str(x) for x in results)

if __name__ == "__main__":
    print(findCommonValuesBetweenThreeSortedArrays(
       [1,2,4,7,8,9],
       [2,4,7,8,21,46,67,76,77],
       [3,4,6,7,8,10,14,15]
    ))

    print(findCommonValuesBetweenThreeSortedArrays(
       [1,5,10,20,20,40,80],
       [6,7,20,20,80,100],
       [3,4,15,20,20,30,70,80,120]
    ))