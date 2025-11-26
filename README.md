 Cryptography Basics - Hashing & Security

Practical cryptography demonstrations showing hashing fundamentals and real-world security applications.

##  Quick Start

```bash
# Clone the repository
git clone https://github.com/ndi-tech/Cryptography-Projects.git
cd cryptography-basics

# Run demonstrations
python3 simple_test.py
python3 hashing_demo.py
./openssl_demo.sh
 What's Included
simple_test.py
Basic hashing introduction

MD5 and SHA-256 examples

Perfect for beginners

hashing_demo.py
Comprehensive hashing properties

File integrity checking

Multiple algorithms (MD5, SHA-1, SHA-256)

openssl_demo.sh
Professional OpenSSL tools

Supply chain attack simulation

Real-world security verification

 Learning Outcomes
Cryptographic hashing fundamentals

File integrity verification

OpenSSL command-line tools

Security breach prevention

Technologies
Python 3 with hashlib

OpenSSL cryptography

Bash scripting

Multiple hash algorithms

Perfect for cybersecurity students, developers, and IT professionals learning cryptography.



MIT License

Copyright (c) 2024 Cryptography Basics

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

GITHUB DEPLOYMENT COMMANDS
# Create the simplified project
mkdir cryptography-basics
cd cryptography-basics

# Create all 5 files above in the directory

# Make scripts executable
chmod +x openssl_demo.sh
chmod +x simple_test.py
chmod +x hashing_demo.py

# Initialize git and push to GitHub
git init
git add .
git commit -m "Initial commit: Cryptography Basics - Hashing demonstrations"
git branch -M main
git remote add origin https://github.com/yourusername/cryptography-basics.git
git push -u origin main
