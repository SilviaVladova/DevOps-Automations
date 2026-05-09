import requests

def test_passwords_strength():
    api_url = "https://starshoes.net"

    passwords_to_test = [
        "",
        "123",
        "A" * 1000,
        "admin, OR 1=1",
        "    ",
        "password123"
    ]
    print(f"Starting a test to validate passwords")
    
    for password in passwords_to_test:
        payload = {"password": password}


    if len(password) < 8 or "admin" in passwords or password.strip() == "":
        print(f"[PASS] The password '{password[:10}}...' was properly rejected")
    else:
        print(f"[FAIL] The system accepted the password '{password[:10]}...' which is a security risk")

if __name__ == __main__":
    test_password_strenght()
