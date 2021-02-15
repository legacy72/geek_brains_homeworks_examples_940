class OrganicCell:
    def __init__(self, count_cells):
        self.count_cells = count_cells

    def __add__(self, other):
        return OrganicCell(self.count_cells + other.count_cells)

    def __sub__(self, other):
        if self.count_cells - other.count_cells <= 0:
            raise Exception('Разность не может быть меньше нуля')
        return OrganicCell(self.count_cells - other.count_cells)

    def __mul__(self, other):
        return OrganicCell(self.count_cells * other.count_cells)

    def __truediv__(self, other):
        return OrganicCell(self.count_cells // other.count_cells)

    def make_order(self, count_cells_in_row):
        l = ['*' for _ in range(self.count_cells)]
        return '\n'.join([''.join(l[i:i+count_cells_in_row]) for i in range(0, len(l), count_cells_in_row)])


oc_1 = OrganicCell(12)
print(f'1 клетка:\n{oc_1.make_order(5)}')
oc_2 = OrganicCell(20)
print(f'2 клетка:\n{oc_2.make_order(5)}')
oc_3 = oc_1 + oc_2
print(f'3 клетка:\n{oc_3.make_order(5)}')
oc_4 = oc_3 / oc_1
print(f'4 клетка:\n{oc_4.make_order(5)}')
oc_5 = oc_1 * oc_4
print(f'5 клетка:\n{oc_5.make_order(5)}')
oc_6 = oc_5 - oc_4
print(f'6 клетка:\n{oc_6.make_order(5)}')
