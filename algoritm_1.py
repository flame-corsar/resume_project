n = int(input('Enter ID: '))
sum_id = []

while n > 0:
    u = n % 10
    n = n // 10
    sum_id.append(u)

group = sum(sum_id)
print(group)

