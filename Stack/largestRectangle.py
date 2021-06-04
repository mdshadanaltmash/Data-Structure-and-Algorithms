def largestRectangle(h):
    # Write your code here
    stack=[]
    i=0
    maxArea=0
    while i<len(h):
        if stack==[] or h[i]>h[stack[-1]]-1:
            stack.append(i)
        else:
            curr=stack.pop()
            width=i if stack==[] else i-stack[-1]-1
            maxArea=max(maxArea,width*h[curr])
            i-=1
        i+=1
    while stack!=[]:
        curr=stack.pop()
        width=i if stack==[] else len(h)-stack[len(stack)-1]-1
        maxArea=max(maxArea,width*h[curr])
    return maxArea

h=[1,2,3,4,5]
largestArea=largestRectangle(h)
print(largestArea)