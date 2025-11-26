#!/bin/bash

echo " OPENSSL CRYPTOGRAPHY DEMONSTRATION"
echo "======================================"
echo "Professional cryptographic tools for real-world security"

mkdir -p openssl_test
cd openssl_test

echo ""
echo "📝 CREATING TEST FILES..."
echo "Hello Crypto World from Ubuntu Server!" > message.txt
echo "Configuration data for secure app" > config.xml
echo "Library files and dependencies" > libs.tar.gz

echo ""
echo "🔍 GENERATING CRYPTOGRAPHIC HASHES:"

for file in message.txt config.xml libs.tar.gz; do
    if [ -f "$file" ]; then
        echo "📄 $file:"
        echo "  MD5:    $(openssl dgst -md5 "$file" | cut -d' ' -f2)"
        echo "  SHA-1:  $(openssl dgst -sha1 "$file" | cut -d' ' -f2)"
        echo "  SHA-256: $(openssl dgst -sha256 "$file" | cut -d' ' -f2)"
        echo ""
    fi
done

echo " SECURITY VERIFICATION TEST:"
echo "-----------------------------"
original_hash=$(openssl dgst -sha256 message.txt | cut -d' ' -f2)
echo "Original SHA-256: $original_hash"

echo ""
echo " SIMULATING FILE TAMPERING..."
echo "# MALICIOUS MODIFICATION" >> message.txt
echo "echo 'Security breach detected'" >> message.txt

modified_hash=$(openssl dgst -sha256 message.txt | cut -d' ' -f2)
echo "After tampering:  $modified_hash"

echo ""
echo "🔐 SECURITY CHECK:"
if [ "$original_hash" != "$modified_hash" ]; then
    echo " TAMPERING DETECTED - Cryptographic verification works!"
    echo " This prevents installation of compromised software"
else
    echo " No changes detected"
fi

echo ""
echo " AVAILABLE HASH ALGORITHMS:"
openssl list -digest-commands

cd ..
echo ""
echo " OpenSSL demonstration completed!"
echo " Used by enterprises worldwide for software verification"
