# import os
# import random
# import tkinter as tk
# from tkinter import messagebox
# import pyttsx3
# from playsound import playsound  # Added to play your recorded MP3 files

# class FunMathKidsApp:
#     def __init__(self, root):
        
#         # 1. SETUP THE APP WINDOW
#         self.root = root
#         self.root.title("FunMath Kids SA")
#         self.root.geometry("600x500")
#         self.root.configure(bg="#E0F7FA")  # Light blue background

#         # 2. START THE TEXT-TO-SPEECH ENGINE
#         try:
#             self.speech_engine = pyttsx3.init()
#         except Exception:
#             self.speech_engine = None

#         # 3. SET UP GAME VARIABLES
#         self.language = "English"
#         self.score = 0
#         self.num1 = 0
#         self.num2 = 0
#         self.correct_answer = 0
        
#         # 4. LOAD IMAGES SAFELY (App won't crash if files are missing)
#         self.star_img = self.load_image("images/star.png")   # Star graphic
#         self.happy_img = self.load_image("images/happy.png") # Happy face graphic
#         self.sad_img = self.load_image("images/sad.png")     # Sad face graphic

#         # 5. SHOW THE WELCOME SCREEN FIRST
#         self.show_welcome_screen()

#     def load_image(self, path):
#         """Helper tool to look for and load a picture safely."""
#         if os.path.exists(path):
#             return tk.PhotoImage(file=path)
#         return None

#     def speak(self, text):
#         """Helper tool to make the computer talk using Text-to-Speech."""
#         if self.speech_engine:
#             self.speech_engine.say(text)
#             self.speech_engine.runAndWait()

#     def play_sound_file(self, filename, fallback_text):
#         """Plays recorded audio for Afrikaans, or falls back to Speech if missing."""
#         path = os.path.join("audio", filename)
        
#         if self.language == "Afrikaans" and os.path.exists(path):
#             try:
#                 # Play the MP3 file without freezing the game window
#                 self.root.after(10, lambda: playsound(path, block=False))
#             except Exception:
#                 # If something goes wrong playing the file, use the fallback speech
#                 self.speak(fallback_text)
#         else:
#             # If English, or if the Afrikaans MP3 is missing, use Text-to-Speech
#             self.speak(fallback_text)

#     def clear_screen(self):
#         """Clears all elements off the window so we can draw a new screen."""
#         for widget in self.root.winfo_children():
#             widget.destroy()

#     def show_welcome_screen(self):
#         """Screen 1: Language selection screen."""
#         self.clear_screen()

#         # Big Title
#         title = tk.Label(self.root, text="🧮 FunMath Kids SA 🌟", font=("Comic Sans MS", 28, "bold"), bg="#E0F7FA", fg="#006064")
#         title.pack(pady=30)

#         # Instruction Label
#         instruction = tk.Label(self.root, text="Choose your language / Kies jou taal:", font=("Comic Sans MS", 16), bg="#E0F7FA")
#         instruction.pack(pady=10)

#         # English Selection Button
#         en_button = tk.Button(self.root, text="English", font=("Comic Sans MS", 16, "bold"), bg="#4CAF50", fg="white", width=12,
#                               command=lambda: self.start_game("English"))
#         en_button.pack(pady=10)

#         # Afrikaans Selection Button
#         af_button = tk.Button(self.root, text="Afrikaans", font=("Comic Sans MS", 16, "bold"), bg="#FF9800", fg="white", width=12,
#                               command=lambda: self.start_game("Afrikaans"))
#         af_button.pack(pady=10)

#         # If a star image exists, display it at the bottom as decoration
#         if self.star_img:
#             star_label = tk.Label(self.root, image=self.star_img, bg="#E0F7FA")
#             star_label.pack(pady=15)

#     def start_game(self, chosen_language):
#         """Triggers the start of the math application session."""
#         self.language = chosen_language
#         self.score = 0
        
#         # Audio feature: Play introductory welcome message
#         if self.language == "English":
#             self.speak("Welcome to Fun Math Kids!")
#         else:
#             # Tries to play 'welkom.mp3'
#             self.play_sound_file("welkom.mp3", "Welkom by Pret Wiskunde!")

