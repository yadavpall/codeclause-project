import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, long_url):
        # Generate a unique hash for the long URL
        hash_object = hashlib.md5(long_url.encode())
        hash_value = hash_object.hexdigest()[:8]

        # Create a short URL by appending the hash to a base URL
        short_url = f"http://short.url/{hash_value}"

        # Store the mapping between short and long URLs
        self.url_mapping[short_url] = long_url

        return short_url

    def expand_url(self, short_url):
        # Retrieve the long URL from the mapping
        long_url = self.url_mapping.get(short_url, None)

        if long_url is not None:
            return long_url
        else:
            return "URL not found"

# Example usage:
url_shortener = URLShortener()

# Shorten a URL
long_url = "https://www.example.com"
short_url = url_shortener.shorten_url(long_url)
print(f"Short URL: {short_url}")

# Expand a URL
expanded_url = url_shortener.expand_url(short_url)
print(f"Expanded URL: {expanded_url}")