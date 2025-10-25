common_words = {
    "the","and","is","in","of","to","for","on","that","it","with","as","was","at","by",
    "an","be","this","from","or","are","but","not","have","they","you","all","his","her",
    "she","he","we","my","me","so","if","no","what","there","when","which","who","your","one","about"
}

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

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def simple_score(text):
    words = [w.strip(".,!?;:()[]\"'").lower() for w in text.split()]
    return sum(1 for w in words if w in common_words)

def crack_caesar(ciphertext):
    best = (0, 0, "") 
    for shift in range(26):
        plain = caesar_decrypt(ciphertext, shift)
        score = simple_score(plain)
        if score > best[0]:
            best = (score, shift, plain)
    return best

if __name__ == "__main__":
    ciphertext = "khoor zruog" 
    score, shift, plaintext = crack_caesar(ciphertext)
    print(f"Best shift: {shift} (score={score})")
    print(f"Decrypted: {plaintext}")
