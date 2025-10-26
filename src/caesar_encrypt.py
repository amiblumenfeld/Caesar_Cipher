def caesar_encrypt(text, shift):
    result = ""
    for c in text:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += c
    return result

if __name__ == "__main__":
    ciphertext = "khoor zruog" 
    score, shift, plaintext = crack_caesar(ciphertext)
    print(f"Best shift: {shift} (score={score})")
    print(f"Decrypted: {plaintext}")
