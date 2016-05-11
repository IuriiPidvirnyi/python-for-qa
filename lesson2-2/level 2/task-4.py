"""
Write program to evaluate (a or not b) and (c or not a) expression for boolean variables a, b, c showing result for all possible variables combinations.
"""

def eval():
    bool=[True,False]
    for a in bool:
        for b in bool:
            for c in bool:
                exp= (a or not b) and (c or not a)
                print 'a:',a,'b:',b,'c:',c,'boolean:',exp

eval()