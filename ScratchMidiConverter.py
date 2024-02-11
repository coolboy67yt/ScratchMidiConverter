import tkinter as tk
from tkinter import filedialog
from mido import MidiFile

def convert_to_txt(input_file, output_file):
    midi = MidiFile(input_file)
    with open(output_file, 'w') as txt_file:
        for msg in midi:
            if msg.type == 'note_on':
                pitch = msg.note
                velocity = msg.velocity
                duration = msg.time
                txt_file.write(f'{pitch}/{velocity}/{duration}\n')
    print("Conversion completed successfully!")

def select_input_file():
    input_file_path = filedialog.askopenfilename(filetypes=[("MIDI files", "*.mid")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, input_file_path)

def select_output_file():
    output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, output_file_path)

def convert():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    convert_to_txt(input_file, output_file)

# Create main window
root = tk.Tk()
root.title("Scratch MIDI Converter")
root.iconbitmap('icon.ico')

# Input file selection
input_label = tk.Label(root, text="Select input MIDI file:")
input_label.grid(row=0, column=0, padx=5, pady=5)
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=5, pady=5)
input_button = tk.Button(root, text="Browse", command=select_input_file)
input_button.grid(row=0, column=2, padx=5, pady=5)

# Output file selection
output_label = tk.Label(root, text="Select output text file:")
output_label.grid(row=1, column=0, padx=5, pady=5)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=5, pady=5)
output_button = tk.Button(root, text="Browse", command=select_output_file)
output_button.grid(row=1, column=2, padx=5, pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