#         self.show_game_screen()
#         self.ask_new_question()

#     def show_game_screen(self):
#         """Screen 2: The active arithmetic playing field."""
#         self.clear_screen()

#         # Score Tracker layout
#         self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Comic Sans MS", 14, "bold"), bg="#E0F7FA")
#         self.score_label.pack(anchor="ne", padx=20, pady=10)

#         # Math Question Display
#         self.math_label = tk.Label(self.root, text="", font=("Comic Sans MS", 36, "bold"), bg="#E0F7FA", fg="#01579B")
#         self.math_label.pack(pady=15)

#         # User Input text box
#         self.input_box = tk.Entry(self.root, font=("Comic Sans MS", 24), justify="center", width=5)
#         self.input_box.pack(pady=10)
#         self.input_box.focus()
        
#         # Super handy shortcut: pressing 'Enter' on keyboard checks the answer directly!
#         self.input_box.bind("<Return>", lambda event: self.check_answer())

#         # Validation Action Button
#         btn_text = "Check Answer! ✔️" if self.language == "English" else "Kontroleer! ✔️"
#         self.check_button = tk.Button(self.root, text=btn_text, font=("Comic Sans MS", 16, "bold"), bg="#2196F3", fg="white",
#                                       command=self.check_answer)
#         self.check_button.pack(pady=10)

#         # Visual Feedback Label (For the flashing animations)
#         self.feedback_label = tk.Label(self.root, text="", font=("Comic Sans MS", 18, "bold"), bg="#E0F7FA")
#         self.feedback_label.pack(pady=5)

#         # Visual Feedback Image (Happy or Sad face placement)
#         self.image_label = tk.Label(self.root, bg="#E0F7FA")
#         self.image_label.pack(pady=5)

#     def ask_new_question(self):
#         """Resets fields and loads a new randomized problem."""
#         self.input_box.delete(0, tk.END)
#         self.feedback_label.config(text="")
#         self.image_label.config(image="")

#         # Basic Addition Generator
#         self.num1 = random.randint(1, 10)
#         self.num2 = random.randint(1, 10)
#         self.correct_answer = self.num1 + self.num2

#         self.math_label.config(text=f"{self.num1} + {self.num2} = ?")

#         # Read math problem to the student out loud
#         if self.language == "English":
#             self.speak(f"What is {self.num1} plus {self.num2}?")
#         else:
#             self.speak(f"Wat is {self.num1} plus {self.num2}?")

#     def flash_feedback(self, execution_count, main_color, background_color):
#         """Feature: Alternates text color back and forth to simulate flashing."""
#         if execution_count > 0:
#             # Find what color the text currently is, and swap it
#             current_color = self.feedback_label.cget("foreground")
#             new_color = background_color if current_color == main_color else main_color
            
#             self.feedback_label.config(fg=new_color)
            
#             # Call this function again in 250 milliseconds (quarter of a second)
#             self.root.after(250, lambda: self.flash_feedback(execution_count - 1, main_color, background_color))

#     def check_answer(self):
#         """Verifies mathematical entry and provides reactive feedback."""
#         kid_typing = self.input_box.get().strip()

#         # Sanity check validation
#         if not kid_typing.isdigit():
#             error_msg = "Please type a number!" if self.language == "English" else "Voer 'n getal in!"
#             messagebox.showwarning("Oops!", error_msg)
#             return

#         kid_answer = int(kid_typing)

#         # LOGIC PATHWAY A: CORRECT ANSWER
#         if kid_answer == self.correct_answer:
#             self.score += 1
#             self.score_label.config(text=f"Score: {self.score}")
            
#             text_reply = "Awesome Job! 🎉" if self.language == "English" else "Mooi so! 🎉"
#             self.feedback_label.config(text=text_reply, fg="#4CAF50")
            
#             if self.happy_img:
#                 self.image_label.config(image=self.happy_img)
                
#             # Plays reg.mp3 or speaks backup text
#             self.play_sound_file("reg.mp3", "Correct!")
            
