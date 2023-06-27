import pyshorteners

class URLShortener:
    def __init__(self):
        self.shortener = pyshorteners.Shortener()

    def shorten_url(self, url):
        try:
            # Shorten the URL using the TinyURL service
            shortened_url = self.shortener.tinyurl.short(url)

            # Print the shortened URL
            print("Shortened URL:", shortened_url)

        except pyshorteners.exceptions.ShorteningErrorException as e:
            # Handle any ShorteningErrorException that may occur
            print("Shortening Error:", str(e))

        except Exception as e:
            # Handle any other exceptions
            print("An error occurred:", str(e))

# Create an instance of the URLShortener class
url_shortener = URLShortener()

# Take the URL as user input
url = input("Enter the URL: ")

# Call the shorten_url method of the URLShortener instance
url_shortener.shorten_url(url)
