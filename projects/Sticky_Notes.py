#/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox

###########MAIN_FRAME##############
root = tk.Tk()
root.title('Sticky Notes')
root.geometry('400x500')

###########FUNCTIONS##############
class TextEditor:
    def __init__(self, root): #Pass the main_window
        self.root = root
        self.text_area = tk.Text(self.root) #Create the write box
        self.text_area.pack(fill=tk.BOTH, expand=1) # Fill the write box(X,Y) in the whole window
        self.current_open_file = '' # file $PATH

    def editor_new(self): #New Window
        self.text_area.delete('1.0',tk.END) # Delete the everything from the index[0] to END, '1.0'==> meaning the first letter
        self.current_open_file='' #Empty file
        
    
    def editor_open(self):
        filename=filedialog.askopenfilename() # Pops up a box to open a system file 

        if filename: # if filename have letters/info
            self.text_area.delete('1.0', tk.END) # Wipe it from index[0] to END
            with open(filename, 'r') as file: # Open the filename and get what is inside
                  self.text_area.insert('1.0', file.read())# Insert the text from index[0] using the file 'file'
            self.current_open_file=filename # Current filename

    def editor_save(self):
        if not self.current_open_file: 
            new_file_path= filedialog.asksaveasfilename() # If no filename ask for one
            if new_file_path:
                        self.current_open_file=new_file_path # Save the file
            else:
                return # IS IT A GOOD PRACTICE ?? LETS FIND OUT LATER.
        with open(self.current_open_file, 'w') as file: # Open the filename and get what is inside
             file.write(self.text_area.get('1.0', tk.END)) # Paste from index[0] to END
   
    def editor_exit(self):
     if messagebox.askokcancel('Exit', 'Confirm exit.'): # Open the messagebox
            self.root.destroy()  # IS DESTROY AGGRESIVE? LETS FIND OUT LATER


    ########IDEAS#####
    #######ADD SHORCUTS : CRL+C,V,X, RESIZE(X,Y,), alt+a, etc.
    

editor = TextEditor(root) # NEW IDEA !!!!!!!!!Editor is running TextEditor.__init__(root)!!!!!!!

###########MEN_BAR##############
menu_bar = tk.Menu(root) # Create menu and asign root_window as a parent
root.config(menu=menu_bar) # Add as a main menu to root window

####MEUN_ADDS#######
menu1 = tk.Menu(menu_bar, tearoff=0) # Create a menu inside menu bar,  I forgot what TEAROFF=0  does :,(  Kind of attching the menu1 to main menu i will not be a floating window.
menu_bar = menu_bar.add_cascade(label='Archivo',menu=menu1) # Show the menu_bar(assign_name, assign menu1 as a child of menu_bar)
menu1.add_command(label='New', command=editor.editor_new) # Add an option and assign a command defined in the FUNCTIONS section
menu1.add_command(label='Open', command=editor.editor_open) #Same
menu1.add_command(label='Save', command=editor.editor_save) #Same
menu1.add_command(label='Exit', command=editor.editor_exit) #Same

###########RUN_THE_ WINDOW##############
root.attributes('-topmost', True) # Sticky window, always on top
root.mainloop() #RUUUN......

