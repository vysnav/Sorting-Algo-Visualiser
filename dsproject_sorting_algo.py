

import time, random, turtle

# screen setup
scr = turtle.Screen()
scr.title("Sorting Algorithms Visualizer")
Width=800
Height=500
scr.setup(width=800, height=500)
scr.tracer(0,0)
scr.bgpic('images/bg.gif')
scr.cv._rootwindow.resizable(False, False)

# rendering turtle
renderer = turtle.Turtle()
renderer.hideturtle()
renderer.penup()

# initial settings
n_elements = 25
time_delay = 0.5
method = 1 #setting default sorting value as 1st method
tot_comparisions = 0
start = time.time()

# naming turtle
namer = turtle.Turtle()
namer.penup()
namer.goto(0,Height/2-20)
namer.hideturtle()
namer.color('white')

# time and comparisions illustrator
timer = turtle.Turtle()
timer.penup()
timer.goto(0, Height/2-35)
timer.hideturtle()
timer.color('white')

# function to draw a rectangle
def rectangle (x,y,w,h,color):
    renderer.speed(0)
    renderer.penup()
    renderer.color(color)
    renderer.begin_fill()
    renderer.goto(x,y)
    renderer.pendown()
    renderer.goto(x+w,y)
    renderer.goto(x+w,y-h)
    renderer.goto(x,y-h)
    renderer.goto(x,y)
    renderer.end_fill()
    renderer.penup()

    #outine
    renderer.goto(x,y)
    renderer.color("white")
    renderer.pendown()
    for i in range(3):
        renderer.goto(x,y)
        #renderer.pendown()
        renderer.goto(x+w,y)
        renderer.goto(x+w,y-h)
        renderer.goto(x,y-h)
        renderer.goto(x,y)
        


# rendering function
def render(array, highlight=[], pivot=[]):
    global tot_comparisions, start
    tot_comparisions+=1
    timer.clear()
    timer.write(f"{time.time()-start:.2f} sec             {tot_comparisions} comparisions",align="center")
    renderer.clear()
    renderer.speed(0)
    length = n_elements
    wid = 400/n_elements
    for i,j in enumerate(array):
        color="cyan" if i in pivot else "blue" if i in highlight else "#AB3AD2"
        rectangle((i-length/2)*wid,(j-length/2)*wid,wid,(j+1)*wid, color)
        # rectangle((i-length/2)*400/length,(j-length/2)*400/length,wid,wid,color)
    scr.update()
    if (time_delay):#---------------------------------------------------------------------------------------------------------------
        if tmr_var==1:time.sleep(0.5)
        elif tmr_var==2:time.sleep(0.25)
        elif tmr_var==3:time.sleep(0)

# main array suffling function
def scramble(l):
    a = list(range(l))
    r = []
    for _ in range(l):
        q = random.randint(0,len(a)-1)
        r.append(a[q])
        a.remove(a[q])
    return r

# display name
def show_name(name):
    namer.clear();namer.setx(0);namer.write(name.title(),True,align="center")


""" algos """
def selectionsort(array):
    for i in range(len(array)):
        Min = i
        for k,l in enumerate(array[i:]):
            if l<array[Min]:
                Min = k+i
            render(array,[Min,k+i])
        array[i],array[Min]=array[Min],array[i]
        render(array)
    return array

def bubblesort(array):
    solved = 0
    while solved!=len(array)-1:
        for i,j in enumerate(array[1:None if solved==0 else -solved]):
            if array[i]>j:
                array[i],array[i+1]=array[i+1],array[i]
            render(array,[i+1])
        solved+=1
    return array

def combsort(array):
    gap = len(array)-1
    fphase = False
    while True:
        for i in range(len(array)-gap):
            if array[i]>array[i+gap]:
                array[i],array[i+gap]=array[i+gap],array[i]
            render(array,[i,gap+i])
        if fphase:break
        if gap==1:fphase = True
        else:gap=int(gap/1.3)
    return array

def insertionsort(array):
    solved = 0
    pointer = 0
    while pointer!=len(array)-1:
        if array[pointer]<array[pointer+1]: solved+=1;pointer=solved
        else:
            array[pointer],array[pointer+1]=array[pointer+1],array[pointer]
            pointer-=1
        if pointer<0:pointer=0
        render(array,[pointer+1])
    return array

