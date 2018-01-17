#/usr/bin/env python
# -*- coding: utf-8 -*-

secret = 8

guess = int(raw_input("Guess the secret number from 1 to 10: "))

if guess == secret:
    print "Congratulations!"

else:
    print "Please try again"