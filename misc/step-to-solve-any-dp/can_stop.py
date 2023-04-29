def canStopRecursive(runway, initSpeed, startIndex = 0):
    # negative base case
    if ((startIndex >= len(runway)) or (startIndex < 0) or 
        (initSpeed < 0) or 
        (not runway[startIndex])):
        return False
    
    # stopping condition base case
    if initSpeed == 0:
        return True
    
    # try all path
    for adjustedSpeed in [initSpeed, initSpeed - 1, initSpeed + 1]:
        # Recurrence relation: if you can stop from any of the subproblem
        # you can also from the main problem
        if canStopRecursive(runway, adjustedSpeed, startIndex + adjustedSpeed):
            return True
    
    return False        

if __name__ == "__main__":
    print(canStopRecursive([True, False, True, True], 1, 0))