def bin_insertion_sort(array):
    pointer = 0
    solved = 0
    while pointer!=len(array)-1:
        if array[pointer]<array[pointer+1]: solved+=1;pointer=solved
        else:
            pointer+=1
            curr = array[pointer]
            limit = [0, pointer]
            check = 0
            while True:
                check = round(sum(limit)/2)
                array.pop(pointer)
                array.insert(check, curr)
                pointer = check
                if (array[pointer-1]if pointer-1>=0 else -float('inf'))<curr<array[pointer+1]:break
                if (array[pointer-1]if pointer-1>=0 else -float('inf'))<curr:limit[0]=pointer
                elif array[pointer+1]>curr:limit[1]=pointer
                render(array, [check])
            solved+=1
            render(array,[check])
            pointer = solved
        render(array, [pointer+1])
        pointer = 0 if pointer<0 else pointer
    return array

def quicksort(array, s=0, e=-1):
    if e==-1: e=len(array)
    if len(array[s:e])<=1:return array[s:e]
    p=(s+e)//2
    a=array[s]
    b=array[p]
    c=array[e-1]
    if b<c<a or a<c<b:
        array[s],array[e-1]=array[e-1],array[s]
    elif c<b<a or c<b<a:
        array[s],array[p]=array[p],array[s]
    pivot = s
    p = s+1
    q = e-1
    render(array,[p,q],[pivot])
    while True:
        Econd = 0
        while Econd!=2:
            Econd = 0
            if array[pivot]>array[p] and p!=e-1:p+=1
            else:Econd+=1
            if array[pivot]<array[q]:q-=1
            else:Econd+=1
            render(array,[p,q], [pivot])
        if p<q:
            array[p],array[q]=array[q],array[p]
        else:
            array[pivot],array[q] = array[q],array[pivot]
            return quicksort(array,s,q)+[array[q]]+quicksort(array,q+1,e)

def mergesort(array, l=0, r=-1):
    if r==-1:r=len(array)
    if r-l<=1:return array
    mid = round((l+r)/2+0.1)
    lhs = mergesort(array,l,mid)[l:mid]
    array = array[:l]+lhs+array[mid:]
    rhs = mergesort(array,mid,r)[mid:r]
    array = array[:mid]+rhs+array[r:]
    llen = mid-l
    rlen = r-mid
    while llen!=0 and rlen!=0:
        if array[l]>array[mid]:
            temp=array[mid]
            array.pop(mid)
            array.insert(l,temp)
            rlen-=1
            mid+=1
        else:
            llen-=1
        l+=1
        render(array,[l,mid])
    return array

# main loop
while True:

    # getting user inputs
    tot_comparisions = 0
    time_delay = 0.5
    n_elements = int(scr.numinput(
        "Number of elements",
        "Enter number of elements in range [1-300]", 
        default = n_elements,
        minval = 1,
        maxval = 300
        ) or 0
    )
    if n_elements==0:break
    tosort = scramble(n_elements)
    method = int(scr.numinput(
        "Select algorithm",
        "Enter\n 1 -> Selection sort\n 2 -> Bubblesort\n 3 -> combsort\n 4 -> Insertion sort\n 5 -> Binary insertion sort\n 6 -> Quick sort\n 7 -> Merge sort",
        default=method, 
        minval=1,
        maxval=7)
    )
    if not method:break
    tmr = scramble(n_elements)
    tmr_var = int(scr.numinput(
        "Speed",
        "Enter\n 1 -> Slow\n 2 -> Medium\n 3 -> Fast",
        default=method, 
        minval=1,
        maxval=3)
    )
    if not tmr_var:break
    # starting sorting
    start = time.time()
    if   method==1:show_name("selection sort");tosort = selectionsort(tosort.copy())
    elif method==2:show_name("bubble sort");tosort = bubblesort(tosort.copy())
    elif method==3:show_name("comb sort");tosort = combsort(tosort.copy())
    elif method==4:show_name("insertion sort");tosort = insertionsort(tosort.copy())
    elif method==5:show_name("binary insertion sort");tosort = bin_insertion_sort(tosort.copy())
    elif method==6:show_name("quicksort sort");tosort = quicksort(tosort.copy())
    elif method==7:show_name("merge sort");tosort = mergesort(tosort.copy())
    # ending sorting
    render(tosort)