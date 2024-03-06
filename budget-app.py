from itertools import zip_longest

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()  # Initialize ledger as an empty list to store transactions

    def deposit(self, amount, description=""):
        """
        Record a deposit into the ledger.

        Args:
        amount (float): The amount of money deposited.
        description (str, optional): Description of the transaction. Defaults to "".
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        Record a withdrawal from the ledger.

        Args:
        amount (float): The amount of money withdrawn.
        description (str, optional): Description of the transaction. Defaults to "".

        Returns:
        bool: True if the withdrawal is successful, False otherwise.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Get the current balance of the category.

        Returns:
        float: Current balance of the category.
        """
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, budget):
        """
        Transfer funds between categories.

        Args:
        amount (float): The amount of money to transfer.
        budget (Category): The category to transfer funds to.

        Returns:
        bool: True if transfer is successful, False otherwise.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget.name}")
            budget.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        """
        Check if there are sufficient funds for a transaction.

        Args:
        amount (float): The amount of money for the transaction.

        Returns:
        bool: True if there are sufficient funds, False otherwise.
        """
        return amount <= self.get_balance()

    def __str__(self):
        """
        Format category object as a string.

        Returns:
        str: String representation of the category object.
        """
        title = f"{self.name:*^30}\n"  # Center the name within a line of '*' characters
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}\n"  # Limit description to 23 characters
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output


def create_spend_chart(categories):
    """
    Create a bar chart showing the percentage spent in each category.

    Args:
    categories (list): List of Category objects.

    Returns:
    str: String representing the bar chart.
    """
    chart = "Percentage spent by category\n"
    arrCategories = [cat.name for cat in categories]
    deductions = [sum(ledger['amount'] for ledger in cat.ledger if ledger['amount'] < 0) for cat in categories]
    total_deductions = sum(deductions)
    percentages = [(d / total_deductions) * 100 for d in deductions]

    for num in range(100, -1, -10):
        chart += f"{num:3d}|"
        for percent in percentages:
            if percent >= num:
                chart += " o "
            else:
                chart += "   "
        chart += ' \n'

    chart += f"{'-' * 10:>14}" + '\n'

    for name in zip_longest(*arrCategories, fillvalue=" "):
        chart += "     " + ("  ".join(name)) + '  \n'

    return chart.rstrip('\n')


# Test the function
# category_1 = Category("Food")
# category_1.deposit(1000, "Initial deposit")
# category_1.withdraw(10.15, "Groceries")
# category_1.withdraw(15.89, "Restaurant and more food for dessert")

# category_2 = Category("Entertainment")
# category_2.deposit(2000, "Initial deposit")
# category_2.withdraw(25.55, "Movie tickets")
# category_2.withdraw(10, "Popcorn")

# print(create_spend_chart([category_1, category_2]))
