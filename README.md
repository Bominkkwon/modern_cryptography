# modern_cryptography
Encoding and decoding data types that are commonly used in cryptography.


## The History of Cryptography

Cryptography has been around for a long time, even in ancient civilizations. People needed secure ways to communicate during battles and politics, so they developed methods to hide their messages from enemies.

One of the earliest methods was the Caesar cipher. Julius Caesar, a Roman general, wanted to send secret messages to his military. He came up with a way to make his messages unreadable to others, which became known as the Caesar cipher.

In this method, a message is encrypted by shifting each letter a fixed number of positions down the alphabet. For example, with a shift of 1, the letter A becomes B, and with a shift of 2, A becomes C. This creates a ciphertext, which is an unreadable version of the original message.

To decrypt the message and make it readable again, the process is reversed. Each letter is shifted back by the same number of positions.

While the Caesar cipher provided confidentiality to Julius Caesar, it is no longer used for serious purposes today because it can be easily decrypted. Instead, more advanced encryption methods have been developed over time.



## Encoding

Encoding is different from encryption because its purpose is not to keep information secret, but rather to transform data so that it can be properly used by a different system.

The main goal of encoding is to convert data into a specific format that can be easily understood and processed by a particular system or device. For instance, text can be encoded into binary format to enable digital transmission of data.

Unlike encryption, encoding does not involve keeping information confidential or hidden. The encoding process uses a publicly available scheme that can be decoded by anyone who knows the scheme. It does not rely on a secret key or any form of encryption algorithm.


- [x] ASCII 


ASCII encoding is a method used to convert numbers to letters. It stands for American Standard Code for Information Interchange. In ASCII encoding, each letter of the English alphabet, along with punctuation marks, symbols, and numbers, is represented by a specific number between 0 and 255. For example, the number 84 represents the letter 'T', and the number 118 represents the letter 'v'. This conversion is often called decimal to ASCII encoding or decimal to text encoding.

You can find more conversions, such as hex and octal, on the [ASCII Table website](https://www.asciitable.com/).

- [x] Hex 

Hex encoding is a way to represent binary data using a shorter format. Binary numbers can be quite long and cumbersome to work with. Hexadecimal, or hex for short, is a numbering system that uses 16 symbols: the numbers 0 to 9 and the letters A to F.

For example:

- The hex value 52 represents the letter 'R'.

- The hex value 7A represents the letter 'z'.

- When we convert the word "hello" to hex, it becomes 68 65 6C 6C 6F.

- This conversion is called hex to ASCII encoding or hex to text encoding.

Additionally, there's another numbering system called octal, which is similar to hex but uses the digits 0 to 7. For instance: The octal value 042 represents the decimal number 34.
- [x] Base64 
- [x] Bytes and Big Integers 
- [x] Encoding Automation (Using the [pwntools library](https://docs.pwntools.com/en/stable/) (pwn)) --please note that the [Pwntools library](https://docs.pwntools.com/en/stable/install.html#installation) is best supported on 64-bit Ubuntu LTS releases (14.04, 16.04, 18.04, and 20.04). Most functionality should work on any Posix-like distribution (Debian, Arch, FreeBSD, OSX, etc.). **It's not compatible with Windows!**

    

**XOR**
- [x] XOR Starter 
- [ ] XOR Properties 
- [ ] Lemur XOR

**Mathematics**
- [x] Greatest Common Divisor - Euclidean Algorithm
<details>
  <summary>Pseudo Code of the Algorithm</summary>
    
``` 
Step 1:  Let  a, b  be the two numbers
Step 2:  a mod b = R
Step 3:  Let  a = b  and  b = R
Step 4:  Repeat Steps 2 and 3 until  a mod b  is greater than 0
Step 5:  GCD = b
Step 6: Finish
```
</details>

- [ ] Extended GCD 

