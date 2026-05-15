import requests

def username_test(username):
    url = 'https://clients-site/password'
    payload = {"username": username}

    # 1. Local check first (no internet needed)
    if 5 <= len(username) <= 10 and username.isalpha():
        print("Valid username format")

        # 2. Server check (only if format is okay)
        try:
            response = requests.post(url, data=payload, timeout=5)
            if response.status_code == 200:
                print("Username accepted")
                return True
            else:
                print(f"Username not accepted (Status: {response.status_code})")
                return False
        except requests.exceptions.RequestException:
            print("Connection error")
            return False
    else:
        print("Invalid format (length or characters)")
        return False

username_test("silvia")
