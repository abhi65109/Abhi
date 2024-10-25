### **Instagram Brute Force Tool**

This Python script performs a brute force attack to attempt to find the password for an Instagram account by trying 1 Billion password combinations. The script generates potential passwords based on user-defined parameters and tests them using Instagram's login endpoint.


> [!WARNING]
> This tool is for educational purposes only. Unauthorized access to any account without the owner’s permission is illegal and unethical. Please use this tool responsibly.


## **Features**
• Generate passwords based on customizable character sets and password lengths.

• Test passwords using Instagram’s login endpoint.

• Implements rate-limiting by introducing delays between requests to avoid detection or blocking by Instagram's servers.

## **Installation**
**Clone the repository:**
```
git clone https://github.com/username/instagram-brute-force.git
cd instagram-brute-force
```
## **Code Overview**

1. generate_passwords(length, chars): Generates all possible combinations of characters of a given length.
   
3. brute_force_instagram(username, passwords): Sends POST requests to Instagram's login API, checking if any of the passwords work.
   
4. main(): Prompts the user for input and coordinates password generation and testing.

## **Notes**

• Rate Limiting: The script introduces a 1-second delay between each password attempt to minimize the chances of being blocked by Instagram.

• Password Chunking: Passwords are tested in batches of 10,000 to manage large password sets effectively.

## **License**

This project is licensed under the **MIT License.**
