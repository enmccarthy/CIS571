"""
Solver for a cyptarithmetic problem using Most Constrained Variable, Most Contraining Variable and Least constrating value. 

Must be assigned 0-9, the first letter cannot be 0. 

Most constrained variable should be assigned next (aka the variable that shows up the most) 

Then the most contraining, choose the one that imposes the most contraints on the remaining variables

Given a variable in which order should its values be tried? Choose the least contraining
 
"""
import copy


"""
initialVarAssignment takes in a subtrahend of len 4, a minuend of len 3 and the difference of length three
It puts variables in order of most constrained and then most constraining
Then passes it to backtracking
"""
number = 0

def initialVarAssignment(sub, minu, diff):
    global number
    unassigned = {}
    unassignList = []
    mostConstrain = []
    # the first letter in each solution cannot be 0 so it has at least one
    # constraint
    #always assign sub[0] first
    unassigned[sub[0]] = 8
    unassigned[minu[0]] = 1
    unassigned[diff[0]] = 1
    # the most constrained variable is the one that shows up the most
    for letter in sub + minu + diff:
        unassigned[letter] = unassigned.setdefault(letter, 0) + 1
    # after the most constrained are assigned we want to assign the most constraining
    for key, item in unassigned.iteritems():
        if item ==1:
            mostConstrain.append(key)
    #if a column has more variables open setting that variable will be the most constraining
    if sub[2] in mostConstrain and minu[1] in mostConstrain and diff[1] in mostConstrain:
        unassigned[sub[2]] = 2
    if sub[3] in mostConstrain and minu[2] in mostConstrain and diff[1] in mostConstrain:
        unassigned[sub[3]] = 2
    for (key, item) in sorted(unassigned.iteritems(), key= lambda(k,v): (v,k)):
        unassignList.append(key)
    solution = backtracking({},unassignList, sub, minu, diff,0)
    if solution == []:
        print "No valid solution"
    else:
        for (assign, steps) in solution:
            print "Assignment:", assign, "Steps to this answers:", steps
        print "Total Steps taken:", number
    return solution
        
"""
backtrack is a recursive function that tries every value to find a valid assignment
"""

def backtracking(assignment, unassigned, sub, minu, diff, steps):
    solution = []
    global number
    if len(unassigned)==0:
        solution.append(([(key,item) for key,item in assignment.iteritems()], steps))
    else:
        var = unassigned.pop()
        if var == sub[0]:
            assignment[var] =1
            number+=1
            solution = solution + backtracking(copy.deepcopy(assignment), copy.deepcopy(unassigned), sub, minu, diff, 1)
        else:
            for value in possibleNum(assignment):
                assignment[var] = value
                if check(assignment, sub, minu, diff):
                    number+=1
                    steps +=1
                    solution = solution + backtracking(copy.deepcopy(assignment), copy.deepcopy(unassigned), sub, minu, diff, steps)
    return solution
"""
possibleNum returns all the values that are left and can be assigned 
It puts 0 last because it is the most constrained number
"""

def possibleNum(assign):
    #0 is the most constrained number so we will try that last
    #sub[0] will always be assigned 1 
    possible = [1,9,8,7,6,5,4,3,2,0]
    for val in assign.values():
        possible.remove(val)
    return possible
        
"""
Check makes sure the assignment is valid, but still allows for assignment if the column has not yet been completed (to allow for the initial assignments)
"""
def check(assignment, sub, minu, diff):
    if assignment.get(sub[0]) == 0 \
       or assignment.get(minu[0]) == 0 \
       or assignment.get(diff[0]) == 0:
        return False
    if sub[1] in assignment and minu[0] in assignment and diff[0] in assignment:
        if assignment[sub[1]]+10 - assignment[minu[0]] != assignment[diff[0]] \
           and assignment[sub[1]]+9 - assignment[minu[0]] != assignment[diff[0]]:
            return False
    if sub[2] in assignment and minu[1] in assignment and diff[1] in assignment:
        if assignment[sub[2]]+10 - assignment[minu[1]] != assignment[diff[1]] \
           and assignment[sub[2]] - assignment[minu[1]] != assignment[diff[1]] \
            and assignment[sub[2]]+9 - assignment[minu[1]] != assignment[diff[1]]\
            and assignment[sub[2]]-1 - assignment[minu[1]] != assignment[diff[1]]: 
            return False
    if sub[3] in assignment and minu[2] in assignment and diff[2] in assignment:
        if assignment[sub[3]]+10 - assignment[minu[2]] != assignment[diff[2]] \
           and assignment[sub[3]] - assignment[minu[2]] != assignment[diff[2]] \
            and assignment[sub[2]]+9 - assignment[minu[1]] != assignment[diff[1]]\
            and assignment[sub[2]]-1 - assignment[minu[1]] != assignment[diff[1]]:
            return False

    for letter in sub+minu+diff:
        if letter not in assignment:
            return True
    if ((assignment[sub[0]]*1000)+(assignment[sub[1]]*100)+(assignment[sub[2]]*10) + assignment[sub[3]])-((assignment[minu[0]]*100) + (assignment[minu[1]]*10) + assignment[minu[2]]) != ((assignment[diff[0]]*100) + (assignment[diff[1]]*10) + assignment[diff[2]]):
        return False
        
    return True
        
    
#initialVarAssignment("FOUR", "TWO", "TWO")    
    
subtrahend = raw_input("Please enter a subtrahend of length 4: ")
minuend = raw_input("Please enter a minuend of length 3: ")
difference = raw_input("Please enter a difference of length 3: ")

initialVarAssignment(subtrahend, minuend, difference)
