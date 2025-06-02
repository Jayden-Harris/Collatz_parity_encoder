# 🔐 Collatz Parity Encoder/Decoder

This Python script implements a **reversible encoder and decoder** using **Collatz parity sequences**. It converts printable ASCII strings into a binary format using the Collatz conjecture and can decode the binary back to the original text without needing explicit metadata.

---

## 📌 Features

- 🔁 **Bidirectional transformation**: Encode and decode any printable string.
- 🧬 **Based on Collatz Conjecture**: Transforms character codes via parity tracking.
- 🏷️ **Metadata-free decoding**: Uses a unique flag (`11`) to delimit sequences.
- 💡 **CLI support**: Easily encode or decode from the command line.

---

🛠 Function Overview

encode(plain_text):
Converts text into a binary string using Collatz parity sequences.

decode(parity_str):
Converts a binary parity string back into the original text.

generate_collatz_parity(n):
Produces the parity sequence (1 = odd, 0 = even) from a Collatz iteration.

reverse_from_parity(parity_str):
Attempts to reverse a parity string back into the original number.

generate_sequence(data):
Maps characters to unique indices.

reverse_sequence(nums):
Maps indices back to characters.

---

## 📦 Requirements

- Python 3.7 or later  
*(No external libraries required.)*

---

## 🚀 Usage

### 🔧 Command-Line

```bash
# Encode a string
python3 collatz_encoder.py encode "Hello, World! 123"

# Decode a parity string
python3 collatz_encoder.py decode "1010110111101011011010110111101110110111011111011011..."
