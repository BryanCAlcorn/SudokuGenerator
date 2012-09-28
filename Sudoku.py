def Sudoku():
    import random;
    puzzle = range(9);
    checker = [0,0,0,0,0,0,0,0,0];
    #makes puzzle a 2-d Array
    for x in range(9):
        puzzle[x] = [0,0,0,0,0,0,0,0,0];
        
    #goes through puzzle and checks if the numbers 1-9 only appear 9 times each
    for i in range(9):
        for j in range(9):
            chkd = False;
            while(chkd == False):
                x = random.randint(1,9);
                #checks if the random number equals 1-9 and if it has occured less than 9 times
                for q in range(9):
                    if(x == q+1):
                        if(checker[q] < 9):
                            checker[q] += 1;
                            chkd = True;
                            break;
                        chkd = False;
                    else:
                        chkd = False;
                if(x in puzzle[i]):
                    chkd = False;
                   # print puzzle
                else:
                    chkd = True;
            puzzle[i][j] = x
    return puzzle;

def BubbleSort(a):
    swapped = True;
    while(swapped):
        swapped = False;
        for i in range(len(a)-1):
            if(a[i] > a[i + 1]):
                a[i + 1], a[i] = a[i], a[i + 1];
                swapped = True;
    return a;
    
def Check(puzzle):
    import copy;
    rows = [];
    boxes = range(9);
    columns = range(9);
    compare = [1,2,3,4,5,6,7,8,9];
    result = True;
    q = 0;
    forloop = [[0,0],[3,0],[6,0],[0,3],[3,3],[6,3],[0,6],[3,6],[6,6]];
    while(result == True):
        #copies all of the rows into a new variable, then sorts and compares them
        rows = copy.deepcopy(puzzle[q]);
        rows = BubbleSort(rows);
        if(rows != compare):
            result = False;
        #if the loop has gone 9 times, breaks out of it
        if(q == 8):
            break;
        q += 1;
    if(result == True):
        for i in range(9):
            for j in range(9):
                #copies all of the columns into a new variable, then sorts and compares them
                columns[j] = copy.deepcopy(puzzle[j][i]);
                columns = BubbleSort(columns);
                if(rows != compare):
                    result = False;
                    break;
    for x in forloop:
        count = 0;
        for f in range(3):
            for g in range(3):
                boxes[count] = copy.deepcopy(puzzle[(f + x[0])][(g + x[1])])
                boxes = BubbleSort(boxes);
                count += 1;
                #print str(f + x[0]) + "," + str(g + x[1]);
        if(boxes != compare):
            result = False;
            return boxes;
    return result,puzzle;

def main():
    result,puzzle = Check(Sudoku());
    count = 1;
    while(result == False):
        result,puzzle = Check(Sudoku());
        print "fail #" + str(count);
        count += 1;
    return puzzle;


def Check2(puzzle):
    import copy
    boxes = range(9);
    compare = [1,2,3,4,5,6,7,8,9];
    forloop = [[0,0],[3,0],[6,0],[1,3],[3,3],[6,3],[0,6],[3,6],[6,6]];
    for x in forloop:
        count = 0;
        for f in range(3):
            for g in range(3):
                boxes[count] = copy.deepcopy(puzzle[(f + x[0])][(g + x[1])])
                boxes = BubbleSort(boxes);
                count += 1;
                print str(f + x[0]) + "," + str(g + x[1]);
        if(boxes != compare):
            result = False;
            return boxes;
