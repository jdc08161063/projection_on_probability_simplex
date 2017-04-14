# funciton definition
def Projection(w):
    #sort w in decending order
    w_sort=sorted(w,reverse=True)
    
    print 'w after sort ', w_sort
    print 'w ', w
    w_sum=0
    for j in range (0,len(w)):
        print 'iteration is:',j
        w_sum=w_sum+w_sort[j]
        print "sum", w_sum
        v=2*(w_sum-1)/(j+1)
        print 'v is', v
        if w_sort[j+1]-0.5*v <0:
            print 'stopping at:',w_sort[j+1]-0.5*v
            break
    print 'stop iteration is:',j
    print "v is",v
    # calculate x_opt in real order using real w
    x_opt=[]
    for i in range (0,len(w)):
        x_opt.append(w[i]-0.5*v)
    return x_opt


w=[0.7,0.2,-0.1,0.4,-0.1,0.5,0.4,0.1,-0.3]
print Projection(w), 'is the final result!!!'
     
