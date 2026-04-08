# Personal-Project1_KidsApp# FunMath Kids SA

FunMath Kids SA is a beginner-friendly educational application designed to help young learners (Grades R–3) improve their basic mathematics skills in a fun and interactive way.

The application uses a colorful graphical interface, audio feedback, and simple game play to make learning engaging and accessible for children.

---

## Features

* English and Afrikaans language support
* Audio interaction (text-to-speech and recorded audio)
* Random math questions (addition)
* Kid-friendly GUI with clear colors and large text
* Visual feedback using images (happy/sad faces, stars)
* Simple animations (flashing feedback text)
* Score tracking system
* Continuous play (multiple questions)

---

## Problem It Solves

Many early-grade learners struggle with basic math concepts such as addition. Traditional learning methods can feel boring or difficult.

FunMath Kids SA addresses this by:

* Making learning interactive and engaging
* Using audio for learners who struggle with reading
* Providing instant feedback to reinforce learning

---

## Technologies Used

* Python
* Tkinter (GUI)
* pyttsx3 (Text-to-Speech)
* playsound (Audio playback)

---

## Project Structure

```
FunMathKidsSA/
│
├── main.py
├── audio/
│   ├── welkom.mp3
│   ├── reg.mp3
│   └── verkeerd.mp3
│
├── images/
│   ├── star.png
│   ├── happy.png
│   └── sad.png
```

---

## How to Run the Project

1. Install Python (version 3+)

2. Install required libraries:

```
pip install pyttsx3 playsound
```

3. Make sure the following folders exist:

* `audio/` (for Afrikaans voice files)
* `images/` (for visuals)

4. Run the program:

```
python main.py
```

---

## How to Use

1. Launch the app
2. Choose a language (English or Afrikaans)
3. Listen to the question
4. Enter your answer
5. Receive instant feedback
6. Continue playing and improving your score

---

## Future Improvements

* Multiple-choice buttons (no typing required)
* Difficulty levels (easy, medium, hard)
* Progress saving per learner
* More math operations (subtraction, multiplication)
* Background music and sound effects
* Mobile app version

---

## Author

Avela Tshaka

---
