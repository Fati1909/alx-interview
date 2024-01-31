#!/usr/bin/python3
"""UTF-8 validation function"""


def validUTF8(data):
    """Validate utf8"""
    def validate_sequence(i):
        """Validate sequence"""
        if len(data) < i:
            return False
        for _ in range(i):
            if not data.pop().startswith("10"):
                return False
        return True

    data = [format(seq, '08b') for seq in reversed(data)]
    while data:
        seq = data.pop()
        if seq.startswith("0"):
            continue
        if seq.startswith("110"):
            if not validate_sequence(1):
                return False
        elif seq.startswith("1110"):
            if not validate_sequence(2):
                return False
        elif seq.startswith("11110"):
            if not validate_sequence(3):
                return False
        else:
            return False
    return True
