color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
value = list(range(10))
mul = list(map(lambda x: 10**x, value))
ans = ''
for i in range(2):
    ans += str(color.index(input()))
ans = int(ans) * mul[color.index(input())]
print(ans)