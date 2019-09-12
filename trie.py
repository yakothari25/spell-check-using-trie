from tkinter import *
import pickle
class Node(object):

    def __repr__(self):
        return "Node({0}, {1}, {2})".format(
            self.value, self.children, self.is_complete)

    def __init__(self,value):
        self.value = value
        self.children = []
        self.is_complete  = False

class Tries(object):

    def __init__(self):
        #if()
        self.node = Node(None)



    def addspell(self,string):
        node = self.node

        for v in string:
            child_values = [child.value for child in node.children]

            if v in child_values:
                index = child_values.index(v)
                node = node.children[index]
            else:
                new_node = Node(v)
                node.children.append(new_node)
                node = new_node

        node.is_complete = True


    def find(self, key):
        node = self.node
        for letter in key:
            child_values = [child.value for child in node.children]
            try:
                index = child_values.index(letter)
            except ValueError:
                return False
            node = node.children[index]
        return node.is_complete



def check():
    global screen1

    screen1 = Toplevel(screen)
    screen1.title("Check Spelling")
    screen1.geometry("300x250")
    global string
    global string_entry
    string = StringVar()
    Label(screen1, text="Please enter String below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Sentence").pack()
    string_entry = Entry(screen1, textvariable=string)
    string_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Check", width=10, height=1, command=checksting).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Clear", width=10, height=1, command=clear).pack()

def checksting():
    string_info = string.get()
    out = "All correct"
    output = " Wrong Spellings: "
    i  = 0;
    for word in string_info.casefold().split():
        if tries.find(word)== False:
            output = output+ "\n"+ word
            i+=1
    if(i==0):
        output = out
    Label(screen1, text = output,fg="red", font=("calibri", 11)).pack()

def clear():
    string_entry.delete(0, END)


def addwords():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Add Words")
    screen1.geometry("300x250")
    global string
    global string_entry
    string = StringVar()
    Label(screen1, text="Please enter String below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="(Keep single space between words)").pack()
    string_entry = Entry(screen1, textvariable=string,width = 30)
    string_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Check", width=10, height=1, command=addstring).pack()

def addstring():
    inputstring = string.get()
    for word in inputstring.casefold().split():
        tries.addspell(word)
    Label(screen1, text="Words added", fg="Green", font=("calibri", 11)).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Clear", width=10, height=1, command=clear).pack()


def saveupdate():
    with open("super.file", "wb") as f:
        pickle.dump(tries, f, pickle.HIGHEST_PROTOCOL)


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("400x300")
    screen.title("Spell Cheaker using Tries")
    Label(text="Spell Cheaker using Tries", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Check String", height="2", width="30", command=check).pack()
    Label(text="").pack()
    Button(text="Add words", height="2", width="30", command=addwords).pack()
    Label(text="").pack()
    Button(text="Save Updates", height="2", width="30", command=saveupdate).pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="Total words added: 235878").pack()
    screen.mainloop()
def addwordsdatabase():
    file = open("word.txt", "r")
    file2 = open("word2.txt", "w")
    n = 1
    for n in range(0, 235883):
        s = file.readline(n).casefold().split()
        try:
            file2.writelines(s[0])
            tries.addspell(s[0])
        except IndexError:
            print(n)

global tries
tries = Tries()

with open("super.file", "rb") as f:
    tries = pickle.load(f)
#addwordsdatabase()


main_screen()