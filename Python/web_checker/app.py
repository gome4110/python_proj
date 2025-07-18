print("🔎 Welcome To Website URL Checker 🔍")

user_url = input("🌐Enter a website URL: ")


# We are checking if the user's website URL starts with HTTPS or HTTP.
# If it starts with HTTPS, it's secure.
# If it starts with HTTP, it's not secure.
# If it doesn't start with either, we assume it's not a valid URL.

if user_url.lower().startswith("https://"):
    print("This website use HTTPS URL. (🔐 Secure)")
elif user_url.lower().startswith("http://"):
    print("This website use HTTP URL. (🚫🔓 Not Secure)")
else:
    print("❌The website URL that you enter is not URL at all!❌")
