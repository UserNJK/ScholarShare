import tkinter as tk

class ForgotPasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Create a label for "Forgot Password"
        title_label = tk.Label(self.root, text="Forgot Password", font=("Arial", 16))
        title_label.pack(pady=10)
        
        # Create an email input field
        email_label = tk.Label(self.root, text="Your email address:")
        email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)
        
        # Create a "Send Link" button
        send_button = tk.Button(self.root, text="Send Link", command=self.send_link)
        send_button.pack(pady=10)
    
    def send_link(self):
        email = self.email_entry.get()
        if not email:
            # Show a message if email is empty
            error_label = tk.Label(self.root, text="Email required!", foreground="red")
            error_label.pack()
        else:
            # Implement the logic to send a reset password link here
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ForgotPasswordApp(root)
    root.mainloop()
