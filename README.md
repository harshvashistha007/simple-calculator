 🧮 Simple Calculator

A beginner-friendly Python script that performs basic arithmetic operations based on user input. Ideal for learning how to use conditional statements and input handling in Python.

## 📁 File

- `harsh.py` — The main script that runs the calculator.

## 🚀 How to Run

1. Clone the repository or download `harsh.py`.
2. Open a terminal and run:
   ```bash
   python harsh.py
   ```

3. Follow the prompts:
   - Enter the first number
   - Enter the second number
   - Choose an operation: `+`, `-`, `*`, `/`

## 🧑‍💻 Code Overview

```python
a = int(input("enter first"))
b = int(input("enter any second"))
choice = input("enter you choice +,-,*,/")

if choice == "+":
    print(a + b)
elif choice == "-":
    print(a - b)
elif choice == "/":
    print(a / b)
elif choice == "*":
    print(a * b)
else:
    print("invalid")
```

## ✅ Example

```
enter first: 10
enter any second: 5
enter you choice +,-,*,/: *
50
```

## 🛠️ Features

- Interactive command-line interface
- Supports addition, subtraction, multiplication, and division
- Simple structure for easy understanding

## 📌 Notes

- Make sure to enter valid integers.
- No error handling for division by zero — consider adding `try-except` blocks for robustness.

## 🌟 Future Improvements

- Add support for floating-point numbers
- Include error handling for invalid inputs
- Extend functionality to support more operations (e.g., modulus, exponentiation)

