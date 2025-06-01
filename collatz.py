import string
from collections import deque

def collatz(n: int) -> str:
    """Generate parity sequence from Collatz iteration of n."""
    parity = []
    while n != 1:
        parity.append('1' if n % 2 else '0')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return ''.join(parity)


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


def generate_sequence(data: str) -> list[int]:
    alpha = string.ascii_lowercase
    return [alpha.index(c) for c in data.lower() if c in alpha]


def consume_sequence(sequence: list[int]) -> str:
    alpha = string.ascii_lowercase
    return ''.join(alpha[s] for s in sequence if 0 <= s < len(alpha))


def encrypt(sequence: list[int]) -> tuple[list[int], list[str]]:
    encrypted_flags = []
    parity_list = []
    for num in sequence:
        par = collatz(num)
        encrypted_flags.append(1)  # Placeholder or marker
        parity_list.append(par)
    return encrypted_flags, parity_list


def decrypt(encrypted: list[int], parity: list[str]) -> str:
    sequence = []
    for flag, par in zip(encrypted, parity):
        n = reverse_from_parity(par, final=flag)
        if n is None:
            raise ValueError(f"Invalid parity sequence encountered: {par}")
        sequence.append(n)

    return consume_sequence(sequence)


def main():
    input_str = "hello world"
    sequence = generate_sequence(input_str)

    encrypted_string, parity = encrypt(sequence)
    print("Encrypted String: " + "".join(str(n) for n in encrypted_string))
    print("Parity sequence: " + "-".join(parity))

    print("---------------------------------------------------------")

    decrypted_string = decrypt(encrypted_string, parity)
    print("Decrypted String:", decrypted_string)


if __name__ == "__main__":
    main()
