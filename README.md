# Modern Cryptography I
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

Base64 encoding is a method that converts binary data into a text format for secure transmission and storage. It uses a set of 64 characters to represent the data.

For example, if we have an image file in binary format, Base64 encoding would convert it into a series of text characters. This encoded version can be easily shared via email or embedded in web pages without any loss of information. When needed, the encoded data can be decoded back into the original image file.

Base64 encoding is widely used in applications, programming languages, and data transfer protocols for efficient handling of binary data in a readable and compatible format.

- [x] Bytes and Big Integers 

Bytes Encoding: Bytes encoding refers to the process of converting data into a sequence of bytes. It involves assigning a specific numeric value to each character or data element, allowing them to be represented as a series of binary digits (bits). Bytes encoding is commonly used for tasks like character encoding (e.g., ASCII or Unicode), data compression, and serialization of complex data structures.

Big Integers Encoding: Big integers encoding involves representing and encoding extremely large integers that cannot be accommodated by standard integer data types. Big integers are encoded by using algorithms and techniques that break down the number into smaller units or convert it to a different representation, such as a hexadecimal or base64 format. This encoding ensures that large numbers can be efficiently stored, transmitted, or processed.

Bytes and big integers encoding are crucial in various applications, including cryptography, secure communication protocols, numerical calculations, and data storage. These encoding methods enable the manipulation and transmission of data in a compact and efficient manner, while preserving the integrity and accuracy of the original information.


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



## Summary


Encoding is the process of transforming data to make it suitable for specific systems or applications, without the primary objective of confidentiality. It is commonly employed to convert digital text into binary format, facilitating storage, transmission, or processing. Various encoding schemes, such as ASCII, Base64, and hexadecimal, offer different approaches to represent and manipulate data. These encoding techniques find application in diverse fields, including telecommunications, programming, web development, and data storage. Online resources like Browserling and Rapid Tables provide accessible tools for encoding and decoding messages, enhancing convenience and efficiency in data manipulation. Understanding different encoding schemes and utilizing available resources contribute to successful data encoding and decoding processes.

