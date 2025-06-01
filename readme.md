# Collatz Encryption: Reversible Encryption Using the Collatz Conjecture Parity Sequences

![Collatz Encryption](https://img.shields.io/badge/Status-Experimental-blue)

## Overview

This project presents a novel reversible encryption algorithm based on the **Collatz conjecture** and its parity sequences. By encoding input data as sequences of parity bits generated from the Collatz process, and using a custom reverse procedure, the algorithm enables encryption and decryption without prior knowledge of the original number.

This approach explores the computational and theoretical properties of the Collatz conjecture applied to cryptography, offering a unique perspective on reversible sequence generation.

---

## Features

- Generate parity sequences from Collatz iterations of numeric inputs.
- Reverse parity sequences to recover original numeric data.
- Map textual data to numeric sequences and vice versa.
- Proof-of-concept encryption and decryption pipelines.
- Lightweight and implemented in Python for easy experimentation.

---

## How It Works

1. **Encoding**  
   Each character is mapped to an index number (0-25 for a-z).  
   The Collatz parity sequence is computed for each number, producing a string of '0's and '1's representing even and odd steps.

2. **Decoding**  
   The parity sequence is reversed step-by-step starting from 1, reconstructing the original number.  
   This enables the original text to be recovered from the parity data.

---

## Usage

Clone the repository and run the provided script:

```bash
git clone 
cd collatz_encryption
python3 collatz.py
