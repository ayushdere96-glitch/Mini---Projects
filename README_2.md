<div align="center">

# 🐍 Python Mini Projects Collection

### Five small command-line apps that teach real Python, one idea at a time.

![Python](https://img.shields.io/badge/Python-3.x-6366F1?style=for-the-badge&logo=python&logoColor=white)
![Projects](https://img.shields.io/badge/Projects-5-22D3EE?style=for-the-badge&labelColor=0F172A)
![Dependencies](https://img.shields.io/badge/Dependencies-None-34D399?style=for-the-badge&labelColor=0F172A)
![Level](https://img.shields.io/badge/Level-Beginner-FBBF24?style=for-the-badge&labelColor=0F172A)
![Stars](https://img.shields.io/badge/Enjoyed_it%3F-Leave_a_⭐-FB7185?style=for-the-badge&labelColor=0F172A)

**No installs. No setup. Just Python and one command.**

[🔐 Password Manager](#-1-password-manager) •
[🎓 Student Result Manager](#-2-student-result-manager) •
[💸 Bill Divider](#-3-bill-divider) •
[📅 Calendar](#-4-calendar) •
[🔢 OTP Generator](#-5-otp-generator)

<br>

> ⭐ **If these projects help you learn, a star on the repo means a lot and helps other beginners find it.**

</div>

---

## 📖 Table of Contents

- [🎨 Color Palette](#-color-palette)
- [📚 Quick Overview](#-quick-overview)
- [⚡ Quick Start](#-quick-start)
- [🔐 1. Password Manager](#-1-password-manager)
- [🎓 2. Student Result Manager](#-2-student-result-manager)
- [💸 3. Bill Divider](#-3-bill-divider)
- [📅 4. Calendar](#-4-calendar)
- [🔢 5. OTP Generator](#-5-otp-generator)
- [🧭 Skills Practiced](#-skills-practiced)
- [🚀 What to Learn Next](#-what-to-learn-next)
- [🤝 Contributing](#-contributing)
- [⭐ Support the Project](#-support-the-project)

---

## 🎨 Color Palette

The **Midnight Neon** palette is used for every badge and highlight in this README.

| Swatch | Name | Hex | Used For |
|:---:|:---|:---|:---|
| ![](https://placehold.co/60x30/0F172A/0F172A.png) | Midnight | `#0F172A` | Dark badge backgrounds |
| ![](https://placehold.co/60x30/6366F1/6366F1.png) | Indigo | `#6366F1` | Python and main brand |
| ![](https://placehold.co/60x30/22D3EE/22D3EE.png) | Cyan | `#22D3EE` | Counts and info |
| ![](https://placehold.co/60x30/34D399/34D399.png) | Mint | `#34D399` | Beginner-friendly and success |
| ![](https://placehold.co/60x30/FBBF24/FBBF24.png) | Amber | `#FBBF24` | Level and tips |
| ![](https://placehold.co/60x30/FB7185/FB7185.png) | Rose | `#FB7185` | Warnings and the star call-to-action |

---

## 📚 Quick Overview

| # | Project | What it does | Difficulty | Main Concepts | File |
|:-:|:---|:---|:---:|:---|:---|
| 1 | 🔐 Password Manager | Saves, shows and generates passwords | ⭐⭐⭐ | Dictionary, loops, conditionals, `random`, file handling | `Password_Manager.py` |
| 2 | 🎓 Student Result Manager | Stores marks and checks pass or fail | ⭐⭐ | Loops, dictionaries | `student_Result_Manager.py` |
| 3 | 💸 Bill Divider | Splits a bill with tip between friends | ⭐ | Input, math, f-strings | `Bill_Divider.py` |
| 4 | 📅 Calendar | Prints any month's calendar | ⭐ | `calendar` module | `Calender.py` |
| 5 | 🔢 OTP Generator | Creates a random one-time code | ⭐ | `random` module | `OTP_Generator.py` |

---

## ⚡ Quick Start

```bash
# 1. Check that Python 3 is installed
python --version

# 2. Download the project
git clone <your-repository-url>
cd <your-repository-folder>

# 3. Run any project
python Password_Manager.py
python student_Result_Manager.py
python Bill_Divider.py
python Calender.py
python OTP_Generator.py
```

> 💡 **Tip:** On Mac or Linux, use `python3` instead of `python`.

> 📸 **Demo slot:** Add a screenshot or GIF of a project running here, for example `assets/demo.gif`. A visual demo helps visitors understand the project in seconds.

---

# 🔐 1. Password Manager

![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-6366F1?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-File_Handling-22D3EE?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-random-34D399?style=flat-square)

A menu-driven app that **saves, shows and generates passwords** for different websites, with the data kept in a text file (`Password.txt`).

<details>
<summary><b>🧒 Simple Explanation (click to open)</b></summary>

<br>

Think of a **small notebook** 📒.

- You write the website name and its password.
- Later you open the notebook and read what you wrote.
- If you can't think of a good password, the app makes one for you 🎲.

</details>

<details>
<summary><b>📖 Detailed Explanation (click to open)</b></summary>

<br>

1. **Load old data:** At start, the program opens `Password.txt` and reads it line by line into the dictionary `passwords` (`website → password`). A `try/except` stops the app from crashing if the file doesn't exist yet.
2. **Generate a password:** `generate_passwords()` joins letters, digits and the symbols `!@#$%&`, then picks **8 random characters** with `random.choice`.
3. **Main menu:** A `while True` loop keeps showing the menu until the user exits.
4. **Menu choices:**
   - `1` asks for a website and password, stores them in the dictionary and **appends** them to the file.
   - `2` prints every saved website and password, or "No Data" if empty.
   - `3` shows a freshly generated password.
   - `4` says goodbye and leaves the loop with `break`.
   - Anything else prints "In Valid Input".

</details>

### 🧠 Concepts Used

| Concept | Where it is used |
|:---|:---|
| 📘 Dictionary | `passwords = {}` stores site → password |
| 🔁 Loops | `while True` menu, `for` loops to read and print |
| 🔀 Conditionals | `if / elif / else` for menu choices |
| 🎲 `random` module | Picks random characters for passwords |
| 📁 File handling | `open()` in `'r'` and `'a'` modes |

### 🖥️ Sample Output

```text
-----Personal Password Manager-----
1. Save Password
2. View Password 
3. Generate Password
4. Exit
Eneter Your Choice : 3
Generate Password :  aB3$kP9z
```

*(The generated password is random, so yours will differ.)*

### ⚠️ Known Issues and Upgrade Ideas

- 🐞 **Save and load formats don't match.** The app saves `site:pwd` but loads by splitting on `' : '` (with spaces). After a restart, the loader fails on the first line, and the bare `except: pass` hides the error, so **no saved passwords load**. Use the same separator in both places.
- 🔒 Passwords are stored as **plain text**. Encrypt them for real use (for example with the `cryptography` library).
- 🎲 Use the `secrets` module instead of `random` for security-grade passwords, and make them longer than 8 characters.
- 🧹 Saving the same website twice adds a duplicate line in the file.

---

# 🎓 2. Student Result Manager

![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-34D399?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-Dictionaries-FBBF24?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-Loops-FB7185?style=flat-square)

A simple app to **add students with their marks** and check whether each one **passes or fails**.

<details>
<summary><b>🧒 Simple Explanation (click to open)</b></summary>

<br>

Imagine a **teacher's register** 📋.

- Write each student's name and marks.
- Later, ask "Did Riya pass?"
- The app says **PASS** if the marks are 40 or more, otherwise **FAIL**.

</details>

<details>
<summary><b>📖 Detailed Explanation (click to open)</b></summary>

<br>

1. A dictionary `student = {}` holds `name → marks`.
2. A `while True` loop shows the menu again and again.
3. **Menu choices:**
   - `1` takes a name and marks (converted with `int()`) and saves them.
   - `2` loops through the dictionary and prints every student and their marks.
   - `3` looks up a name. If found, `marks >= 40` prints **PASS**, otherwise **FAIL**. If not found, it prints "Student Not Found!".
   - `4` exits the program.
4. The **pass mark is 40**.

</details>

### 🧠 Concepts Used

| Concept | Where it is used |
|:---|:---|
| 📘 Dictionary | Stores student names and marks |
| 🔁 Loops | Menu loop and the `.items()` loop |
| 🔀 Conditionals | Pass or fail check, menu choices |

### 🖥️ Sample Output

```text
-----Student Manager App-----
1. Add Student
2. View Student 
3. Check Result
4. Exit
Enter Your Choice : 1
Eneter Student Name : Riya
Enetr Marks : 72
Riya Succesfully Added!

Enter Your Choice : 3
Enter The Name : Riya
PASS
```

### ⚠️ Known Issues and Upgrade Ideas

- 🐞 Typing letters instead of a number for marks crashes the app (`ValueError`). Wrap the input in `try/except`.
- 💾 All data is lost when the program closes. Save it to a file or CSV.
- ✅ Marks like `-5` or `500` are accepted. Add a 0–100 check.
- 📊 Add grades (A, B, C) or a class average.

---

# 💸 3. Bill Divider

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-34D399?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-f--strings-6366F1?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-Math-22D3EE?style=flat-square)

Calculates the **total bill with tip** and shows **how much each person pays**.

<details>
<summary><b>🧒 Simple Explanation (click to open)</b></summary>

<br>

You and your friends ate at a restaurant 🍕. The app answers one question:

> "We all pay equally, tip included. How much do I give?"

</details>

<details>
<summary><b>📖 Detailed Explanation (click to open)</b></summary>

<br>

1. Takes three inputs: **bill amount**, **number of people** and **tip percentage**.
2. Uses these formulas:
   - `tip_amount = Bill × tip / 100`
   - `Total = Bill + tip_amount`
   - `share = Total / People`
3. Prints results with `:.2f`, so money always shows **two decimal places**.

</details>

### 🧮 Example Calculation

| Input | Value |
|:---|:---:|
| Bill | 1200 |
| People | 4 |
| Tip | 5% |

`Tip = 60` → `Total = 1260` → `Each = 315.00`

### 🖥️ Sample Output

```text
Enter Bill Amount :1200
Number Of People :4
Tip Percentage :5

 BILL SUMMARY
Toatl : 1260.00
Each Person Pays : 315.00
```

### ⚠️ Known Issues and Upgrade Ideas

- 🐞 Entering `0` people causes a division-by-zero error.
- ✏️ The output label has a typo: `Toatl` should be `Total`.
- 🌟 Add a currency symbol (₹) or a loop to handle more than one bill.

---

# 📅 4. Calendar

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-34D399?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-calendar_module-FBBF24?style=flat-square)

Prints the **calendar of any month and year** in the terminal.

<details>
<summary><b>🧒 Simple Explanation (click to open)</b></summary>

<br>

It is a **paper calendar on your screen** 🗓️. Tell it the year and month, and it shows all the dates neatly.

</details>

<details>
<summary><b>📖 Detailed Explanation (click to open)</b></summary>

<br>

1. Imports Python's built-in `calendar` module (nothing to install).
2. Asks for a **year** and a **month number** (1–12).
3. `calendar.month(year, Month)` returns the formatted calendar as text, and `print` shows it.

</details>

### 🖥️ Sample Output

```text
Enter Year :2026
Enter Month :10

     October 2026
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
```

### ⚠️ Known Issues and Upgrade Ideas

- 🐞 A month outside 1–12 causes an error. Add a validation check.
- 🌟 Try `calendar.year(2026)` for a full-year view, or `calendar.setfirstweekday(6)` to start weeks on Sunday.

---

# 🔢 5. OTP Generator

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-34D399?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-random-FB7185?style=flat-square)

Generates a **random One-Time Password (OTP)**, like the codes banks and apps send you.

<details>
<summary><b>🧒 Simple Explanation (click to open)</b></summary>

<br>

When you log in to an app, it sends a **secret number** 📱 that works only once. This program creates a number like that.

</details>

<details>
<summary><b>📖 Detailed Explanation (click to open)</b></summary>

<br>

1. Imports the `random` module.
2. `random.randint(10000, 999999)` picks a whole number between those two values.
3. Prints a "Generating OTP....." message and then the OTP.

</details>

### 🖥️ Sample Output

```text
 OTP GENERATOR 

Generating OTP.....
Your OTP : 482913
```

*(The number is random, so yours will differ.)*

### ⚠️ Known Issues and Upgrade Ideas

- 🐞 The range `10000–999999` gives a **5-digit OTP about 9% of the time** and a 6-digit OTP otherwise. For always 6 digits, use `random.randint(100000, 999999)`.
- 🔒 Use the `secrets` module for real security.
- ⏱️ Add an expiry timer, or ask the user to type the OTP back to verify it.

---

## 🧭 Skills Practiced

| Skill | P1 | P2 | P3 | P4 | P5 |
|:---|:-:|:-:|:-:|:-:|:-:|
| Variables and input | ✅ | ✅ | ✅ | ✅ | ✅ |
| Loops | ✅ | ✅ | | | |
| Conditionals | ✅ | ✅ | | | |
| Dictionaries | ✅ | ✅ | | | |
| Modules | ✅ | | | ✅ | ✅ |
| File handling | ✅ | | | | |
| f-string formatting | ✅ | ✅ | ✅ | | ✅ |

---

## 🚀 What to Learn Next

1. 🛡️ **Error handling** with `try / except`
2. 🧩 **Functions** to split big programs into small parts
3. 💾 **CSV and JSON** files for saving data
4. 🖼️ **A GUI** with `tkinter`
5. 🌐 **A web version** with Flask or Streamlit

---

## 🤝 Contributing

Found a bug or have an idea? You are welcome to help.

1. Fork the repository
2. Create a branch for your change
3. Open a pull request with a short description

The "Known Issues" lists above are good places to start.

---

## ⭐ Support the Project

If this collection helped you learn or gave you ideas, please consider giving it a **star**. It takes a second and helps other beginners discover it.

<div align="center">

![Footer](https://img.shields.io/badge/Keep-Coding-6366F1?style=for-the-badge&labelColor=0F172A)
![Footer](https://img.shields.io/badge/Keep-Learning-22D3EE?style=for-the-badge&labelColor=0F172A)
![Footer](https://img.shields.io/badge/Keep-Building-34D399?style=for-the-badge&labelColor=0F172A)

**Made with ❤️ by Ayush**

</div>
