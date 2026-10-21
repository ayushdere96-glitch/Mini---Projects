<div align="center">

# 🐍 Python Mini Projects Collection

### *5 beginner-friendly projects • Real-world ideas • Simple code*

![Python](https://img.shields.io/badge/Python-3.x-6366F1?style=for-the-badge&logo=python&logoColor=white)
![Projects](https://img.shields.io/badge/Projects-5-22D3EE?style=for-the-badge&labelColor=0F172A)
![Level](https://img.shields.io/badge/Level-Beginner-34D399?style=for-the-badge&labelColor=0F172A)
![Type](https://img.shields.io/badge/Type-CLI_Apps-FBBF24?style=for-the-badge&labelColor=0F172A)
![Made With Love](https://img.shields.io/badge/Made_with-❤️-FB7185?style=for-the-badge&labelColor=0F172A)

<br>

**Click any project below to jump straight to it 👇**

[🔐 Password Manager](#-1-password-manager) •
[🎓 Student Result Manager](#-2-student-result-manager) •
[💸 Bill Divider](#-3-bill-divider) •
[📅 Calendar](#-4-calendar) •
[🔢 OTP Generator](#-5-otp-generator)

</div>

---

## 🎨 Color Palette

This README uses a modern **"Midnight Neon"** palette. Every badge and highlight follows it.

| Swatch | Name | Hex | Used For |
|:---:|:---|:---|:---|
| ![](https://placehold.co/60x30/0F172A/0F172A.png) | Midnight | `#0F172A` | Dark backgrounds |
| ![](https://placehold.co/60x30/6366F1/6366F1.png) | Indigo | `#6366F1` | Main brand / Python |
| ![](https://placehold.co/60x30/22D3EE/22D3EE.png) | Cyan | `#22D3EE` | Info / counts |
| ![](https://placehold.co/60x30/34D399/34D399.png) | Mint | `#34D399` | Success / beginner |
| ![](https://placehold.co/60x30/FBBF24/FBBF24.png) | Amber | `#FBBF24` | Tips / highlights |
| ![](https://placehold.co/60x30/FB7185/FB7185.png) | Rose | `#FB7185` | Warnings / love |

---

## 📚 Quick Overview

| # | Project | Difficulty | Main Concepts | File |
|:-:|:---|:---:|:---|:---|
| 1 | 🔐 Password Manager | ⭐⭐⭐ | Dictionary, Loops, Conditionals, `random`, File Handling | `Password_Manager.py` |
| 2 | 🎓 Student Result Manager | ⭐⭐ | Loops, Dictionaries | `student_Result_Manager.py` |
| 3 | 💸 Bill Divider | ⭐ | Input, Math, f-strings | `Bill_Divider.py` |
| 4 | 📅 Calendar | ⭐ | `calendar` module | `Calender.py` |
| 5 | 🔢 OTP Generator | ⭐ | `random` module | `OTP_Generator.py` |

---

## 🛠️ How to Run Any Project

```bash
# 1. Make sure Python is installed
python --version

# 2. Run any file
python Password_Manager.py
python student_Result_Manager.py
python Bill_Divider.py
python Calender.py
python OTP_Generator.py
```

> 💡 **Tip:** Use `python3` instead of `python` on Mac/Linux.

---

# 🔐 1. Password Manager

![Level](https://img.shields.io/badge/Difficulty-Intermediate-6366F1?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-File_Handling-22D3EE?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-random-34D399?style=flat-square)

A menu-driven app that **saves, shows and generates passwords** for different websites. Saved data stays in a text file (`Password.txt`), so it is still there the next time you open the app.

<details>
<summary><b>🧒 Simple Explanation (click to open)</b></summary>

<br>

Think of it as a **small notebook** 📒.

- You write down the website name and its password.
- Whenever you want, you open the notebook and read it.
- If you can't think of a strong password, the app makes one for you 🎲.

</details>

<details>
<summary><b>📖 Detailed Explanation (click to open)</b></summary>

<br>

1. **Loading old data:** On start, the program opens `Password.txt` and reads it line by line into a dictionary called `passwords` (`website → password`). The `try/except` makes sure the app does not crash if the file doesn't exist yet.
2. **Generating passwords:** `generate_passwords()` joins letters, digits and symbols (`!@#$%&`) and picks **8 random characters** with `random.choice`.
3. **Main menu:** A `while True` loop keeps showing the menu until the user chooses Exit.
4. **Menu options:**
   - `1` → Ask for website and password, store in the dictionary and **append** to the file.
   - `2` → Print every saved website and password (or "No Data").
   - `3` → Show a freshly generated password.
   - `4` → Say goodbye and `break` out of the loop.
   - Anything else → "In Valid Input".

</details>

### 🧠 Concepts Used

| Concept | Where it is used |
|:---|:---|
| 📘 Dictionary | `passwords = {}` stores site → password |
| 🔁 Loops | `while True` menu, `for` loop to read/print data |
| 🔀 Conditionals | `if / elif / else` for menu choices |
| 🎲 `random` module | Picks random characters for passwords |
| 📁 File Handling | `open()` in `'r'` and `'a'` modes |

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

### ⚠️ Known Issues & Upgrade Ideas

> These are great things to fix next. They make a nice learning step!

- 🐞 **File format mismatch:** data is *saved* as `site:pwd`, but *loaded* by splitting on `' : '` (with spaces). Saved passwords will not load correctly after a restart. Use the same separator in both places.
- 🔒 Passwords are stored as **plain text**. For real use, encrypt them (e.g., the `cryptography` library).
- 🔑 8 characters is short. Try 12–16.
- 🎲 Use the `secrets` module instead of `random` for security-grade randomness.

---

# 🎓 2. Student Result Manager

![Level](https://img.shields.io/badge/Difficulty-Beginner-34D399?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-Dictionaries-FBBF24?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-Loops-FB7185?style=flat-square)

A simple app to **add students with marks** and check whether each one **passes or fails**.

<details>
<summary><b>🧒 Simple Explanation (click to open)</b></summary>

<br>

Imagine a **teacher's register** 📋.

- Write each student's name and marks.
- Later, ask "Did Rahul pass?"
- The app says **PASS** if marks are 40 or more, otherwise **FAIL**.

</details>

<details>
<summary><b>📖 Detailed Explanation (click to open)</b></summary>

<br>

1. A dictionary `student = {}` holds `name → marks`.
2. A `while True` loop shows the menu repeatedly.
3. **Options:**
   - `1` → Takes a name and marks (converted with `int()`), saves them in the dictionary.
   - `2` → Loops through the dictionary and prints every student and their marks.
   - `3` → Looks up a name. If found, `marks >= 40` gives **PASS**, otherwise **FAIL**. If not found, prints "Student Not Found!".
   - `4` → Exits the program.
4. The **pass mark is 40**.

</details>

### 🧠 Concepts Used

| Concept | Where it is used |
|:---|:---|
| 📘 Dictionary | Stores student names and marks |
| 🔁 Loops | Menu loop and `.items()` loop |
| 🔀 Conditionals | Pass/Fail check, menu choices |

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

### ⚠️ Known Issues & Upgrade Ideas

- 🐞 Typing letters instead of a number for marks crashes the app (`ValueError`). Wrap the input in `try/except`.
- 💾 Data disappears when the program closes. Save it to a file or CSV.
- 📊 Add grades (A, B, C) or a class average.

---

# 💸 3. Bill Divider

![Level](https://img.shields.io/badge/Difficulty-Easy-34D399?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-f--strings-6366F1?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-Math-22D3EE?style=flat-square)

Calculates the **total bill with tip** and tells you **how much each person pays**.

<details>
<summary><b>🧒 Simple Explanation (click to open)</b></summary>

<br>

You and your friends ate at a restaurant 🍕. The app answers one question:

> "Everyone pays equally, including the tip. How much do I give?"

</details>

<details>
<summary><b>📖 Detailed Explanation (click to open)</b></summary>

<br>

1. Takes three inputs: **bill amount**, **number of people**, **tip percentage**.
2. Formulas:
   - `tip_amount = Bill × tip / 100`
   - `Total = Bill + tip_amount`
   - `share = Total / People`
3. Prints the results with `:.2f` so money shows **two decimal places**.

</details>

### 🧮 Example Calculation

| Input | Value |
|:---|:---:|
| Bill | 1000 |
| People | 4 |
| Tip | 10% |

`Tip = 100` → `Total = 1100` → `Each = 275.00`

### 🖥️ Sample Output

```text
Enter Bill Amount :1000
Number Of People :4
Tip Percentage :10

 BILL SUMMARY
Toatl : 1100.00
Each Person Pays : 275.00
```

### ⚠️ Known Issues & Upgrade Ideas

- 🐞 Entering `0` people causes a division-by-zero error.
- ✏️ Small typo in the output: `Toatl` should be `Total`.
- 🌟 Add a currency symbol (₹) or a loop to calculate more than one bill.

---

# 📅 4. Calendar

![Level](https://img.shields.io/badge/Difficulty-Easy-34D399?style=flat-square)
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

1. Imports Python's built-in `calendar` module (no installation needed).
2. Asks the user for a **year** and a **month number** (1–12).
3. `calendar.month(year, Month)` returns the formatted calendar as text, and `print` displays it.

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

### ⚠️ Known Issues & Upgrade Ideas

- 🐞 A month outside 1–12 causes an error. Add a validation check.
- 🌟 Try `calendar.year(2026)` to show the whole year, or `calendar.setfirstweekday(6)` to start weeks on Sunday.

---

# 🔢 5. OTP Generator

![Level](https://img.shields.io/badge/Difficulty-Easy-34D399?style=flat-square)
![Concept](https://img.shields.io/badge/Uses-random-FB7185?style=flat-square)

Generates a **random One-Time Password (OTP)** just like the codes you get from banks and apps.

<details>
<summary><b>🧒 Simple Explanation (click to open)</b></summary>

<br>

When you log in to an app, it sends a **secret number** 📱 that works only once. This program creates such a number.

</details>

<details>
<summary><b>📖 Detailed Explanation (click to open)</b></summary>

<br>

1. Imports the `random` module.
2. `random.randint(10000, 999999)` picks a whole number in that range.
3. Prints the OTP with a "Generating OTP....." message.

</details>

### 🖥️ Sample Output

```text
 OTP GENERATOR 

Generating OTP.....
Your OTP : 482913
```

### ⚠️ Known Issues & Upgrade Ideas

- 🐞 The range `10000–999999` can give a **5-digit or 6-digit** OTP. For always-6-digit, use `random.randint(100000, 999999)`.
- 🔒 Use the `secrets` module for real security.
- ⏱️ Add an expiry timer or ask the user to enter the OTP to verify it.

---

## 🧭 Skills You Practised

| Skill | P1 | P2 | P3 | P4 | P5 |
|:---|:-:|:-:|:-:|:-:|:-:|
| Variables & Input | ✅ | ✅ | ✅ | ✅ | ✅ |
| Loops | ✅ | ✅ | | | |
| Conditionals | ✅ | ✅ | | | |
| Dictionaries | ✅ | ✅ | | | |
| Modules | ✅ | | | ✅ | ✅ |
| File Handling | ✅ | | | | |
| f-string formatting | ✅ | ✅ | ✅ | | ✅ |

---

## 🚀 What to Learn Next

1. 🛡️ **Error handling** with `try / except`
2. 🧩 **Functions** to split big programs into small parts
3. 💾 **CSV / JSON** files for saving data
4. 🖼️ **GUI** with `tkinter`
5. 🌐 **Web version** with Flask or Streamlit

---

<div align="center">

### ⭐ If you like this repo, give it a star!

![Footer](https://img.shields.io/badge/Keep-Coding-6366F1?style=for-the-badge&labelColor=0F172A)
![Footer](https://img.shields.io/badge/Keep-Learning-22D3EE?style=for-the-badge&labelColor=0F172A)
![Footer](https://img.shields.io/badge/Keep-Building-34D399?style=for-the-badge&labelColor=0F172A)

**Made with ❤️ by Ayush**

</div>
