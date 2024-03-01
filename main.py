# from collections import namedtuple
#
# User = namedtuple('User', 'id name lastname age email')
#
# users = [
#     (1, 'Toxir', 'Toxirov', 28, 'toxir@gmail.com'),
#     (2, 'Sobir', 'Toxirov', 18, 'sobir@gmail.com'),
#     (3, 'Toxir', 'Sobirov', 35, 'toxir2@gmail.com'),
# ]
#
# for user in users:
#     us = User(*user)
#     print(us.id, us.name, us.lastname, us.age, us.email)
#
#
#



from collections import namedtuple

Car = namedtuple('Car', 'nomi rangi tezligi narxi orindiqlarsoni boshqaruv')

cars = [
    ('Malibu', 'Red', '300 km/h', 20000, 4, 'Avtomat'),
]

for car in cars:
    us = Car(*car)
    print(*us)
