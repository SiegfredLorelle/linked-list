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


    def add_at_beginning(self, element):
        # Create a node for the new element
        added_node = Node(element)

        # If there are other nodes, then point the new node to the head of linked list
        if self.head:
            added_node.next = self.head

        # Make the added node the head to indicate it as the start of linked list
        self.head = added_node


    def add_after(self, element, position):
        # Traverse the linked list until the given position is reached (counter represents current position)
        counter = 1
        current = self.head
        while current != None:
            # When position is reach, create a node for the new element, point the new node to the where current node points, point the current node to the new node
            if counter == position:
                added_node = Node(element)
                added_node.next = current.next
                current.next = added_node
                break
            # Go to next node
            current = current.next
            counter += 1


    def delete(self, element):
        current = self.head
        # Check the if the element to be deleted is in the first node, if yes then point head to next node (also point deleted node to None)
        if current.element == element:
            after_delete_node = current.next
            current.next = None
            self.head = after_delete_node

        # Check if the element of the next node is the element to be deleted, if yes then point to where the next node points (also point deleted node to None)
        else:
            while current.next != None:
                if current.next.element == element:
                    after_delete_node = current.next.next
                    current.next.next = None
                    current.next = after_delete_node
                    break
                # If next node is not the one to be deleted, then go to next node
                current = current.next
            else:
                print(f"\nElement '{element}' is not found in the linked list. No node was deleted.")


    def display(self):
        # If linked list is empty inform the user about it
        if not self.head:
            print("\nLinked list seems to be empty.")
            return

        # If linked list is not empty, then traverse the linked list, printing the element of each node
        print("\nLinked list:")
        current = self.head
        while current != None:
            print(f"{current.element} -> ", end="")
            
            if not current.next:
                self.tail = current

            current = current.next
        print()


    def count(self):
        if not self.head:
            return 0
        
        counter = 0
        current = self.head
        while current != None:
            current = current.next
            counter += 1

        return counter


    def reverse(self, node):

        if not node.next:
            self.tail, self.head = self.head, self.tail
            self.tail.next = None
            return self.head
        
        tmp_node = self.reverse(node.next)
        tmp_node.next = node
        return node



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
                    print("\nChoice must be 1-9 inclusive.\n")
                    continue
            except (TypeError, ValueError):
                print("\nOnly enter the assigned number for your choice (e.g., 3).\n")
            else:
                break

        # Execute commands depending on user input
        self.input_manager(choice)

    def input_manager(self, choice):
        """ Execute commands depending on user input """
        if self.input_keys["choice"][choice] == "create list":
            # Create a linked list
            self.ll = Linked_List()
            # Asks infos needed to create the linked list
            elements = self.create_list_info()
            # Add the nodes to the linked list using the given elements, then display the linked list
            self.ll.create_list(elements)
            self.ll.display()

        elif self.input_keys["choice"][choice] == "add at beginning":
            """ Inserts the given element at the beginning and displays the linked list """
            # Ensures the linked list exists
            if self.ll_exist():
                # Ask for an element to insert at the beginning, insert it, then display the linked list
                element = self.ask_for_element("\nEnter element to insert at the beginning:  ")
                self.ll.add_at_beginning(element)
                self.ll.display()

        elif self.input_keys["choice"][choice] == "add after":
            # Ensures the linked list exists, and that it is not empty
            if self.ll_exist():
                if self.ll.count() == 0:
                    print(f"\nLinked List have {self.ll.count()} nodes. I suggest adding an element at the beginning by choosing 2 in Main Menu.")

                else:
                    # Ask for element to insert, and the position where to insert the element (element is inserted after the given position)
                    element = self.ask_for_element("\nEnter element to insert:  ")
                    position = self.ask_for_position("\nEnter position after which the element is inserted:  ")
                    # Insert the element, then display the linked list
                    self.ll.add_after(element, position)
                    self.ll.display()


        elif self.input_keys["choice"][choice] == "delete":
            # Ensures the linked list exists, and that it is not empty
            if self.ll_exist():
                if self.ll.count() == 0:
                    print(f"\nLinked List have {self.ll.count()} nodes. I suggest adding an element at the beginning by choosing 2 in Main Menu.")

                # Asks for the element to delete, delete it if found, then display the linked list
                else:
                    element = self.ask_for_element("\nEnter element to delete:  ")
                    self.ll.delete(element)
                    self.ll.display()


        elif self.input_keys["choice"][choice] == "display":
            """ Display the linked list if it exists """
            if self.ll_exist():
                self.ll.display()

        elif self.input_keys["choice"][choice] == "count":
            """ Prints the number of nodes in the linked list if it exists """
            if self.ll_exist():
                print(f"\nLinked list has {self.ll.count()} node(s).")

        elif self.input_keys["choice"][choice] == "reverse":
            """ Reverses the linked list if it exists and is not empty """
            # Ensures the linked list exists, and that it is not empty
            if self.ll_exist():
                if self.ll.count() == 0:
                    print(f"\nLinked List has {self.ll.count()} nodes. I suggest adding an element at the beginning by choosing 2 in Main Menu.")

                # If linked list is not empty, then reverse and display it
                else:
                    self.ll.reverse(self.ll.head)
                    self.ll.display()
        
        elif self.input_keys["choice"][choice] == "search":
            ...
        
        elif self.input_keys["choice"][choice] == "quit":
            sys.exit("\nClosing the program ...\n")
        
        input("\nPress enter to proceed ...  ")
        self.main_menu()



    def create_list_info(self):
        # Ask how many nodes the linked list should have
        while True:
            try:
                number_of_nodes = int(input("\nHow many nodes does the linked list have?  "))
                if number_of_nodes < 0:
                    print("\nNumber of nodes cannot be negative.")
                    continue
            except (TypeError, ValueError):
                print("\nNumber of nodes must be an integer.")
            else:
                print()
                break

        # Ask for the elements for each node
        elements=[]
        for i in range(number_of_nodes):
            element = self.ask_for_element(f"Enter your element[{i}]:  ")
            elements.append(element)
        return elements

    def ask_for_element(self, msg):
        """ Ask for an element/value, and converts it to int or float if necessary """
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
        """ Check if linked list already exists """
        if self.ll:
            return True
        else:
            print("\nNo Linked List yet. Create a linked list by choosing 1 in Main Menu.")
            return False

    def ask_for_position(self, msg):
        """ Ask for a position (1-based index) """
        while True:
            try:
                position = int(input(msg))
                if position <= 0:
                    print("Position must be positive (first position is 1).\n")
                    continue
                elif position > self.ll.count():
                    print(f"There are only {self.ll.count()} node(s).\n")
                    continue
            except (TypeError, ValueError):
                print("Position must be an integer.\n")
                continue
            else:
                return position




if __name__ == "__main__":
    App()


# TODO
# When creating linked list and a current linked list exists, ask again to if user want to delete current linked list
# Search