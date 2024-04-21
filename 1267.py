N = int(input())

N_lst = list(map(int, input().split()))

Y_cost, M_cost = 0, 0

for n in N_lst:
    Y_cost += (n // 30 + 1) * 10
    M_cost += (n // 60 + 1) * 15

if Y_cost < M_cost:
    print('Y', Y_cost)
elif M_cost < Y_cost:
    print('M', M_cost)
else:
    print('Y', 'M', Y_cost)