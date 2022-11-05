import time
import sys
import keyboard # pip3 install keyboard 
import pyautogui  # pip3 install pyautogui 
import random

'''
Goals for today:

_ none
'''

#if len(sys.argv) >= 3:

#
def execMc(color,first,sec,og,dest):
    command = "clone " + str(color) + " " + str(og[1]) + " " + str(og[2] + first) + " " 
    command += str(color) + " " + str(og[1] + 30) + " " + str(og[2] + first) + " " 
    command += str(dest[0]) + " " + str(dest[1]) + " " + str(dest[2] + sec) + " " 

    pyautogui.press('/') 
    pyautogui.write(command)
    pyautogui.press('enter') 

# helper
def clonePlace(place,dest):
    # clone swapped stuff in real view
    command = "clone " + str(place[0]) + " " + str(place[1]) + " " + str(place[2]) + " " 
    command += str(place[0]) + " " + str(place[1] + 30) + " " + str(place[2] + 30) + " " 
    command += str(dest[0]) + " " + str(dest[1]) + " " + str(dest[2]) + " " 

    pyautogui.press('/') 
    pyautogui.write(command)
    pyautogui.press('enter') 

#TODO: add all swaps here
def delayedSwap(first,sec,arr,old):
    #if len(old) > 3:
    #    print("old swap: 1pos " + str(old[0]) + " val " + str(old[1]) + " swapval "+ str(old[2]) + " val " + str(old[3]))
    #print("first swap: 1pos " + str(first) + " val " + str(arr[first]) + " swapval "+ str(sec) + " val " + str(arr[sec]))
    
    og = (-9,6,522) # -z so 521 is next
    place = (15,6,522)
    dest = (31,26,522)
    # -9 white, -10 gray, -11 black, -12 orange, -13 red, -14 yellow, -15 green, -16 light blue, -17 blue,
    # old swap
    execMc(-13,arr[first],first,og,place)
    execMc(-12,arr[sec],sec,og,place)
    #clonePlace(place,dest)
    if len(old) == 4:
        if old[0] != first and old[0] != sec: 
            execMc(-10,old[1],old[0],og,place) # TODO make old blocks gray and you're golden
        if old[2] != sec and old[2] != first: 
            execMc(-10,old[3],old[2],og,place)
    clonePlace(place,dest)

def removeOld(old):
    og = (-9,6,522) # -z so 521 is next
    place = (15,6,522)
    dest = (31,26,522)
    execMc(-10,old[1],old[0],og,place) # TODO make old blocks gray and you're golden
    execMc(-10,old[3],old[2],og,place)
    #time.sleep(1)
    clonePlace(place,dest)

#double swap at the same time
def doubleExec(color1,first,sec,og,dest,color2,swapf,swaps,height):
    '''
    /summon falling_block ~ ~3 ~ {Block:command_block,Time:1,TileEntityData:{Command:"/fill ~ ~-1 ~-1 ~ ~5 ~-1 redstone_block"},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:"/fill ~ ~-1 ~-1 ~ ~5 ~-1 concrete 5"}}]}
    '''
    command = 'summon falling_block -5 '+str(7 + height)+' 522 {Block:command_block,Time:1,TileEntityData:'
    c2 = '{Command:"/clone ' + str(color1) + " " + str(og[1]) + " " + str(og[2] + first) + " " 
    c2 += str(color1) + " " + str(og[1] + 30) + " " + str(og[2] + first) + " " 
    c2 += str(dest[0]) + " " + str(dest[1]) + " " + str(dest[2] + sec)  
    c2 += '"},Passengers:'
    c3 = '[{id:falling_block,Block:command_block,Time:1,TileEntity'
    c4 = 'Data:{Command:"/clone '
    c4 += str(color2) + " " + str(og[1]) + " " + str(og[2] + swapf) + " " 
    c4 += str(color2) + " " + str(og[1] + 30) + " " + str(og[2] + swapf) 
    c5 = " " + str(dest[0]) + " " + str(dest[1]) + " " + str(dest[2] + swaps) + '"}}]}' 

    #print(command)
    pyautogui.press('/') 
    pyautogui.write(command)
    pyautogui.write(c2)
    pyautogui.write(c3)
    pyautogui.write(c4)
    pyautogui.write(c5)
    pyautogui.press('enter') 

# swap 2 minecraft positions
def mcswap(first,sec,arr,count):
    og = (-9,6,522) # -z so 521 is next
    dest = (31,26,522)
    # -9 white, -10 gray, -11 black, -12 orange, -13 red, -14 yellow, -15 green, -16 light blue, -17 blue,
    
    # old swap
    execMc(-13,arr[first],first,og,dest)
    execMc(-12,arr[sec],sec,og,dest)
    execMc(-10,arr[sec],sec,og,dest)
    execMc(-10,arr[first],first,og,dest)
    
    #new swap
    #doubleExec(-13,arr[first],first,og,dest,-12,arr[sec],sec,count + 1)
    #doubleExec(-10,arr[first],first,og,dest,-10,arr[sec],sec,count + 3)
    

