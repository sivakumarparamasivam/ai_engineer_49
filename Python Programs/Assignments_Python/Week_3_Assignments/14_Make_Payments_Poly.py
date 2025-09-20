# ---------------------------
# a) Define classes
# ---------------------------

class CreditCardPayment:
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class PayPalPayment:
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")


class BankTransferPayment:
    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount}")


# ---------------------------
# c) Polymorphic function
# ---------------------------

def make_payment(payment_method, amount):
    payment_method.process_payment(amount)


# ---------------------------
# d) Main section
# ---------------------------

if __name__ == "__main__":
    # Create objects
    cc_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()
    bank_payment = BankTransferPayment()

    # Demonstrate polymorphism using a loop
    payments = [
        (cc_payment, 100),
        (paypal_payment, 75),
        (bank_payment, 250)
    ]

    for method, amount in payments:
        make_payment(method, amount)
