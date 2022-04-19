#Programming hangman game

from graphics import *
import csv
import random
from random import randint


#File directory: "C:\\Users\\leomu\\OneDrive\\Documents\\UNIVERSIDAD\\2021-2022\\S2\\P of programming\\hangman words.csv"

# --- classes ---
class Button:

    # It is activated or deactivated with the activate()
    # and deactivate() methods. The clicked(p) method
    # returns true if the button is active and p is inside it.

    def __init__(self, win, center, width, height, hidden_letter ):
        # Creates a rectangular button, eg:
        # qb = Button(myWin, centerPoint, width, height, 'Quit') 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.hidden_letter  = Text(center, hidden_letter )
        self.hidden_letter .draw(win)
        self.deactivate()

    def clicked(self, p):
        # Returns true if button active and p is inside"
        if self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax:
            return(True)
        # return (self.active and
        #         self.xmin <= p.getX() <= self.xmax and
        #         self.ymin <= p.getY() <= self.ymax)

    def get_hidden_letter(self):
        "Returns the hidden_letter  string of this button."
        return self.hidden_letter .getText()

    def activate(self):
        # Sets this button to 'active'."
        self.active = True

    def deactivate(self):
        # Sets this button to 'inactive'."
        self.active = False



# --- Functions ---

#Randomly chooses word from the csv file
def wordPicker(path):
    with open(path) as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        return chosen_row

#Returns number of hidden_letters of chosen word
def wordSplitter(word):
    global split_word
    word_to_split = str(word[0])
    split_word = list(word_to_split)
    print(word_to_split)
    return split_word

#Draws the number of lines according to the number of letterrs in the chosen word
def lineDrawer():

    x1,y1 = 100,50
    x2,y2 = 50,50
    hidden_letterSpace = Line(Point(x1,y1),Point(x2,y2))
    hidden_letterSpace.setFill(color_rgb(190,76,147))
    hidden_letterSpace.setWidth(3)
    hidden_letterSpace.draw(win)

    i = 1
    while i < number_of_hidden_letters:
        x1 += 60
        x2 += 60
        hidden_letterSpace = Line(Point(x1,y1),Point(x2,y2))
        hidden_letterSpace.setFill(color_rgb(190,76,147))
        hidden_letterSpace.setWidth(3)
        hidden_letterSpace.draw(win)
        i += 1

#Creates buttons containing the random and correct letters that when pressed they will return that letter
def create_hidder(win,number_of_hidden_letters):
    global button_list
    global random_hidden_letter_presser
    button_list = []
    
    pt = win.getMouse()


    i = 0
    while i < number_of_hidden_letters+10:

        lines = open("C:\\Users\\leomu\\OneDrive\\Documents\\UNIVERSIDAD\\2021-2022\\S2\\P of programming\\letters.txt").read().splitlines()
        chosen_random_hidden_letter = random.choice(lines)

        centerX = randint(50,640)
        centerY = randint(80,640)
        width = randint(30,100)
        height = randint(30,100)

        random_hidden_letter_presser = Button(win,Point(centerX,centerY),width,height, chosen_random_hidden_letter)
        button_list.append(random_hidden_letter_presser)

        i+=1

    for letter in split_word:
        correct_hidden_letter_presser = Button(win,Point(centerX,centerY),width,height, letter)
        button_list.append(correct_hidden_letter_presser)
    


win = GraphWin("Hangman",700,700)
win.setBackground(color_rgb(212,198,66))

number_of_hidden_letters = len(wordSplitter(wordPicker("C:\\Users\\leomu\\OneDrive\\Documents\\UNIVERSIDAD\\2021-2022\\S2\\P of programming\\hangman words.csv")))

lineDrawer()

#Quit button
quit_button = Button(win,Point(650,650),40,20,"QUIT")
create_hidder(win,number_of_hidden_letters)

pt = win.getMouse()

#Heres the cycle where the chicking for the clicks on the buttons occur
while not quit_button.clicked(pt):
    for button in button_list:
        if button.clicked(pt):
            print(str(button.get_hidden_letter()))
            #add letter to inventory
    pt = win.getMouse()
win.close()