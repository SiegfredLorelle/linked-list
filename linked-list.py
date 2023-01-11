class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_list(self, number_of_nodes, elements):
        print(number_of_nodes, elements)

    def add_at_beginning(self, element):
        ...

    def add_after(self, element):
        ...

    def delete(self, element):
        ...

    def display(self):
        ...

    def count(self):
        ...
    
    def reverse(self):
        ...


class App:

    input_keys = {
        "choice": {1: "create list", 2: "add at beginning", 3: "add after", 4: "delete", 5: "delete", 6: "count", 7: "reverse", 8: "search", 9: "quit"}

    }

    def __init__(self):
        self.main_menu()

    def main_menu(self):
        print("\nMain Menu\n")
        print("[1] Create list\n[2] Add at beginning\n[3] Add after\n[4] Delete\n[5] Display\n[6] Count\n[7] Reverse\n[8] Search\n[9] Quit\n")

        # Ask user what to do (with input checks)
        while True:
            try:
                choice = int(input("What do you want to do?  ")) 
                if choice not in self.input_keys["choice"]:
                    print("Choice must be 1-9 inclusive.\n")
                    continue
            except (TypeError, ValueError):
                print("Only enter the assigned number for your choice (e.g., 3).\n")
            else:
                break
        print()
        self.input_manager(choice)

    def input_manager(self, choice):
        if self.input_keys["choice"][choice] == "create list":
            # Create a linked list
            ll = Linked_List()
            # Asks infos needed to create the linked list
            number_of_nodes, elements = self.create_list_info()
            # Add the nodes to the linked list
            ll.create_list(number_of_nodes, elements)



    def create_list_info(self):
        # Ask how many nodes the linked list should have
        while True:
            try:
                number_of_nodes = int(input("How many nodes does the linked list have?  "))
                if number_of_nodes < 0:
                    continue
            except (TypeError, ValueError):
                print("Number of nodes must be an integer.\n")
            else:
                break

        # Ask for the elements of each nodes (converts the element to int or float if it is one)
        elements=[]
        for i in range(number_of_nodes):
            while True:
                element = input(f"Enter your element[{i}]:  ")
                if not element:
                    print("Element cannot be empty.")
                    continue
                try:
                    element = int(element)
                except (TypeError, ValueError):
                    try:
                        element = float(element)
                    except (TypeError, ValueError):
                        pass
                elements.append(element)
                break
        return number_of_nodes, elements

if __name__ == "__main__":
    App()