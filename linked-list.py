import sys

class Node:
    """ Node consisting of element and next """
    def __init__(self, element):
        """ Element aka value/data, next is a pointer to the next node"""
        self.element = element
        self.next = None

class Linked_List:
    """ A collection of connected nodes """
    def __init__(self):
        """ Linked list starts at the head node and ends with the tail node """
        self.head = None
        self.tail = None

    def create_list(self, elements):
        """ Creatses a linked list, assigning a node for each element, connecting the nodes exactly as how the elements are sequenced """
        # If no elements, then just inform user that linked list is made with no nodes
        if len(elements) <= 0:
            return

        # Create a node for first element and set it as head
        self.head = Node(elements[0])

        # If given elements are more than 1
        if len(elements) > 1:
            # Create a node for each element and set the pointer accordingly
            current = self.head
            for element in elements[1:]:
                current.next = Node(element)
                current = current.next


    def add_at_beginning(self, element):
        """ Create a node with the value of the given element at the start of the link list """
        # Create a node for the new element
        added_node = Node(element)
        # If there are other nodes, then point the new node to the head of linked list
        if self.head:
            added_node.next = self.head
        # Make the added node the head to indicate it as the start of linked list
        self.head = added_node


    def add_after(self, element, position):
        """ Insert a node containing the value of the given element after the node at the given position """
        # Traverse the linked list until the given position is reached (counter represents current position)
        counter = 1
        current = self.head
        while current:
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
        """ Delete the first node found containing the given element """
        current = self.head
        # Check the if the element to be deleted is in the first node, if yes then point head to next node (also point deleted node to None)
        if current.element == element:
            after_delete_node = current.next
            current.next = None
            self.head = after_delete_node

        # Check if the element of the next node is the element to be deleted, if yes then point current node to where the next node points (also point deleted node to None)
        else:
            while current.next:
                if current.next.element == element:
                    after_delete_node = current.next.next
                    current.next.next = None
                    current.next = after_delete_node
                    return
                # If next node is not the one to be deleted, then go to next node
                current = current.next

            # If it did not return within while block, then the element is not found
            print(f"\nElement '{element}' is NOT found in the linked list. No node was deleted.")


    def display(self):
        """ Display the elements and the pointers of each node of the linked list """
        # If linked list is empty inform the user about it
        if not self.head:
            print("\nLinked list seems to be empty.")
            return

        # Traverse the linked list, printing the element of each node
        print("\nLinked list:")
        current = self.head
        while current:
            # Print the element of the node, and represent the pointer as arrow pointing to next node
            print(f"{current.element} -> ", end="")
            # Assigns the tail to the last node (decided to assign it in display method, because display is always called every change in linked list)
            if not current.next:
                self.tail = current
            # Go to next node
            current = current.next
        print()


    def count(self):
        """ Return the number of nodes the linked list has """
        # If linked list is empty, return 0 because no nodes
        if not self.head:
            return 0

        # Traverse the linked list, incrementing the counter as each node passes
        counter = 0
        current = self.head
        while current != None:
            current = current.next
            counter += 1
        # Return number of nodes after traversing the entire linked list
        return counter


    def reverse(self, node):
        """ Reverse the linked list recursively """
        # Base case: if at the end of the linked list
        if not node.next:
            # Swap the head and tail, and point the new tail to none/null
            self.tail, self.head = self.head, self.tail
            self.tail.next = None
            # Return the current node aka new head (received as the node at right by the previous 2nd to the last node)
            return self.head
        
        # Point the node at the right to current node (left)
        node_at_right = self.reverse(node.next)
        node_at_right.next = node
        # Return current node (received as the node at right by the node at left)
        return node

    def search(self, element):
        """ Find the first node containing the given element """
        # Traverse the linked list until the given element is found
        current = self.head
        position = 1
        while current:
            # If found, then print its position
            if current.element == element:
                print(f"\nElement '{element}' is found at position {position}.")
                return
            # Go to next node
            current = current.next
            position += 1

        # If it did not return within while block, then the element is not found
        print(f"\nElement '{element}' is NOT found in the linked list.")
            


