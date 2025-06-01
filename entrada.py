class Linear_algebrar:
    def __init__(self):
        print('Vamos começar a brincar...')

    def scalar_product(self, m1: list, m2: list):
        step_one = [x * y for x, y in zip(m1, m2)]
        step_two = sum(step_one[:])

        return step_two


linear = Linear_algebrar()

res = linear.scalar_product([2, 4, 2], [2, 4, 2])

print(f'Resultado da multiplicação de matrizes: {res}')
