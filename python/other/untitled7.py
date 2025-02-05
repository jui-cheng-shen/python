import random
Rock = "Rock" or "石頭"
Paper = ' Paper' or '布'
Scissors = 'Scissors' or '剪刀'


a = input('please input [Rock] or [Paper] or [Scissors] =>')


s = ['Rock', 'Scissors', 'Paper']
print('out of computer is =>', random.choices(s, k=1))
s2 = random.choices(s)


if a == s2:
    print('平手')


elif a == Scissors and s2 == Rock and s2 != Paper:
    print('you lose')


elif a == Scissors and s2 == Paper and s2 != Rock:
    print('you win')


elif a == Paper and s2 == Scissors:
    print('you lose')


elif a == Paper and s2 == Rock:
    print('you win')


elif a == Rock and s2 == Paper:
    print('you lose')


else:
    print('you lose')
