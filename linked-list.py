import sys

class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_list(self, elements):
        # If no no elements, then just inform user that linked list is made with no nodes
        if len(elements) <= 0:
            print("Linked List created with 0 nodes.")
            return

        # Create a node for first element and set it as head
        self.head = Node(elements[0])

        if len(elements) > 1:
            # Create a node for each element and set the pointer accordingly
            current = self.head
            for element in elements[1:]:
                current.next = Node(element)
                current = current.next

        # Display the linked list
        self.display()

    def add_at_beginning(self, element):
        # Create a node for the new element
        added_node = Node(element)

        # If there are other nodes, then point the new node to the head of linked list
        if self.head:
            added_node.next = self.head

        # Make the added node the head to indicate it as the start of linked list
        self.head = added_node

        # Display the linked list
        self.display()

    def add_after(self, element):
        ...

    def delete(self, element):
        ...

    def display(self):
        if self.head:
            print("\nLinked list:")
            current = self.head
            while current != None:
                print(f"{current.element} -> ", end="")
                current = current.next
            print()
        
        else:
            print("Sorry, linked list seems to be empty or that its head is not configured correctly.")

    def count(self):
        ...
    
    def reverse(self):
        ...


class App:

    input_keys = {
        "choice": {1: "create list", 2: "add at beginning", 3: "add after", 4: "delete", 5: "display", 6: "count", 7: "reverse", 8: "search", 9: "quit"}

    }

    def __init__(self):
        self.ll = None
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
            self.ll = Linked_List()
            # Asks infos needed to create the linked list
            elements = self.create_list_info()
            # Add the nodes to the linked list
            self.ll.create_list(elements)
        
        elif self.input_keys["choice"][choice] == "add at beginning":
            if self.ll_exist():
                element = self.ask_for_element("Enter element to insert at the beginning:  ")
                self.ll.add_at_beginning(element)

            

        elif self.input_keys["choice"][choice] == "add after":
            ...

        elif self.input_keys["choice"][choice] == "delete":
            ...

        elif self.input_keys["choice"][choice] == "display":
            if self.ll_exist():
                self.ll.display()

        elif self.input_keys["choice"][choice] == "count":
            ...
        
        elif self.input_keys["choice"][choice] == "reverse":
            ...
        
        elif self.input_keys["choice"][choice] == "search":
            ...
        
        elif self.input_keys["choice"][choice] == "quit":
            sys.exit("Closing the program ...\n")
        
        input("\nPress enter to proceed ...  ")
        self.main_menu()



    def create_list_info(self):
        # Ask how many nodes the linked list should have
        while True:
            try:
                number_of_nodes = int(input("How many nodes does the linked list have?  "))
                if number_of_nodes < 0:
                    print("Number of nodes cannot be negative.\n")
                    continue
            except (TypeError, ValueError):
                print("Number of nodes must be an integer.\n")
            else:
                print()
                break

        # Ask for the elements for each node
        elements=[]
        for i in range(number_of_nodes):
            element = self.ask_for_element(f"Enter your element[{i}]:  ")
            elements.append(element)
        return elements

    # Ask for an element/value and converts it to int or float if necessary
    def ask_for_element(self, msg):
        while True:
            element = input(msg)
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
            return element
    

    def ll_exist(self):
        if self.ll:
            return True
        else:
            print("No Linked List yet. Create a linked list by choosing 1 in Main Menu.\n")
            return False

if __name__ == "__main__":
    App()


# TODO
# if when creating linked list and a current linked list exists, ask again to if user want to delete current linked list