# from graphics import *
# import csv
# from ProgrammingHangmanGame import *
# from InventoryClassTest import *
from graphics import *
from ProgrammingHangmanGame import Button


def inventoryWindow():
    inventory = GraphWin("Inventory")
    inventory.setCoords(0, 0, 100, 100)
    inventory.setBackground("white")
    inventory.getMouse()


def main():
    # Creates the main window
    win = GraphWin()
    win.setCoords(0, 0, 100, 100)

    # win.setBackground("White")

    # Inventory button
    InventoryButton = Button(win, Point(60, 60), 30, 20, "Inventory")  # win, center, width, height, label
    InventoryButton.activate()

    # Test object to test inventory
    TestLetter = Button(win, Point(30, 30), 10, 10, "A")  # win, center, width, height, label
    TestLetter.activate()

    pt = win.getMouse()

    # Opens inventory window when you click the inventory button
    if InventoryButton.clicked(pt):
        # Opens the window inventory
        inventoryWindow()

    # Save item to inventory
    if TestLetter.clicked(pt):
        TestLetter = Button(inventoryWindow, Point(30, 30), 10, 10, "A")
        TestLetter.active()
    # if TestLetter.clicked(iv):
    # TestLetter = Button(inventory, Point(30, 30), 10, 10, "A")
    # TestLetter.deactivate()


main()
