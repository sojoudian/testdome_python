class IceCreamMachine:
    all={}
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        res = []
        for i in self.ingredients:
            for j in self.toppings:
                res.append([i, j])
        return res

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())
