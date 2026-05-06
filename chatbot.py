import sys

class CoffeeBot:
    def __init__(self):

        # Menu with prices
        self.menu_prices = {
            "Espresso": 120,
            "Latte": 150,
            "Cappuccino": 180,
            "Green Tea": 100
        }

        # Define intents and keywords
        self.responses = {
            "greeting": ["hello", "hi", "hey", "good morning"],
            "menu": ["menu", "order", "drink", "coffee", "tea"],
            "price": ["price", "cost", "rates"],
            "hours": ["hours", "open", "time", "closing"],
            "location": ["where", "address", "location", "place"],
            "thanks": ["thanks", "thank you", "bye", "goodbye"]
        }

        # Bot answers
        self.answers = {
            "greeting": "Hello! Welcome to Brew & Byte. How can I help you today?",

            "menu": (
                "We offer:\n"
                "1. Espresso\n"
                "2. Latte\n"
                "3. Cappuccino\n"
                "4. Green Tea\n"
                "Type 'price' to see prices."
            ),

            "hours": "We are open from 7:00 AM to 8:00 PM every day.",

            "location": "You can find us at 123 Java Lane, Silicon Valley.",

            "thanks": "You're welcome! Have a great day!",

            "fallback": (
                "I'm sorry, I didn't understand that.\n"
                "Try: menu, price, hours, or location."
            )
        }

    # Detect user intent
    def get_intent(self, user_input):
        user_input = user_input.lower()

        for intent, keywords in self.responses.items():
            for word in keywords:
                if word in user_input:
                    return intent

        return "fallback"

    # Show menu prices
    def show_prices(self):
        print("\n--- Price List ---")

        for item, price in self.menu_prices.items():
            print(f"{item}: ₹{price}")

        print()

    # Chat function
    def chat(self):
        print("\n--- Brew & Byte Support Bot ---")
        print("Type 'quit' to exit.\n")

        while True:

            # User input
            user_text = input("You: ")

            # Exit
            if user_text.lower() in ['quit', 'exit']:
                print("Bot: Goodbye!")
                break

            # Find intent
            intent = self.get_intent(user_text)

            # If user asks for prices
            if intent == "price":
                self.show_prices()

            else:
                print("Bot:", self.answers[intent])

            print()


# Main Program
if __name__ == "__main__":
    bot = CoffeeBot()
    bot.chat()
