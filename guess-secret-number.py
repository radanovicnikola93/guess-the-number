import random

def main():
    secret = random.randint(1, 20)

    while True:
        guess = int(raw_input("Guess the secret number from 1 to 20: "))

        if guess == secret:
            print "Congratulations! Its number %s! :)" % secret
            break
        elif guess > secret:
            print "Try something lower."
        elif guess < secret:
            print "Try something higher."

if __name__ == "__main__":
    main()