# insewrtion sort
def insertion_sort(arr):
    i = 1
    count = 1
    old=[]
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            if (keyboard.is_pressed("*")): 
                print("STOP")
                exit()
            temp = arr[j-1]
            arr[j-1] = arr[j] #swap
            arr[j] = temp
            #print(arr)
            #mcswap(j-1,j,arr,count)
            delayedSwap(j-1,j,arr,old)
            old=[j-1,arr[j-1],j,arr[j]]
            count+=1
            j = j - 1
        i+=1
    removeOld(old)

def bubbleSort(array):
    count = 1
    old=[]
  # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                #mcswap(j+1,j,array,count)
                delayedSwap(j+1,j,array,old)
                old=[j+1,array[j+1],j,array[j]]
                count+=1
    removeOld(old)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

# randomize array
def randomize(arr):
    count = 1
    old=[]
    #fill out ordered stuff
    pyautogui.press('/') 
    pyautogui.write("clone -10 6 522 -10 "+ str(6+len(arr))+" "+ str(522+len(arr))+" 15 6 522") #31,26,522
    pyautogui.press('enter')
    for i in range(0,2*len(arr)):
        if (keyboard.is_pressed("*")): 
            print("STOP")
            exit()
        r = random.randint(0,len(arr)-1)
        r2 = random.randint(0,len(arr)-1) 
        temp = arr[r2]
        arr[r2] = arr[r] #swap
        arr[r] = temp
        #print(arr)
        #mcswap(r2,r,arr,count)
        delayedSwap(r2,r,arr,old)
        old=[r2,arr[r2],r,arr[r]]
        count+=1
    removeOld(old)
    return arr

#
def create_pillar(lenn,color,column): # 1 orange 8 light gray 14 red
    og = (-9,6,522)
    for i in range(0,lenn):
        command = "fill " + str(column) + " " + str(og[1]) + " " + str(og[2] + i) + " " + str(column) + " " + str(og[1] + i) + " " + str(og[2] + i) + " minecraft:concrete " + str(color)

        pyautogui.press('/') 
        pyautogui.write(command)
        pyautogui.press('enter') 

'''
THIS WORKS: https://www.digminecraft.com/command_blocks/multiple_commands.php
/summon falling_block ~ ~1 ~ 
{Block:command_block,Time:1,TileEntityData:
{Command:"/fill ~ ~-1 ~-1 ~ ~10 ~-1 redstone_block"},Passengers:
[{id:falling_block,Block:redstone_block,Time:1}]}

YES:

/summon falling_block ~ ~3 ~ 
{Block:command_block,Time:1,TileEntityData:
{Command:"/fill ~ ~-1 ~-1 ~ ~5 ~-1 redstone_block"},Passengers:
[{id:falling_block,Block:command_block,Time:1,TileEntityData:
{Command:"/fill ~ ~-1 ~-1 ~ ~5 ~-1 concrete 5"}}]}
'''
############################################################ MAIN PROGRAM START ####################################################################################


LENGTH = 6
RANDOM = False
INSERT = False
FILL = False
BUBBLE = False
MERGE = False

if len(sys.argv) >= 2:
    try:
        LENGTH = int(sys.argv[1])
        #print(LENGTH)
    except:
        print("no num")
    if "-f" in sys.argv:
        FILL = True
    if "-r" in sys.argv:
        RANDOM = True
    if "-i" in sys.argv:
        INSERT = True
    if "-b" in sys.argv:
        BUBBLE = True
    if "-m" in sys.argv:
        MERGE = True
    
while(True):
    if (keyboard.is_pressed("~")):
        print("Let's get this bot started")
        time.sleep(.5)
        break

pyautogui.press('/') 
pyautogui.write("time set 1000")
pyautogui.press('enter')
pyautogui.press('/') 
pyautogui.write("fill 31 26 522 31 56 552 minecraft:air")
pyautogui.press('enter')
pyautogui.press('/') 
pyautogui.write("fill 15 6 522 15 36 552 minecraft:air")
pyautogui.press('enter')

mytime = time.time()

start = [item for item in range(0, LENGTH)]

if FILL:
    create_pillar(LENGTH,1,-12)# -9 white, -10 gray, -11 black, -12 orange, -13 red, -14 yellow, -15 green, -16 light blue, -17 blue,
    create_pillar(LENGTH,8,-10)
    create_pillar(LENGTH,14,-13)
if RANDOM:
    start = randomize(start)
    pyautogui.press('/') 
    pyautogui.write("fill -5 6 522 -5 255 522 minecraft:air")
    pyautogui.press('enter')
    while(True):
        if (keyboard.is_pressed("~")):
            print("Let's keep going")
            #print(start)
            time.sleep(.5)
            break

if INSERT:
    insertion_sort(start)
if BUBBLE:
    bubbleSort(start)
if MERGE:
    mergeSort(start, 0, len(start))

pyautogui.press('/') 
pyautogui.write("fill -5 6 522 -5 255 522 minecraft:air")
pyautogui.press('enter')


tottime = time.time() - mytime
#print(start)
print("=== This took " + str((tottime - tottime % 60) / 60) + " minutes " + str(tottime % 60) + " seconds ===")
print("=== Done ===")
