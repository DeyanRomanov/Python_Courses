class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        res = []
        for i in self.products:
            if i.lower()[0] == first_letter.lower()[0]:
                res.append(i)
        return res

    def __repr__(self):
        return f"Items in the {self.name} catalogue:\n" + "\n".join(sorted(self.products))
        a = self.products.copy()
        a.sort()
        for i in a:
            res += i+"\n"
        return res
