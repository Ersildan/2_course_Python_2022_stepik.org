words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish',
         'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray',
         'accident', 'abduct', 'bigot', 'bet', 'abandon',
         'besides', 'access', 'friday', 'bestow', 'abound',
         'absent', 'beware', 'abundant', 'abnormal', 'aboard',
         'about', 'accelerate', 'abort', 'thursday', 'tuesday',
         'sunday', 'berth', 'beyond', 'benevolent', 'abate',
         'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder',
         'abrupt', 'saturday', 'accessory', 'absorb'
         ]

print(*sorted(list(filter(lambda lol: len(lol) == 6, words))))
