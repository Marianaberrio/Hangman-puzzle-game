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

       # creates rgb colors to use on the buttons
        purple = color_rgb(111, 89, 80)
        orange = color_rgb(165, 100, 53)
        pink = color_rgb(240, 220, 215)
        brick = color_rgb(173, 121, 91)
        brown = color_rgb(143, 94, 54)
	
	#color list
        color_list = [purple, orange, pink, brick, brown]
	
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill(random.choice(color_list)) #chooses a random color for every button
        self.rect.draw(win)
        self.hidden_letter = Text(center, hidden_letter)
        self.hidden_letter.draw(win)
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

    def undraw(self):
        self.rect.undraw()
        self.hidden_letter.undraw()


class inventory:
    
    def __init__(self,open= False):
        self.open = open
        self.inventory_button = Button(win, Point(50, 650), 40, 20, "INV")
        self.letter_list = []
    

    def draw_inventory(self):

        self.inventory_window = GraphWin("INVENTORY(Don't close inventory)",500,500)
        self.inventory_window.setBackground("green")
        self.open = True


    def add_letter(self,letter,grid_counterX,grid_counterY):

        centerX, centerY = 40,40
        
        if self.open:
            
            self.stored_letter = Button(self.inventory_window,Point(centerX*grid_counterX,centerY*grid_counterY),30,30,letter.get_hidden_letter())
            self.letter_list.append(self.stored_letter)


    def use_letter(self,stored_letter):
        pt = win.getMouse()
        if self.stored_letter.clicked(pt):
            print(stored_letter.hidden_letter)

# --- Functions ---
# Draws a piece of the Hangman picture when an incorrect letter is guessed. The piece that
# is drawn depends on the number of fails that the player has got accumulated

def drawPiece(strike, win, win_width, win_height, win_hangmanpic):
    
	hangman_yaxis = win_width / 2.2  # The body of the hangman will align with this axis
    
	if strike == 1:
		# Fail 1: Draw the post
		line1 = Line(Point(win_width - win_width / 3, 100), Point(win_width - win_width / 3, 300))
		line1.draw(win)
		win_hangmanpic.append(line1)
		line2 = Line(Point(win_width - win_width / 3, 300), Point(hangman_yaxis, 300))
		line2.draw(win)
		win_hangmanpic.append(line2)
		line3 = Line(Point(hangman_yaxis, 300), Point(hangman_yaxis, 270))
		line3.draw(win)
		win_hangmanpic.append(line3)
        
	elif strike == 2:
		# Fail 2: Draw head
		circle4 = Circle(Point(hangman_yaxis, 254), 16)
		circle4.draw(win)
		win_hangmanpic.append(circle4)
        
	elif strike == 3:
		# Fail 3: Draw the torso
		line5 = Line(Point(hangman_yaxis, 238), Point(hangman_yaxis, 180))
		line5.draw(win)
		win_hangmanpic.append(line5)
        
	elif strike == 4:
		# Fail 4: Draw the left arm
		line6 = Line(Point(hangman_yaxis, 225), Point(hangman_yaxis - 20, 200))
		line6.draw(win)
		win_hangmanpic.append(line6)
        
	elif strike == 5:
		# Fail 5: Draw the right arm
		line7 = Line(Point(hangman_yaxis, 225), Point(hangman_yaxis + 20, 200))
		line7.draw(win)
		win_hangmanpic.append(line7)
        
	elif strike == 6:
		# Fail 6: Draw the left leg
		line8 = Line(Point(hangman_yaxis, 180), Point(hangman_yaxis - 15, 135))
		line8.draw(win)
		win_hangmanpic.append(line8)
        
	elif strike == 7:
		# Fail 7: Draw the right leg
		line9 = Line(Point(hangman_yaxis, 180), Point(hangman_yaxis + 15, 135))
		line9.draw(win)
		win_hangmanpic.append(line9)
    
    # GAME OVER

