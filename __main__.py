from Bot import Bot
from abc import ABC, abstractmethod

class View(ABC):    
    @abstractmethod
    def display(self):
        pass

    
class HelpView(View):
    def display(self):
        print("List of commands:")
        for command in commands:
            print(command)
        print()

class ContactListView(View):
    def __init__(self, contacts):
        self.contacts = contacts
    
    def display(self):
        print("Contact list:")
        for contact in self.contacts:
            print(contact)
        print()

class MessageView(View):
    def __init__(self, message):
        self.message = message
    
    def display(self):
        print(self.message)
        print()
if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot()
    bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()
        if action == 'help':
            HelpView().display()
            action = input().strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        elif action == 'view':
            ContactListView(bot.book.contacts).display()
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if action == 'exit':
            break
