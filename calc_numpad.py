num_pad = (
    ('C', '/', '*', 'x'),
    (7, 8, 9, '-'),    
    (4, 5, 6, '+'),
    (1, 2, 3, '#'),
    ('%', 0, '.', '=')
)

for num in num_pad:
    for n in num:
        print(n, end=" ")
    print()