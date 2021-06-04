# Enter your code here. Read input from STDIN. Print output to STDOUT

q=int(input())
ops=[]
result=""
for i in range(q):
    op=input().strip().split()
    if op[0]=='4':
        while ops[-1][0]=='3' or ops[-1][0]=='4':
            ops.pop()
        if ops[-1][0]=='1':
            result=result[0:len(result)-len(ops[-1][1])]
            ops.pop()
        else:
            result+=ops[-1][2]
            ops.pop()
    elif op[0]=='1':
        result+=op[1]
        ops.append(op)
    elif op[0]=='2':
        op.append(result[-int(op[1]):])
        ops.append(op)
        result=result[0:len(result)-int(op[1])]
    else:
        print(result[int(op[1])-1])
        ops.append(op)