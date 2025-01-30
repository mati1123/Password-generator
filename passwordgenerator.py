import tkinter
import random
import string 

def generate_password(): # password function
    length = 12 # 12 letter length
    characters = string.ascii_letters + string.digits + string.punctuation # create list varaible with alla letters, digits and special letter
    password = ''.join(random.choice(characters) for i in range(length)) #take random letter from character loop 12 times and join it to a stirng 
    
    password_entry.config(state = "normal") #Make the text editable
    password_entry.delete(0, tkinter.END) #Remove old text to insert new
    password_entry.insert(0,password) #insert new password
    password_entry.config(state="readonly")  #go back to read only


def copy_to_clipboard():
    password = password_entry.get() # Get the generated password from the Entry field
    m.clipboard_clear() # Clear the clipboard to remove any previous copied text
    m.clipboard_append(password) # Copy the new password to the clipboard
    m.update() # Update the GUI to ensure the copied password is available immediately

    

m = tkinter.Tk() # Create the main window and save it to the variable m
m.title("Password Generator") # give the title window 'Password Generator'
m.geometry("500x400") #Give the main window 500x400 pixel size

title_label = tkinter.Label(m, text="Password Generator", font=("Arial", 24, "bold"))   # Creates a label with large bold text in the main window

title_label.pack(pady=10) # Center the label and add 10 pixels of vertical padding

generate_button = tkinter.Button(m, text="Generate Password", font=("Arial", 14), command=generate_password) # Create a button to generate a password
generate_button.pack(pady=10) # Place the button below the title with 10 pixels of vertical padding


password_entry = tkinter.Entry(m, font=("Arial", 14), bg="white", width=30, justify="center") # Creates an Entry field inside the main window (m) with Arial font size 14, white background, width of 30 characters, and center-aligned text for displaying the generated password.
password_entry.pack(pady=10)

copy_button = tkinter.Button(m, text="Copy", font=("Arial", 14), command=copy_to_clipboard) # Create a button to copy password
copy_button.pack(pady=10) 

m.mainloop() #Starts the gui to have the window open