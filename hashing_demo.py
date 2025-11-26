#!/usr/bin/env python3
"""
Comprehensive Cryptography - Hashing Demonstration
Covers multiple algorithms and real-world applications
"""

import hashlib
import os

def print_header(title):
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def demo_basic_hashes():
    print_header("BASIC HASH FUNCTIONS")
    
    messages = [
        "Hello Cryptography!",
        "password123",
        "Ubuntu Server",
        "a",  # Single character
        ""    # Empty string
    ]
    
    for message in messages:
        print(f"\nMessage: '{message}'")
        md5 = hashlib.md5(message.encode()).hexdigest()
        sha1 = hashlib.sha1(message.encode()).hexdigest()
        sha256 = hashlib.sha256(message.encode()).hexdigest()
        
        print(f"  MD5:     {md5}")
        print(f"  SHA-1:   {sha1}")
        print(f"  SHA-256: {sha256}")

def demo_hash_properties():
    print_header("HASH PROPERTIES")
    
    print("1.  DETERMINISTIC - Same input = Same output")
    text = "Hello World"
    hash1 = hashlib.sha256(text.encode()).hexdigest()
    hash2 = hashlib.sha256(text.encode()).hexdigest()
    print(f"   Input: '{text}'")
    print(f"   Hash 1: {hash1[:16]}...")
    print(f"   Hash 2: {hash2[:16]}...")
    print(f"   ✓ Hashes match: {hash1 == hash2}")
    
    print("\n2.  AVALANCHE EFFECT - Small change = Big difference")
    msg1 = "Hello World"
    msg2 = "Hello World!"
    hash1 = hashlib.sha256(msg1.encode()).hexdigest()
    hash2 = hashlib.sha256(msg2.encode()).hexdigest()
    print(f"   Input 1: '{msg1}' -> {hash1[:16]}...")
    print(f"   Input 2: '{msg2}' -> {hash2[:16]}...")
    print(f"   ✓ Hashes completely different: {hash1 != hash2}")

def demo_file_hashing():
    print_header("FILE INTEGRITY CHECKING")
    
    os.makedirs("data", exist_ok=True)
    
    files = {
        "document.txt": "This is a confidential document.\nImportant data here.",
        "config.json": '{"database": "mysql", "port": 3306, "ssl": true}',
        "script.py": "#!/usr/bin/env python3\nprint('Hello World')"
    }
    
    for filename, content in files.items():
        filepath = f"data/{filename}"
        
        with open(filepath, "w") as f:
            f.write(content)
        
        with open(filepath, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        
        print(f" {filename}:")
        print(f"   Size: {len(content)} bytes")
        print(f"   SHA-256: {file_hash}")
        print()

def main():
    print(" COMPREHENSIVE CRYPTOGRAPHY DEMONSTRATION")
    print("All computations done locally - no internet needed!")
    
    demo_basic_hashes()
    demo_hash_properties()
    demo_file_hashing()
    
    print("\n All demonstrations completed successfully!")
    print("\n Real-world applications:")
    print("• Password storage verification")
    print("• Software download integrity")
    print("• Data tamper detection")
    print("• Digital forensics")

if __name__ == "__main__":
    main()
