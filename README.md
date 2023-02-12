# RC4 Cipher (ARC4/ARCFOUR)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Twitter](https://img.shields.io/twitter/follow/luctstt.svg?label=Follow&style=social)](https://twitter.com/iluzioDev)

## Introduction 📋

> RC4 was designed by Ron Rivest of RSA Security in 1987. While it is officially termed "Rivest Cipher 4", the RC acronym is alternatively understood to stand for "Ron's Code"

[RC4 - Crypto Wiki | Fandom](https://cryptography.fandom.com/wiki/RC4)

> It is a variable key-size stream cipher with byte-oriented operations. It uses either 64 bit or 128-bit key sizes. It is generally used in applications such as Secure Socket Layer (SSL), Transport Layer Security (TLS), and also used in IEEE 802.11 wireless LAN std.

[What is RC4 Encryption? - GeeksforGeeks](https://www.geeksforgeeks.org/what-is-rc4-encryption/)

<p float="left">
	<img src="https://upload.wikimedia.org/wikipedia/commons/7/79/Ronald_L_Rivest_photo.jpg" alt="Ronald Rivest" height="225px">
</p>

## Features ✨

* Encryption and Decryption of any text.
* Customized inputs.
* Ascii Code-Text Convertion.
* Support Keys of variable length.

## Install 🔧

```
git clone https://github.com/iluzioDev/RC4-cipher
cd RC4-cipher
python3 RC4-cipher.py
```

## Usage 💡

Once executed, a menu will prompt asking for desired option:

```
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
■                  WELCOME TO THE RC4 CIPHER TOOL!                ■
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
What would you want to do?
[1] Cipher Message.
[2] Cipher Ascii Code of Message.
[3] Convert Ascii Code to Text.
[4] Convert Text to Ascii Code.
[0] Exit.
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Option  ->
```

1. Encrypts/Decrypts a message after inserting a key. The program will generate a key stream to make a XOR operation with the message.
2. Similar to option 1, encrypts/decrypts a message giving its ascii code ```(no plain text!)```.
3. Converts a given ascii code to its corresponding string. It's important to notice that the ascii code of each character has 3 digits!
  ```
  ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  Introduce ascii code: 072101108108111
  ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  OUTPUT TEXT: Hello
  ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
   ```
4. Similar to option 4, converts a string to its corresponding ascii code

## Maintainers 👷

<table>
  <tr>
    <td align="center"><a href="https://github.com/iluzioDev"><img src="https://avatars.githubusercontent.com/u/45295283?v=4" width="100px;" alt="IluzioDev"/><br /><sub><b>IluzioDev</b></sub></a><br />💻</td>
  </tr>
</table>

## License ⚖️

Distributed under the MIT License. [Click here](LICENSE.md) for more information.

---
<div align="center">
	<b>
		<a href="https://www.npmjs.com/package/get-good-readme">File generated with get-good-readme module</a>
	</b>
</div>
