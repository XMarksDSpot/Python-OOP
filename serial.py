class SerialGenerator:
    """Machine to create unique incrementing serial numbers."""
    
    def __init__(self, start=0):
        """Initialize the serial generator with a start number."""
        self.start = start
        self.next = start
    
    def generate(self):
        """Return the next sequential number and increment the counter."""
        current = self.next
        self.next += 1
        return current
    
    def reset(self):
        """Reset the serial number back to the start value."""
        self.next = self.start
    
    def __repr__(self):
        """Provide a useful string representation of the instance."""
        return f"<SerialGenerator start={self.start} next={self.next}>"
