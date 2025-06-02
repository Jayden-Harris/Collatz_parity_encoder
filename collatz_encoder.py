import string
import argparse

def generate_collatz_parity(n: int) -> str:
    """
    Generate the Collatz parity sequence for a given integer n.
    The parity sequence is a string of '0' and '1' representing
    whether each step is even (0) or odd (1) in the Collatz iteration,
    excluding the final 1.
    """
    parity = []
    while n != 1:
        parity.append("1" if n % 2 else "0")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return "".join(parity)

def generate_sequence(data: str) -> list[int]:
    """
    Convert a string into a list of integer codes corresponding
    to printable ASCII characters, starting index at 2.
    Ignores newline and carriage return characters.
    """
    printable_chars = string.printable.replace("\n", "").replace("\r", "")
    char_map = {char: idx for idx, char in enumerate(printable_chars, start=2)}
    return [char_map[c] for c in data if c in char_map]

def reverse_sequence(nums: list[int]) -> list[str]:
    """
    Convert a list of integer codes back to their corresponding
    printable ASCII characters.
    """
    printable_chars = string.printable.replace("\n", "").replace("\r", "")
    char_map = {char: idx for idx, char in enumerate(printable_chars, start=2)}
    reversed_map = {idx: char for char, idx in char_map.items()}
    return [reversed_map[num] for num in nums if num in reversed_map]

def reverse_from_parity(parity_str: str, final: int = 1) -> int | None:
    """
    Reverse a Collatz parity sequence back to the original integer.
    The sequence is read in reverse order.
    Returns None if the sequence is invalid.
    """
    n = final
    for bit in reversed(parity_str):
        if bit == "0":
            # If the bit is 0, the previous number was n * 2 (even step)
            n = n * 2
        elif bit == "1":
            # If the bit is 1, the previous number was (n - 1) / 3 (odd step)
            if (n - 1) % 3 != 0:
                return None
            prev = (n - 1) // 3
            # Previous number must be odd for this step to be valid
            if prev % 2 == 0:
                return None
            n = prev
        else:
            # Invalid bit character
            return None
    return n

def encode(plain_text: str) -> str:
    """
    Encode a plaintext string into a concatenated Collatz parity code string.
    Each character's code is followed by "11" as a delimiter.
    """
    sequence = generate_sequence(plain_text)
    parity_list = [generate_collatz_parity(num) for num in sequence]
    # Append "11" delimiter after each parity code
    encoded = [parity + "11" for parity in parity_list]
    return "".join(encoded)

def decode(parity_str: str) -> str:
    """
    Decode a concatenated parity code string back into plaintext.
    Splits the input on "11" delimiters to get each parity code,
    then reverses them to original numbers and maps back to characters.
    """
    parity_arr = [p for p in parity_str.split("11") if p]  # Ignore empty splits
    sequence = []
    for p in parity_arr:
        n = reverse_from_parity(p)
        if n is None:
            raise ValueError(f"Invalid parity sequence: {p}")
        sequence.append(n)
    char_array = reverse_sequence(sequence)
    return "".join(char_array)

def main():
    parser = argparse.ArgumentParser(description="Collatz-based parity encoder/decoder")
    parser.add_argument("mode", choices=["encode", "decode"], help="Choose to encode or decode")
    parser.add_argument("data", help="The string to encode or decode")
    args = parser.parse_args()

    if args.mode == "encode":
        result = encode(args.data)
        print(result)
    elif args.mode == "decode":
        try:
            result = decode(args.data)
            print(result)
        except ValueError as e:
            print(f"Decoding error: {e}")

if __name__ == "__main__":
    main()
