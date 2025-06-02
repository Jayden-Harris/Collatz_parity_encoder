import string
import argparse

def generate_collatz_parity(n: int) -> str:
    """Generate parity sequence from Collatz iteration of n."""
    parity = []
    while n != 1:
        parity.append('1' if n % 2 else '0')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return "".join(parity)

def generate_sequence(data):
    printable_chars = string.printable.replace("\n", "").replace("\r", "")  # keeps space
    char_map = {char: idx for idx, char in enumerate(printable_chars, start=2)}
    return [char_map[c] for c in data if c in char_map]


def reverse_sequence(nums):
    printable_chars = string.printable.replace("\n", "").replace("\r", "")  # keeps space
    char_map = {char: idx for idx, char in enumerate(printable_chars, start=2)}
    reversed_map = {idx: char for char, idx in char_map.items()}
    return [reversed_map[num] for num in nums if num in reversed_map]

def reverse_from_parity(parity_str: str, final: int = 1) -> int | None:
    """Reverse the Collatz parity sequence to recover original number."""
    n = final
    for bit in reversed(parity_str):
        if bit == '0':
            n = n * 2
        elif bit == '1':
            if (n - 1) % 3 != 0:
                return None
            prev = (n - 1) // 3
            if prev % 2 == 0:
                return None
            n = prev
        else:
            return None
    return n

def encode(plain_text):
    encoded = []
    sequence = generate_sequence(plain_text)
    
    parity_list = [generate_collatz_parity(s) for s in sequence]
  
    for parity in parity_list:
        encoded.append(parity + "11")
    
    return "".join(encoded)

def decode(parity_str):
    parity_arr = [p for p in parity_str.split("11") if p] 
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