```python
#!/usr/bin/env python3
"""
Basic Cryptography - Simple Hashing Test
Perfect for beginners learning cryptographic hashing
"""

import hashlib

def main():
    print("=== SIMPLE HASHING TEST ===")
    text = "Hello Cryptography World!"
    print(f"Text: '{text}'")
    
    # MD5 Hashing
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    print(f"MD5: {md5_hash}")
    
    # SHA-256 Hashing
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    print(f"SHA-256: {sha256_hash}")
    
    print(" Basic hashing works!")
    print("\n MD5 is insecure - use SHA-256 for real security!")
    
    # Show hash properties
    print("\n Hash Properties Demo:")
    same_text = "Hello Cryptography World!"
    different_text = "Hello Cryptography World!!"
    
    hash1 = hashlib.sha256(text.encode()).hexdigest()
    hash2 = hashlib.sha256(same_text.encode()).hexdigest()
    hash3 = hashlib.sha256(different_text.encode()).hexdigest()
    
    print(f"Same input:    {hash1[:16]}...")
    print(f"Same input:    {hash2[:16]}...")
    print(f"Different input: {hash3[:16]}...")
    print(f"✓ Deterministic: {hash1 == hash2}")
    print(f"✓ Avalanche effect: {hash1 != hash3}")

if __name__ == "__main__":
    main()
