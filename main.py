
#Imports
import tkinter as tk
import random
from time import sleep as wait


#Startup
with open("startupinfo.txt", "r", encoding="utf-8") as startup:
    contents = startup.read()
with open("notes.txt", "r", encoding="utf-8") as notes:
    notes = notes.read()

root = tk.Tk()
root.geometry("1000x500")
root.attributes("-topmost", True)
root.attributes("-fullscreen", True)
root.attributes("-full")
root.deiconify()
root.configure(bg="black")
root.title("Commands")
output_text = tk.Text(root, wrap=tk.WORD, font=("s", 12))
output_text.configure(bg='black')
output_text.configure(fg='green')
output_text.configure(borderwidth=0)
output_text.config(state="disabled")
output_text.configure()
output_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
marker = tk.Label(root, text=">>>", font=("TkDefaultFont", 12))
marker.configure(bg='black', fg='green')
marker.pack(side=tk.LEFT, padx=10, pady=10)
command_input = tk.Entry(root, font=("TkDefaultFont", 12), bd=0)
command_input.configure(bg='black', fg='green')
command_input.pack(side=tk.LEFT, padx=0, pady=10, ipady=2)
command_input.focus_set()
root.bind("<Return>", lambda event: run_command())
root.update()
root.geometry(f"{output_text.winfo_width()}x{output_text.winfo_height() + 20}")
command_input.config(width=0)
output_text.replace("1.0","end", contents)

root.update()

#Commands
def OT_Disabler():
    output_text.config(state="disabled")
def OT_Enabler():
    output_text.config(state="normal")

def write(wr):
    OT_Enabler()
    output_text.insert(tk.END,wr)
    OT_Disabler()

def clear_input():
    command_input.delete(0, tk.END)


def run_command():
    command = command_input.get()
    OT_Enabler()
    output_text.insert(tk.END, f">>> {command}\n")

    # Check special commands list
    if any(special_command in command for special_command in special_commands):
        wait_for_argument()
        OT_Disabler()
    else:
        # Check regular commands dictionary
        if command in commands:
            output_text.insert(tk.END, commands[command]() + "\n")
            OT_Disabler()
        else:
            # Command not found, output error message
            output_text.insert(tk.END, f"{command} is not a valid command.\nPlease enter a valid command:\n")
            OT_Disabler()

    command_input.delete(0, tk.END)

def help_command():
    return "Available commands:\n" + "\n".join(commands.keys())

def quit_command():
    root.destroy()

def close_terminal_command():
    root.destroy()

def clear_command():
    OT_Enabler()
    command_input.delete(0, tk.END)
    output_text.replace("1.0", "end", contents + "\n")
    OT_Disabler()

def test_command():
    clear_input()

def color_change_command():
    if special_commands.keys() in command_input.get():
        print ("success!")
    clear_command()

def wait_for_argument():
    log = command_input.get()
    log = log[5:]
    write(log)




def notes_command():
    write(wr=notes)
    clear_input()

def wr():
    wrone = commands.get()
    write(wrone)



#Dictionaries
commands = {
    "help": help_command,
    "quit": quit_command,
    "close": quit_command,
    "clear": clear_command,
    "test": test_command,
    "color": color_change_command,
    "notes": notes_command
    }

special_commands =( "write")

scommands = ("color")

#More Setup
write(contents+"\n")
#Root Window Setup
root.mainloop()
