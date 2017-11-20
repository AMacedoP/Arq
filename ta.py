from time import time

def hallarTri(n):
    return n * (n + 1) / 2

def hallarPen(n):
    return n * (3 * n - 1) / 2

def hallarHex(n):
    return n * (2 * n - 1)

def igu(a, b, c):
    if (a == b) and (b == c):
        return True
    return False

def hallarMin(nums):
    m = min(nums)
    for i in range(len(nums)):
        if nums[i] == m:
            return i

def main():
    nNums = [286, 165, 143]
    nums = [hallarTri(nNums[0]), hallarPen(nNums[1]), hallarHex(nNums[2])]

    finish = True
    startT = time()
    while finish:
        if igu(nums[0], nums[1], nums[2]):
            print nums[0], nNums[0], nums[1], nNums[1], nums[2], nNums[2]
            break

        m = hallarMin(nums)
        nNums[m] = nNums[m] + 1
        if m == 0:
            nums[0] = hallarTri(nNums[m])
        elif m == 1:
            nums[1] = hallarPen(nNums[m])
        elif m == 2:
            nums[2] = hallarHex(nNums[m])
    endT = time()    
    print "Tiempo ejecucion: " + str((endT - startT) * 1000) + " ms"

main()
