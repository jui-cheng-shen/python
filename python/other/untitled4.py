

a=input('please input [Rock] or [Paper] or [Scissors] =>')


def hello(N1,N2,N3):
    if a ==  N1:
        print("--------------")
        print('out of computer is =>',[N2] or [N3] or [N1])
        print("--------------")
        print('you lose')
        
        
    elif a == N2:
        print("--------------")
        print('out of computer is =>',N3 or N2 or N1)
        print("--------------")
        print('you lose')
        
    elif a == N3:
        print("--------------")
        print('out of computer is =>',[N1 or N2 or N3])
        print("--------------")
        print('you lose')
        print([0,3])

    
  

N1 ="Rock" or "石頭"
N2 = ' Paper' or '布'
N3 = 'Scissors' or '剪刀'


hello(N1,N2,N3)



