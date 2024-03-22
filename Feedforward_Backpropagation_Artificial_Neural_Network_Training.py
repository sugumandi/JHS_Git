from math import exp

i1, i2 = .05, .10
t1, t2 =.01, 0.99 #최종 목표 값

w1, w3 = .15, .25
w2, w4 = .20, .30
b1, b2 = .35, .35

w5, w7 = .40, .50
w6, w8 = .45, .55
b3, b4 = .6, .6

for epoch in range(2000):
    print('epoch = %d' %epoch)
    
    h1 = i1*w1 +i2*w2 +1*b1
    h2 = i1*w3 +i2*w4 +1*b2
    h1 = 1/(1+exp(-h1))
    h2 = 1/(1+exp(-h2))
    
    o1 = h1*w5 +h2*w6 +1*b3
    o2 = h1*w7 +h2*w8 +1*b4
    o1 = 1/(1+exp(-o1))
    o2 = 1/(1+exp(-o2))
    
    print('o1, o2 = %6.3f %6.3f' %(o1, o2))
    
    E = (o1-t1)**2/2 + (o2 - t2)**2/2
    if E<0.0000001:
        break
    
    o1b, o2b = o1 - t1, o2 - t2
    o1b, o2b = o1b*o1*(1-o1), o2b*o2*(1-o2)
    
    h1b, h2b = o1b*w5 + o2b*w7, o1b*w6 + o2b*w8
    h1b, h2b = h1b*h1*(1-h1), h2b*h2*(1-h2)
    
    w1b, w3b = h1b*i1, h2b*i1
    w2b, w4b = h1b*i2, h2b*i2
    b1b, b2b = 1*h1b, h2b*1
    w5b, w7b = o1b*h1, o2b*h1
    w6b, w8b = o1b*h2, o2b*h2
    b3b, b4b = 1*o1b, 1*o2b
    
    #인공신경망 학습
    lr = 0.01 #가중치
    w1, w3 = w1 - lr*w1b, w3 - lr*w3b
    w2, w4 = w2 - lr*w2b, w4 - lr*w4b
    b1, b2 = b1 - lr*b1b, b2 - lr*b2b
    w5, w7 = w5 - lr*w5b, w7 - lr*w7b
    w6, w8 = w6 - lr*w6b, w8 - lr*w8b
    b3, b4 = b3 - lr*b3b, b4 - lr*b4b