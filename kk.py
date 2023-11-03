import tkinter as tk
from tkinter import ttk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK with your service account credentials
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "scholarshare-6a4dc",
  "private_key_id": "1151b1e9f203ce4935a6d871c6feccdf1d78fbfe",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDB4Kd1UgJOCMGT\n6g5onTZtrW5NLO5DY8rj2NVBQgK1d/kbMYB9LaWQTuaYVamWOCT54ZbSsPKGJ+8i\nfhSU9V1gaaAYdx5a0iXGOVIJ1r4jRmVtPM/BCSmAN/pDcvfAfKbrJKwE0RiAJkGP\nntwi1LbEmgADW68qnPJh4eeRNDuiLI+DUwxDfaPTgktjvvoMGcgY574W2MDjJ/qr\nUmTricP6PCj3XcUYEaSdP4VzuX6SXZ0JIGLa0++d4MErM4SgsHZobhHFvRe2ztbJ\nLG1WSKf0AKfOUL9bwdfRmJmt+u1GuoAoqb5w5ZYt+FzgcB35ejIcYU4uQv+EC3aK\nJ5eK5QxnAgMBAAECggEAA+OXPOrlUBU4Z+TVtK5GEiIyI/1Q+mkt52wMNVnn3dB+\nOjN26E71q2QZyFgDvjvPgnN/YdKpOTtppfr0bIwhjW1PdbjXgMyAjD1UfsQHjyJA\ns0NzQYKNHGwhgvttKnSuCsVgpKU8KCcQHF6zFDnhiaCIb9HzbZ3sb7fU4LNNYoxh\noIZUV3sX+T6EAKvJSzdyAWG8utyMZfphrLaCRsw219RtQ/D/Lsjno0vx6B4WAaZq\nlQT4TQMI7l3oAT5c5z/zFxBy1nmqRUNQj+gi47WxkLz6ldD7fa7Z56qKFW/oQX/6\n/ae7ACAba8ioFPItjfF5xA13YzHsncWDGg+o/mbQ+QKBgQDivMgsHgukRcVE54/F\nySym/QvnTvrDlUXHkh45tbUigs0Td1GU8vfLfMfEq2jubC2F0OxSkWw2vai8U7ME\npt7F+kww5QN6W8Z+NmI1Tf4+CLaJDS+rFkKGOacGfJ8y8M4i54Rq5uDEtdo72w0A\nqIS7rLQjK1RTcBJ360vQRA+jRQKBgQDa5jWBpRZDvLtAowrVPYZJFzK7sF7qy3bn\ngUkQHEfVmaBoOilYlwfZsxmEqaQZGRhyF/li9YyCka4mTCZUD2OSJrCu7f+xplFG\ncql6fCU4xYHfFFYw14SJRRrS20m5TR1CDbKhbsNWTGrciwaL7c5SgKDvRpenZhQk\nkLn3tPW1uwKBgQDIeZabu20bsDz98ahjfr6mX3MY7/I04FU0YfOrnwgrHW/p2EQf\n6LxEBW40bEJ5HNkbSmDJmJ8Pv53j9jWA1XJ/phGb4cGzfFYC3l7zNqSngNi0UR5m\nrWXgfDU8PRAd4GDC5+VjCASQqSHubn4OqPHDZq5XskX7CEqsETWVTbht6QKBgQCH\n/dsh9vj1DixbBK+3OKjTgbkAB5uATPVK7/P/MUKjffS8q92B7xpucikZVPbgrMmW\nIDTL+PbZKz5BBrANKx5V7vl3Q97FdCksFhIaSUQql/GOMKk3YL0zNp5qfte3aiQS\nJEZkqlZqp8D/0NM5XXz/nm/dF0MiOXWsHcmbDW5U/wKBgQCa7FjyGCc7ROQre+kK\no5ZBtvSzSyN6pniP55vAHG5Qq+FRTqVpsfXXuwvNVN5ztHyHoAeB7fC95gbrwVLS\nWWa/9d88redHv2Zqd6rAVhOPJLoJLVMxdy3WJ+I1JrivcDq2YDW/pe8vfycWxyIl\n+QrtRTJFFjuSsO6zdYrXqoXh2Q==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-qdz6y@scholarshare-6a4dc.iam.gserviceaccount.com",
  "client_id": "101171006076980968038",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-qdz6y%40scholarshare-6a4dc.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
)
firebase_admin.initialize_app(cred)

# Access a Firestore database reference
db = firestore.client()

# Now you can interact with Firebase services like Firestore, Realtime Database, Authentication, etc.


class BuildProfileWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Build Profile")
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg="#F0F0F0")


        label_title = ttk.Label(self.root, text="Let's build your profile!", font=("Helvetica", 16), background="#F0F0F0")
        label_title.grid(row=0, column=0, columnspan=2, pady=(30, 0))

        self.create_input_field("Username", "Enter your username", 1)
        self.create_input_field("Date of birth", "DD/MM/YYYY", 2)
        self.create_input_field("Gender", "Enter your gender", 3)
        self.create_input_field("Branch of study", "Enter your branch of study", 4)
        self.create_input_field("Year of Study", "Enter your year of study", 5)

        button_done = ttk.Button(self.root, text="Done", command=self.done_button_clicked)
        button_done.grid(row=6, column=0, columnspan=2, pady=(16, 0))
        button_done.config(width=20)

    def create_input_field(self, label_text, hint_text, row):
        label = ttk.Label(self.root, text=label_text, background="#F0F0F0")
        label.grid(row=row, column=0, pady=(12, 0), padx=16, sticky="w")

        entry = ttk.Entry(self.root)
        entry.insert(0, hint_text)
        entry.grid(row=row, column=1, pady=(12, 0), padx=16, sticky="w")

    def done_button_clicked(self):
        # Add your logic here for handling the "Done" button click
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = BuildProfileWidget(root)
    root.mainloop()