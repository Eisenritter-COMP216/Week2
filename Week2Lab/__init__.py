from Week2Lab import Pet


def main():
    garfield = Pet.Pet('Garfield',3)
    x = 1
    print(f'{x}:{garfield}')
    garfield.owner = 'Jon'
    x += 1
    print(f'{x}:{garfield}')
    x += 1
    print(f'{x}:{garfield.owner}')
    garfield.set_owner('Jon')
    x += 1
    print(f'{x}:{garfield}')
    garfield.train()
    x += 1
    print(f'{x}:{garfield}')
    # create a list with about 4 pets
    pets = [garfield, Pet.Pet('Beethoven', 2), Pet.Pet('Jake', 5), Pet.Pet('Stuart', 7)]
    for p in pets:
        x += 1
        print(f'\n{x}:{p}')


if __name__ == '__main__':
    main()
