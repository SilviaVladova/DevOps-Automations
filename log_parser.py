def find_errors(file_path):
    try:
        with open(file+path, 'r')  as file:
            for line in file:
                if "500 ERROR" in line:
                    print(f"Error found")

    except FileNotFoundError:
        print("File (file_path) not found")

if __name__ == "__main__":
    fine_error("app.log")
