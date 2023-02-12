#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 2023

@author: iluzioDev

This script implements the RC4 stream cipher algorithm.
"""

""""""
# Constants
N_BYTES = 256
""""""

# Swap two elements in a list
def swap(x, i, j):
  aux = x[i]
  x[i] = x[j]
  x[j] = aux

# Converts a string to ASCII Code Integers
def text_to_ascii(text):
  return ''.join([str(ord(i)).zfill(3) for i in text])

# Converts ASCII Code Integers to a string
def ascii_to_text(ascii):
  ascii = str(ascii)
  if len(ascii) % 3 != 0:
    ascii = ascii.zfill(len(ascii) + (3 - (len(ascii) % 3)))
  return ''.join(chr(int(ascii[i - 2] + ascii[i - 1] + ascii[i])) for i in range(len(ascii) - 1, 0, -3))[::-1]

# Key Scheduling Algorithm (KSA)
def KSA(S, key):
  j = 0
  for i in range(N_BYTES):
    j = (j + S[i] + key[i % len(key)]) % N_BYTES
    swap(S, i, j)
  return

# Pseudo-Random Generation Algorithm (PRGA)
def PRGA(S, i, j):
  i = (i + 1) % N_BYTES
  j = (j + S[i]) % N_BYTES
  swap(S, i, j)
  return S[(S[i] + S[j]) % N_BYTES]

# Cipher text with RC4 algorithm
def cipher(S, text, key):
  i = 0
  j = 0
  key = [ord(c) for c in key]
  KSA(S, key)
  result = ''
  for c in text:
    result += chr(ord(c) ^ PRGA(S, i, j))
  return result

# Main Function
def main():
  while True:
    S = list(range(N_BYTES))
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■                  WELCOME TO THE RC4 CIPHER TOOL!                ■')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('What would you want to do?')
    print('[1] Cipher Message.')
    print('[2] Cipher with Ascii Code of Message.')
    print('[3] Convert Ascii Code to Text.')
    print('[4] Convert Text to Ascii Code.')
    print('[0] Exit.')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    option = input('Option  ->  ')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

    # If option is not valid, ask again
    if option not in ['0', '1', '2', '3', '4']:
      print('ERROR. Option Unknown!')
      continue

    # Exit if option is 0
    if option == '0':
      print('See you soon!')
      print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
      break

    # If option is 1, ask for text to encrypt
    # If option is 2, ask for ascii code to encrypt
    if option == '1':
      text = input('Introduce text to encrypt: ')
    if option == '2':
      ascii_code = input('Introduce ascii code: ')
      text = ascii_to_text(ascii_code)
    
    # Ask for key and cipher text
    if option in ['1', '2']:
      key = input('Introduce key: ')
      cipher_text = cipher(S, text, key)
      print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
      print('Cipher Text:', cipher_text)
      print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
      print('Ascii Code:', text_to_ascii(cipher_text))
    
    # If option is 3, ask for ascii code to convert to text
    if option == '3':
      ascii_code = input('Introduce ascii code: ')
      print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
      print('Output Text:', ascii_to_text(ascii_code))
      print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

    # If option is 4, ask for text to convert to ascii code
    if option == '4':
      text = input('Introduce text: ')
      print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
      print('Ascii Code Output:', text_to_ascii(text))
      print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

main()