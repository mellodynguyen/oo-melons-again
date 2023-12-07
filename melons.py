"""Classes for melon orders."""


class AbstractMelonOrder:
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

        # self.order_type = None
        # self.tax = 0

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas Melons":
            base_price = 5 * 1.5
            # base_price = 7.50
        else:
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price

        if self.qty < 10 and self.order_type == "international":
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


# share: species, qty, order_type = None, tax

# class AbstractAnimal:
#     def __init__(self, name):
#         self.name = name

# class Cat(AbstractAnimal):
    # greeting = 'Meow'
    # species = 'cat'


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "International"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0.00
    passed_inspection = False

    def mark_inspection(self, passed):
        # This method should update the attribute passed_inspection
        # if passed == True:
        #     passed_inspection = True
        # else:
        #     passed_inspection = False
        # return passed_inspection
        # or just:
        # return passed_inspection = True

        self.passed_inspection = passed
        return passed_inspection 

    # govorder1 = governmentmelonorder("watermelon", 6)
    # 
