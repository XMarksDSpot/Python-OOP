Python Object-Oriented Practice

This project contains Python classes to practice object-oriented programming concepts.

Project Files

-serial.py – A class to generate unique sequential serial numbers.

-wordfinder.py – A class to randomly select words from a dictionary file.

-words.txt – A sample word list used by WordFinder.


Installation and Setup

Requirements

Python 3.x installed on your system.

A text editor or an IDE (e.g., VS Code, PyCharm, Jupyter Notebook).

The words.txt file should be in the same directory as wordfinder.py.

Cloning the Repository

If using Git, clone the repository:

git clone https://github.com/your-repo/python-oo-practice.git
cd python-oo-practice

Or manually download and extract the files.

Usage

1. SerialGenerator

SerialGenerator generates unique, incrementing serial numbers.

Example Usage

Run the Python shell and import serial.py:

from serial import SerialGenerator

serial = SerialGenerator(start=100)

print(serial.generate())  # Output: 100
print(serial.generate())  # Output: 101

serial.reset()
print(serial.generate())  # Output: 100

2. WordFinder

WordFinder reads words from a text file and returns a random word.

Example Usage

Run the Python shell and import wordfinder.py:

from wordfinder import WordFinder

wf = WordFinder("words.txt")  # Reads words from the file
print(wf.random())  # Outputs a random word from words.txt

If words.txt contains:

apple
banana
cherry

Possible output:

banana

3. SpecialWordFinder

SpecialWordFinder is a subclass of WordFinder that ignores blank lines and lines starting with # (comments).

Example Usage

from wordfinder import SpecialWordFinder

swf = SpecialWordFinder("words.txt")
print(swf.random())  # Outputs a random word (excluding comments and blank lines)

If words.txt contains:

# Fruits
apple
banana

# Vegetables
carrot

Possible output:

banana

Troubleshooting

Common Errors

File Not Found Error

Ensure words.txt exists in the same directory as wordfinder.py.

If using a different file, provide the correct path:

wf = WordFinder("/path/to/your/words.txt")

Permission Denied

Check that you have read access to the file:

ls -l words.txt

If needed, change permissions:

chmod +r words.txt

Running Doctests

This project includes doctests to validate the functionality of the classes.
Run the tests using:

python3 -m doctest serial.py -v
python3 -m doctest wordfinder.py -v

Contributing

Fork this repository.

Create a new branch:

git checkout -b feature-branch

Commit your changes:

git commit -m "Added a new feature"

Push to GitHub:

git push origin feature-branch

Submit a Pull Request.
