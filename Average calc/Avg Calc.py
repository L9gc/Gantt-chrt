import tkinter as tk

def calculate_average():
    try:
        # Get the test scores from the Entry widgets and convert them to float
        score1 = float(entry1.get())
        score2 = float(entry2.get())
        score3 = float(entry3.get())

        # Calculate the average
        average = (score1 + score2 + score3) / 3
        
        # Display the average in the result_label
        result_label.config(text=f"Average Score: {average:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric scores.")

# Create the main window
root = tk.Tk()
root.title("Test Score Average Calculator")

label1 = tk.Label(root, text="Enter the score for test 1:")
label2 = tk.Label(root, text="Enter the score for test 2:")
label3 = tk.Label(root, text="Enter the score for test 3:")

label1.pack()
entry1 = tk.Entry(root, width=10)
entry1.pack()

label2.pack()
entry2 = tk.Entry(root, width=10)
entry2.pack()

label3.pack()
entry3 = tk.Entry(root, width=10)
entry3.pack()


# Create a button to calculate the average
calculate_button = tk.Button(root, text="Calculate Average", command=calculate_average)
calculate_button.pack()

quit = tk.Button(root, text = "Quit", command = root.destroy)
quit.pack(side="right")

# Create a label to display the average
result_label = tk.Label(root, text="", pady=10)
result_label.pack()

# Run the Tkinter main loop
root.mainloop()
