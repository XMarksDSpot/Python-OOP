import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    
    def __init__(self, path):
        """Read words from a file and store them in a list."""
        self.words = self.read_words(path)
        print(f"{len(self.words)} words read")
    
    def read_words(self, path):
        """Read words from file, stripping newlines and ignoring blank lines."""
        with open(path, "r") as file:
            return [word.strip() for word in file if word.strip()]
    
    def random(self):
        """Return a random word from the list."""
        return random.choice(self.words)
    
    def __repr__(self):
        """Provide a useful string representation of the instance."""
        return f"<WordFinder words_count={len(self.words)}>"
    
class SpecialWordFinder(WordFinder):
    """Special Word Finder: ignores blank lines and comment lines."""
    
    def read_words(self, path):
        """Read words from file, ignoring blank lines and comment lines."""
        with open(path, "r") as file:
            return [word.strip() for word in file if word.strip() and not word.startswith("#")]