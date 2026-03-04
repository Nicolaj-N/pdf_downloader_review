import re

def get_file_extension_regex(url):
    match = re.search(r'\.([a-zA-Z0-9]+)$', url)
    if match:
        return match.group(1)
    else:
        return None

# Example usage:
url = "http://www.eugesta.lt/assets/SOCIALINES-ATSAKOMYBES-ATASKAITA-2016.pdf"
extension = get_file_extension_regex(url)
print("File extension:", extension)