# Function to check if they can advance to a new level
def check_game_level():
    global chosen_row, path, word, win, number_of_hidden_letters # retrieve global variables
    if chosen_row == inv.letter_list: # compare csv picked word to word in the letter_list variable in class method
        print("Congrats! The game is complete." # If it is equals, display msg
              "You guessed the word right!"
              "You can now move onto the next level.")
        wordPicker(path) # and re-run the function with new words etc. So new level.
        wordSplitter(word)
        create_hidder(win, number_of_hidden_letters, path)
    else: # else keep trying and stay on the same level.
        print("Keep trying!")
        create_hidder(win, number_of_hidden_letters, path)
        
#Randomly chooses word from the csv file
def wordPicker(path):
    with open(path) as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        return chosen_row

#Returns number of hidden_letters of chosen word
def wordSplitter(word):
    global split_word
    word_to_split = str(word[0]).upper() #This is a list indexing because wordPicker() returns a single index list
    split_word = list(word_to_split)
    print(word_to_split)
    return split_word

#Draws the number of lines according to the number of letterrs in the chosen word
def lineDrawer():

    x1,y1 = 100,50
    x2,y2 = 50,50
    hidden_letterSpace = Line(Point(x1,y1),Point(x2,y2))
    hidden_letterSpace.setFill("black")
    hidden_letterSpace.setWidth(3)
    hidden_letterSpace.draw(win)

    i = 1
    while i < number_of_hidden_letters:
        x1 += 60
        x2 += 60
        hidden_letterSpace = Line(Point(x1,y1),Point(x2,y2))
        hidden_letterSpace.setFill("black")
        hidden_letterSpace.setWidth(3)
        hidden_letterSpace.draw(win)
        i += 1

#Creates buttons containing the random and correct letters that when pressed they will return that letter
def create_hidder(win,number_of_hidden_letters,path):
    global button_list
    global random_hidden_letter_presser
    button_list = []
    
    pt = win.getMouse()


    i = 0
    for letter in split_word:
        centerX1 = randint(50,640)
        centerY1 = randint(80,640)
        width1 = randint(30,100)
        height1 = randint(30,100)
        correct_hidden_letter_presser = Button(win,Point(centerX1,centerY1),width1,height1, letter)

        button_list.append(correct_hidden_letter_presser)

    while i < number_of_hidden_letters+10:
        centerX2 = randint(50,640)
        centerY2 = randint(80,640)
        width2 = randint(30,100)
        height2 = randint(30,100)
        lines = open(path).read().splitlines()
        chosen_random_hidden_letter = random.choice(lines)


        random_hidden_letter_presser = Button(win,Point(centerX2,centerY2),width2,height2, chosen_random_hidden_letter)

        button_list.append(random_hidden_letter_presser)
        i+=1


win = GraphWin("Hangman",700,700)
win.setBackground(color_rgb(212,198,66))

number_of_hidden_letters = len(wordSplitter(wordPicker("C:\\Users\\leomu\\OneDrive\\Documents\\UNIVERSIDAD\\2021-2022\\S2\\P of programming\\hangman words.csv")))

lineDrawer()

#Quit button
quit_button = Button(win,Point(650,650),40,20,"QUIT")

inv = inventory()

create_hidder(win,number_of_hidden_letters,"C:\\Users\\leomu\\OneDrive\\Documents\\UNIVERSIDAD\\2021-2022\\S2\\P of programming\\letters.txt")

pt = win.getMouse()

grid_counterX = 1
grid_counterY = 1

#Heres the cycle where the chicking for the clicks on the buttons occur
y = 1
while not quit_button.clicked(pt):
    if inv.inventory_button.clicked(pt):
        inv.draw_inventory()

    for button in button_list:
        if button.clicked(pt):
            print(str(button.get_hidden_letter()))
            button.undraw()
            inv.add_letter(button,grid_counterX,grid_counterY)
            y+=1

            if y == 12:
                grid_counterX = 1
                grid_counterY += 1
                y = 1
            else:
                grid_counterX += 1
            #add letter to inventory
    inv.open = True
    
    pt = win.getMouse()
win.close()
