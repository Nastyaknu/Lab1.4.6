class Polynom:
    def __init__(self):
        self._coefs_dict = {}

    def get_power(self):
        return self._coefs_dict.keys()

    def get_coef(self, pwr):
        # return self._coefs_dict.get(pwr, 0)
        if pwr in self._coefs_dict:
            return self._coefs_dict[pwr]
        else:
            return 0.0

    #

    def _process_line(self, line):
        data = line.split()
        if len(data):
            assert len(data) == 2
            try:
                pwr = int(data[0])
            except:
                print('Incorrect power:', line[0])
                return False
            #
            assert pwr >= 0
            try:
                coef = float(data[1])
            except:
                print('Incorrect coef:', line[1])
                return False
            #
            self._coefs_dict[pwr] = coef
            return True

    #
    def read_from_file(self, file_name):
        self._coefs_dict = {}
        try:
            with open(file_name) as f:
                for line in f:
                    self._process_line(line.strip())
        except:
            print("Error while reading from file")

    #

    def read_from_keyboard(self):
        self._coefs_dict = {}
        print("Input powers & coefs, one pair per line, or empty line to stop")
        while True:
            s = input()
            if s == "":
                break
            self._process_line(s)

    #

    def set_coefs(self, poly):
        self._coefs_dict = poly

    def evaluate_at_point(self, x):
        result = 0
        for pwr, coef in self._coefs_dict.items():
            term = x ** pwr * coef
            result += term
        return result

    #

    def show(self):
        print(self._coefs_dict)

    @staticmethod
    def add(poly1, poly2):
        powers1 = poly1.get_power()
        powers2 = poly2.get_power()
        poly = {}
        for pwr in set(powers1) | set(powers2):
            poly[pwr] = poly1.get_coef(pwr) + poly2.get_coef(pwr)
        new_polynom = Polynom()
        new_polynom.set_coefs(poly)
        return new_polynom

    @staticmethod
    def subtraction(poly1, poly2):
        powers1 = poly1.get_power()
        powers2 = poly2.get_power()
        poly = {}
        for pwr in set(powers1) | set(powers2):
            poly[pwr] = poly1.get_coef(pwr) - poly2.get_coef(pwr)
        new_polynom = Polynom()
        new_polynom.set_coefs(poly)
        return new_polynom

    @staticmethod
    def multiplication(poly1, poly2):
        powers1 = poly1.get_power()
        powers2 = poly2.get_power()
        poly = {}
        for pwr1 in powers1:
            for pwr2 in powers2:
                poly[pwr1 + pwr2] = poly.get(pwr1 + pwr2, 0) + poly1.get_coef(pwr1) * poly2.get_coef(pwr2)
        new_polynom = Polynom()
        new_polynom.set_coefs(poly)
        return new_polynom


while True:
    try:
        x = float(input("Input x:"))
        break
    except:
        print("Not a valid value")

P1 = Polynom()
P1.read_from_file("input01.txt")
P2 = Polynom()
P2.read_from_file("input02.txt")
p1_x = P1.evaluate_at_point(x)
p2_x = P2.evaluate_at_point(x)
q = p1_x+p2_x*p1_x-p2_x
h = p2_x*(p1_x-p2_x)**2
print(f"q(x)={q} h(x)={h}")
with open("output.txt", 'w') as f:
    f.write(f"{q}\n{h}")
