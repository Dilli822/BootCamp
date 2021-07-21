names = ["dilli", "hang"]

name_iter = iter(names)

while True:
    try:
        name = next(name_iter)
        print(name)
    except StopIteration:
        break
        