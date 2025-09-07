Ubuntu Image Fetcher

"I am because we are." – The Wisdom of Ubuntu

The Ubuntu Image Fetcher is a Python tool that connects to the web community, fetches images mindfully, and organizes them for later sharing. It reflects Ubuntu principles of community, respect, sharing, and practicality.

✨ Features

📥 Download images from user-provided URLs

📂 Automatically organizes them into a Fetched_Images folder

🛡️ Handles errors gracefully (connection issues, invalid URLs, etc.)

🔎 Prevents duplicate downloads using file hashes

✅ Verifies that URLs actually point to images before saving

🌐 Supports fetching multiple images at once

🛠️ Requirements

Python 3.x

requests

Install dependencies:

pip install requests

🚀 Usage

Run the script:

python ubuntu_fetcher.py


Example interaction:

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (separated by spaces): 
https://example.com/ubuntu-wallpaper.jpg https://example.com/logo.png

✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg
✓ Successfully fetched: logo.png
✓ Image saved to Fetched_Images/logo.png

Connection strengthened. Community enriched.

📌 Ubuntu Principles in Practice

Community: Connects to the wider web to fetch shared resources.

Respect: Handles errors gracefully without crashing.

Sharing: Saves and organizes images for later use.

Practicality: Provides a real, reusable tool.

📚 Challenge Features

Multiple URL support

Duplicate prevention with hashing

HTTP header validation for images

Respectful User-Agent

📂 Repository Structure
Ubuntu_Requests/
│── ubuntu_fetcher.py     # Main Python script
│── README.md             # Documentation
└── Fetched_Images/       # Auto-created storage for downloaded images

👥 Author

Developed with ❤️ in the spirit of Ubuntu.