class App:
    """ Holds the linked list, manages communication between user and program """
    input_choice_keys = {1: "create list", 2: "add at beginning", 3: "add after", 4: "delete", 5: "display", 6: "count", 7: "reverse", 8: "search", 9: "quit"}

    def __init__(self):
        self.ll = None
        self.main_menu()

    def main_menu(self):
        """ Shows user possible commands and ask which one to execute """
        print("\nMain Menu\n")
        print("[1] Create list\n[2] Add at beginning\n[3] Add after\n[4] Delete\n[5] Display\n[6] Count\n[7] Reverse\n[8] Search\n[9] Quit\n")

        # Ask user what to do (with input checks)
        while True:
            try:
                choice = int(input("What do you want to do?  ")) 
                if choice not in self.input_choice_keys:
                    print("\nChoice must be 1-9 inclusive.\n")
                    continue
            except (TypeError, ValueError):
                print("\nOnly enter the assigned number for your choice (e.g., 3).\n")
            else:
                break

        # Execute commands depending on user input
        self.input_manager(choice)

    def input_manager(self, choice):
        """ Execute commands based on user input """
        if self.input_choice_keys[choice] == "create list":
            # If a link list already exists, ask the user if its okay to overwrite the current linked list to create a new one
            if self.ll and self.ll.count() != 0:
                while True:
                    try:
                        create_new_ll = input("\nLinked list already exists. Would you like to create a new one, overwriting the current linked list? [y/n]:  ")[0].lower()
                        if create_new_ll == "n":
                            input("\nPress enter to proceed ...  ")
                            self.main_menu()
                        elif create_new_ll == "y":
                            break
                    except IndexError:
                        continue

            # Create a linked list
            self.ll = Linked_List()
            # Asks infos needed to create the nodes of the linked list
            elements = self.ask_ll_info()
            # Add the nodes to the linked list using the given elements, then display the linked list
            self.ll.create_list(elements)
            self.ll.display()

        elif self.input_choice_keys[choice] == "add at beginning":
            # Ensures the linked list exists
            if self.ll_exist():
                # Ask for an element to insert at the beginning, insert it, then display the linked list
                element = self.ask_for_element("\nEnter element to insert at the beginning:  ")
                self.ll.add_at_beginning(element)
                self.ll.display()

        elif self.input_choice_keys[choice] == "add after":
            # Ensures the linked list exists, and that it is not empty
            if self.ll_exist() and not self.ll_empty():
                # Ask for element to insert, and the position (1 based-index) where to insert the element (element is inserted after the given position)
                element = self.ask_for_element("\nEnter element to insert:  ")
                position = self.ask_for_position("\nEnter position after which the element will be inserted:  ")
                # Insert the element, then display the linked list
                self.ll.add_after(element, position)
                self.ll.display()

        elif self.input_choice_keys[choice] == "delete":
            # Ensures the linked list exists, and that it is not empty
            if self.ll_exist() and not self.ll_empty():
                # Asks for the element to delete, delete it if found, then display the linked list
                element = self.ask_for_element("\nEnter element to delete:  ")
                self.ll.delete(element)
                self.ll.display()

        elif self.input_choice_keys[choice] == "display":
            # Display the linked list if it exists
            if self.ll_exist():
                self.ll.display()

        elif self.input_choice_keys[choice] == "count":
            # Prints the number of nodes in the linked list if it exists
            if self.ll_exist():
                print(f"\nLinked list has {self.ll.count()} node(s).")

        elif self.input_choice_keys[choice] == "reverse":
            # Ensures the linked list exists, and that it is not empty
            if self.ll_exist() and not self.ll_empty():
                # Reverse, then display the link list
                self.ll.reverse(self.ll.head)
                self.ll.display()

        elif self.input_choice_keys[choice] == "search":
            # Ensures the linked list exists, and that it is not empty
            if self.ll_exist() and not self.ll_empty():
                # Asks for element to search, and search for it
                element = self.ask_for_element("\nEnter element to search:  ")
                self.ll.search(element)

        elif self.input_choice_keys[choice] == "quit":
            # Exits the program
            sys.exit("\nClosing the program ...\n")

        # Add a buffer after every command to let user read infos before going back to main menu
        input("\nPress enter to proceed ...  ")
        self.main_menu()


    def ask_ll_info(self):
        """ Asks the elements of the nodes of the linked list """
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
                break

        # Ask for the elements for each node
        elements=[]
        for i in range(number_of_nodes):
            element = self.ask_for_element(f"Enter your element[{i}]:  ")
            elements.append(element)
        return elements

    def ask_for_element(self, msg):
        """ Ask for an element/value/data, and converts it to int or float if necessary """
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

    def ll_empty(self):
        """ Check if linked list is empty """
        if self.ll.count() == 0:
            print(f"\nLinked List has {self.ll.count()} nodes. I suggest adding an element at the beginning by choosing 2 in Main Menu.")
            return True
        return False

    def ask_for_position(self, msg):
        """ Ask for a position (1-based index) """
        while True:
            try:
                position = int(input(msg))
                if position <= 0:
                    print("\nPosition must be positive (first position is 1).")
                    continue
                elif position > self.ll.count():
                    print(f"\nThere are only {self.ll.count()} node(s).")
                    continue
            except (TypeError, ValueError):
                print("\nPosition must be an integer.")
                continue
            else:
                return position



if __name__ == "__main__":
    App()