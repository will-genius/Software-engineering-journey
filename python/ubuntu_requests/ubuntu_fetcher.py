import requests
import os
import hashlib
from urllib.parse import urlparse

def get_filename_from_url(url):
    """Extract filename from URL or generate one if missing"""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:  # If no filename, generate a default
        filename = "downloaded_image.jpg"
    return filename

def is_duplicate(content, folder="Fetched_Images"):
    """Check if the file (by hash) already exists in the folder"""
    file_hash = hashlib.md5(content).hexdigest()
    for fname in os.listdir(folder):
        fpath = os.path.join(folder, fname)
        with open(fpath, "rb") as f:
            if hashlib.md5(f.read()).hexdigest() == file_hash:
                return True
    return False

def fetch_image(url):
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Fetch with respectful headers
        headers = {
            "User-Agent": "UbuntuFetcher/1.0 (Respectful Image Collector)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Check Content-Type before saving
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ The URL does not point to an image: {url}")
            return
        
        # Duplicate check
        if is_duplicate(response.content, "Fetched_Images"):
            print(f"⚠ Duplicate image skipped: {url}")
            return
        
        # Save image
        filename = get_filename_from_url(url)
        filepath = os.path.join("Fetched_Images", filename)
        
        with open(filepath, "wb") as f:
            f.write(response.content)
        
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Ask user for one or multiple URLs
    urls = input("Please enter one or more image URLs (separated by spaces): ").split()
    
    for url in urls:
        fetch_image(url)
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
