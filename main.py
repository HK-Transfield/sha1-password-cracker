# This entrypoint file to be used in development. Start by reading README.md
import password_cracker
import sys


def main():

    print("\n--------- SHA-1 Password Cracker ---------")

    # Wait for the user to enter a valid response
    while True:
        try:
            option = input(
                "\nWhat would you like to do? Enter [1/2/3]\n(1) salted hash\n(2) SHA-1 hash\n(3) quit\nEnter option: ")
            if option.strip() not in ('1', '2', '3'):
                print("\nERROR: " + option +
                      "is not a valid option. Please enter [1/2/3].")
            else:
                break
        except Exception as e:
            print(e)

    # cracking salted hashes
    if option.strip() == "1":
        salted_hash = input("\nEnter a salted hash: ")
        cracked_password2 = password_cracker.crack_sha1_hash(
            salted_hash.strip(), use_salts=True)
        print(cracked_password2)

    # cracking regular hashes
    elif option.strip() == "2":
        hash = input("\nEnter a SHA-1 hash: ")
        cracked_password1 = password_cracker.crack_sha1_hash(
            hash.strip())
        print(cracked_password1)

    # quit the program
    elif option.strip() == "3":
        print("OK, goodbye!")
        sys.exit()


if __name__ == "__main__":
    main()
