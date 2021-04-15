# первый проект
if 5 > 2:
    print('It works, Ruslan, Well Done!')
else:
    print("It doesnt works, you're badass!")


# второй проект
name = 'Ruslan'
if name == 'Ruslan':
    print('Hey, Ruslan!')
elif name == 'Denis':
    print('Hey, Denis!')
else:
    print('Hey, Arseniy!')


# третий проект
def hi(name):
    if name == 'Ruslan':
        print('Hi, Ruslan!')
    elif name == 'Denis':
        print('Hi, Denis!')
    else:
        print('Hi, Arseniy!')

hi('Ruslan')


# четвертый проект
def hi(name):
    print('Hi, ' + name + '!')

men = ['Denis', 'Arseniy', 'Arslan', 'Artem', 'Kirill', 'Ruslanbek', 'Me']
for name in men:
    hi(name)
    print('Next man')


# пятый проект
for I in range(1, 10):
    print(I)
