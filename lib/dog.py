#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Rover", breed="Mastiff"):
        self._name = name
        self._breed = breed

    def get_name(self):
        return self._name

    def set_name(self, name):
        if ((name) is (str)) and (1 <= len(name) <= 25):
            self._name = name
        elif ((name) is not (str)) or (len(name) > 25): 
            print("Name must be a string between 1 and 25 characters.")
        elif ((name) is not (str)) or (len(name) < 1):
            print("Name must be a string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in the list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
