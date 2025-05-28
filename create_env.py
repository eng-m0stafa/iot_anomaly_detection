# Create .env file with proper UTF-8 encoding
with open(".env", "w", encoding="utf-8") as f:
    f.write("API_KEY=your_secret_key_here")
print("Created .env file successfully!")
