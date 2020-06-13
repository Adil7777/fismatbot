def check_cod(cod):
    f = open('code.txt', 'w')
    f.write(cod)
    f.close()


def read_cod():
    f = open('code.txt', 'r').read()
    return f
