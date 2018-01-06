# Password Strength Calculator

Script for checking your password's strength. Password will get '1' if it's in the blacklist.
If upper-case, lower-case letters, digits and symbols are used, password will get '10'

# How to use

Script requires Python 3.5 to be installed in system and txt file with list of 
worst passwords(e.g. from [here](https://www.symantec.com/connect/blogs/top-500-worst-passwords-all-time)). 

```commandline

C:\6_password_strength>python password_strength.py <input_file.txt>

Example:
C:\6_password_strength>python password_strength.py blacklist.txt
Please enter your password: P@$$w0Rd
Your password's strenght is 10

C:\6_password_strength>python password_strength.py blacklist.txt
Please enter your password: password
Your password in blacklist! Strenght = 1 Please try again

C:\6_password_strength>python password_strength.py blacklist.txt
Please enter your password: 54321
Your password's strenght is 2

```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