#             # Trigger the flashing animation feature
#             self.flash_feedback(6, "#4CAF50", "#E0F7FA")

#         # LOGIC PATHWAY B: INCORRECT ANSWER
#         else:
#             text_reply = "Try Again! 🦊" if self.language == "English" else "Probeer weer! 🦊"
#             self.feedback_label.config(text=text_reply, fg="#F44336")
            
#             if self.sad_img:
#                 self.image_label.config(image=self.sad_img)
                
#             # Plays verkeerd.mp3 or speaks backup text
#             self.play_sound_file("verkeerd.mp3", "Wrong answer, try again!")
            
#             # Trigger the flashing animation feature
#             self.flash_feedback(6, "#F44336", "#E0F7FA")

#         # Continual progression loop: Wait 2.5 seconds, then load the next problem
#         self.root.after(2500, self.ask_new_question)


# # Launcher initialization block
# if __name__ == "__main__":
#     window = tk.Tk()
#     app = FunMathKidsApp(window)
#     window.mainloop()
import os
import random
import tkinter as tk
from tkinter import messagebox
import pyttsx3  # We use ONLY this for talking out loud!

class FunMathKidsApp:
    def __init__(self, root):
        # 1. SETUP THE APP WINDOW
        self.root = root
        self.root.title("FunMath Kids SA")
        self.root.geometry("600x500")
        self.root.configure(bg="#E0F7FA")  # Light blue background

        # 2. START THE TEXT-TO-SPEECH ENGINE
        try:
            self.speech_engine = pyttsx3.init()
        except Exception:
            self.speech_engine = None

        # 3. SET UP GAME VARIABLES
        self.language = "English"
        self.score = 0
        self.num1 = 0
        self.num2 = 0
        self.correct_answer = 0
        
        # 4. LOAD IMAGES SAFELY (App won't crash if files are missing)
        self.star_img = self.load_image("images/star.png")   
        self.happy_img = self.load_image("images/happy.png") 
        self.sad_img = self.load_image("images/sad.png")     

        # 5. SHOW THE WELCOME SCREEN FIRST
        self.show_welcome_screen()

    def load_image(self, path):
        """Helper tool to look for and load a picture safely."""
        if os.path.exists(path):
            return tk.PhotoImage(file=path)
        return None

    def speak(self, text):
        """Helper tool to make the computer talk out loud."""
        if self.speech_engine:
            try:
                self.speech_engine.say(text)
                self.speech_engine.runAndWait()
            except Exception:
                pass

    def clear_screen(self):
        """Clears all elements off the window so we can draw a new screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        """Screen 1: Language selection screen."""
        self.clear_screen()

        # Big Title
        title = tk.Label(self.root, text="🧮 FunMath Kids SA 🌟", font=("Comic Sans MS", 28, "bold"), bg="#E0F7FA", fg="#006064")
        title.pack(pady=30)

        # Instruction Label
        instruction = tk.Label(self.root, text="Choose your language / Kies jou taal:", font=("Comic Sans MS", 16), bg="#E0F7FA")
        instruction.pack(pady=10)

        # English Selection Button
        en_button = tk.Button(self.root, text="English", font=("Comic Sans MS", 16, "bold"), bg="#4CAF50", fg="white", width=12,
                              command=lambda: self.start_game("English"))
        en_button.pack(pady=10)

        # Afrikaans Selection Button
        af_button = tk.Button(self.root, text="Afrikaans", font=("Comic Sans MS", 16, "bold"), bg="#FF9800", fg="white", width=12,
                              command=lambda: self.start_game("Afrikaans"))
        af_button.pack(pady=10)

        # Display star image if it exists
        if self.star_img:
            star_label = tk.Label(self.root, image=self.star_img, bg="#E0F7FA")
            star_label.pack(pady=15)

    def start_game(self, chosen_language):
        """Triggers the start of the math application session."""
        self.language = chosen_language
        self.score = 0
        
        # Audio feature: Greet the child based on language
        if self.language == "English":
            self.speak("Welcome to Fun Math Kids!")
        else:
            self.speak("Welkom by Pret Wiskunde!")

        self.show_game_screen()
        self.ask_new_question()

    def show_game_screen(self):
        """Screen 2: The active arithmetic playing field."""
        self.clear_screen()

        # Score Tracker layout
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Comic Sans MS", 14, "bold"), bg="#E0F7FA")
        self.score_label.pack(anchor="ne", padx=20, pady=10)

        # Math Question Display
        self.math_label = tk.Label(self.root, text="", font=("Comic Sans MS", 36, "bold"), bg="#E0F7FA", fg="#01579B")
        self.math_label.pack(pady=15)

        # User Input text box
        self.input_box = tk.Entry(self.root, font=("Comic Sans MS", 24), justify="center", width=5)
        self.input_box.pack(pady=10)
        self.input_box.focus()
        
        # Shortcut: pressing 'Enter' on keyboard checks the answer directly!
        self.input_box.bind("<Return>", lambda event: self.check_answer())

        # Validation Action Button
        btn_text = "Check Answer! ✔️" if self.language == "English" else "Kontroleer! ✔️"
        self.check_button = tk.Button(self.root, text=btn_text, font=("Comic Sans MS", 16, "bold"), bg="#2196F3", fg="white",
                                      command=self.check_answer)
        self.check_button.pack(pady=10)

        # Visual Feedback Label (For the flashing animations)
        self.feedback_label = tk.Label(self.root, text="", font=("Comic Sans MS", 18, "bold"), bg="#E0F7FA")
        self.feedback_label.pack(pady=5)

        # Visual Feedback Image (Happy or Sad face placement)
        self.image_label = tk.Label(self.root, bg="#E0F7FA")
        self.image_label.pack(pady=5)

    def ask_new_question(self):
        """Resets fields and loads a new randomized problem."""
        self.input_box.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.image_label.config(image="")

        # Basic Addition Generator
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.correct_answer = self.num1 + self.num2

        self.math_label.config(text=f"{self.num1} + {self.num2} = ?")

        # Read math problem out loud
        if self.language == "English":
            self.speak(f"What is {self.num1} plus {self.num2}?")
        else:
            self.speak(f"Wat is {self.num1} plus {self.num2}?")

    def flash_feedback(self, execution_count, main_color, background_color):
        """Alternates text color back and forth to simulate flashing."""
        if execution_count > 0:
            current_color = self.feedback_label.cget("foreground")
            new_color = background_color if current_color == main_color else main_color
            self.feedback_label.config(fg=new_color)
            self.root.after(250, lambda: self.flash_feedback(execution_count - 1, main_color, background_color))

    def check_answer(self):
        """Verifies mathematical entry and provides reactive feedback."""
        kid_typing = self.input_box.get().strip()

        # Sanity check validation
        if not kid_typing.isdigit():
            error_msg = "Please type a number!" if self.language == "English" else "Voer 'n getal in!"
            messagebox.showwarning("Oops!", error_msg)
            return

        kid_answer = int(kid_typing)

        # IF THE ANSWER IS CORRECT
        if kid_answer == self.correct_answer:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            
            text_reply = "Awesome Job! 🎉" if self.language == "English" else "Mooi so! 🎉"
            self.feedback_label.config(text=text_reply, fg="#4CAF50")
            
            if self.happy_img:
                self.image_label.config(image=self.happy_img)
                
            self.flash_feedback(6, "#4CAF50", "#E0F7FA")
            self.speak("Correct!" if self.language == "English" else "Dit is reg!")

        # IF THE ANSWER IS INCORRECT
        else:
            text_reply = "Try Again! 🦊" if self.language == "English" else "Probeer weer! 🦊"
            self.feedback_label.config(text=text_reply, fg="#F44336")
            
            if self.sad_img:
                self.image_label.config(image=self.sad_img)
                
            self.flash_feedback(6, "#F44336", "#E0F7FA")
            self.speak("Wrong answer, try again!" if self.language == "English" else "Dit is verkeerd, probeer weer!")

        # Wait 2.5 seconds, then load the next problem
        self.root.after(2500, self.ask_new_question)

if __name__ == "__main__":
    window = tk.Tk()
    app = FunMathKidsApp(window)
    window.mainloop()