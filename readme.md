# Collatz Parity Encoder/Decoder

This Python tool implements a reversible encoder and decoder using Collatz parity sequences. It converts printable ASCII strings into a binary format based on the Collatz conjecture and can decode them back to the original text without requiring additional metadata.

---

## Features

- **Bidirectional Transformation** – Encode and decode any printable string.
- **Collatz-Based Encoding** – Character codes are transformed using parity sequences derived from the Collatz conjecture.
- **Metadata-Free Decoding** – Uses a unique `11` delimiter for sequences, eliminating the need for extra metadata.
- **Command-Line Interface** – Encode or decode directly from the terminal.

---

## Function Overview

- `encode(plain_text)` – Converts text into a binary parity string.  
- `decode(parity_str)` – Converts a binary parity string back into the original text.  
- `generate_collatz_parity(n)` – Produces the parity sequence (1 = odd, 0 = even) from a Collatz iteration.  
- `reverse_from_parity(parity_str)` – Reverses a parity string back into the original number.  
- `generate_sequence(data)` – Maps characters to unique indices.  
- `reverse_sequence(nums)` – Maps indices back to characters.

---

## Requirements

- Python 3.7 or later  
- No external libraries required

---

## Usage

### Command-Line

```bash
# Encode a string
python3 collatz_encoder.py encode "Hello, World! 123"

# Decode a parity string
python3 collatz_encoder.py decode "1010110111101011011010110111101110110111011111011011..."
```

## Notes
This tool is suitable for experiments in symbolic computation, reversible encoding, and virtual machine instruction sets. The Collatz parity method provides a deterministic, reversible approach to converting human-readable text into a compact binary representation.
