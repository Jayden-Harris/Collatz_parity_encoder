import string

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

def find_unused_flag(parity_list, max_len=8):
    for length in range(1, max_len + 1):
        for i in range(2 ** length):
            candidate = format(i, f"0{length}b")
            if all(candidate not in p for p in parity_list):
                return candidate
    return None

def generate_sequence(data):
    alpha = string.ascii_lowercase
    alpha_map = {char: idx for idx, char in enumerate(alpha, start=1)}
    return [alpha_map[c] for c in data.lower() if c in alpha]

def encode(plain_text):
    encoded = []
    sequence = generate_sequence(plain_text)
    
    parity_list = [generate_collatz_parity(s) for s in sequence]
    
    # Find a unique binary flag not present in any parity string
    flag = find_unused_flag(parity_list)
    if not flag:
        raise ValueError("No unique flag found")
    
    # Append each parity + flag
    for parity in parity_list:
        encoded.append(parity + flag)
    
    return "".join(encoded)

def main():
    encoded = encode("Hello world")
    print(encoded)

if __name__ == "__main__":
    main()
