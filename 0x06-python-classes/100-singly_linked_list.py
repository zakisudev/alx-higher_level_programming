#!/usr/bin/python3
" Define classes for a single linked list "


class Node:
    " Represent a node in a singly linked list "

    def __init__(self, data, next_node=None):
        """ Initializes a new Node

        Args:
            data (int): Data of new Node
            next_node (Node): The next node of the new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        " Get/set the data of the Node "
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        " Get/set the next node of the Node "
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    " Represent a singly linked list "

    def __init__(self):
        " Initializes and new Singley linked list "
        self.__head = None

    def sorted_insert(self, value):
        """ Insert a new Node to the Singly linked list

        The node is inserted into the list at the list at
        the ordered numerical position

        Args:
            value (Node): The new Node to insert
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str(self):
        " Define the print() representation of Singly Linked List "
        linkedList = []
        temp = self.__head
        while temp is not None:
            linkedList.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(linkedList))
