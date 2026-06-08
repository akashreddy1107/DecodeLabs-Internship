# Week 3: Secure Password Generator

## Description
This Python application generates a cryptographically secure random password based on the user's desired length. It ensures that the generated password meets industry-standard complexity requirements.

## Features
- **Cryptographic Security**: Uses Python's `secrets` module (instead of the standard `random` module) for cryptographically secure pseudo-random number generation (CSPRNG).
- **Complexity Guarantee**: Every generated password is guaranteed to contain at least:
  - 1 Uppercase letter
  - 1 Lowercase letter
  - 1 Digit
  - 1 Special/Punctuation character
- **Length Constraint**: Requires a minimum password length of 4 characters to satisfy the character type requirements.
- **Random Shuffling**: Shuffles the final list of characters using `secrets.SystemRandom().shuffle` to ensure the placement of guaranteed character types is entirely random and unpredictable.

## How to Run the Code
1. Open your terminal or command prompt.
2. Navigate to the folder containing `week3.py`.
3. Run the script using Python:
   ```bash
   python week3.py
   ```

## Output Screenshot
*(Add your output screenshot here!)*
<!-- Place your screenshot image in the repository and link it below -->
![Week 3 Output Screenshot](week3_output.png)
