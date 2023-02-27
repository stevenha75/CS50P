import re


def main():
    print(parse(input("HTML: ")))

# Parses HTML input and returns a shortened link
def parse(s):
    # Checks general formatting
    if matches := re.search(r"^<iframe .*src=\"([a-zA-Z0-9:/\.]+)\".*></iframe>", s):
        # Stores URL group
        URL = matches.group(1)
        # Checks URL formatting & stores vid ID
        if URL := re.search(
            r"^http(?:s)?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)$", URL
        ):
            # Returns shortened link if all is well
            return "https://youtu.be/" + URL.group(1)
        # Return none if fails link check
        else:
            return "None"
    # Return none if fails general formatting check
    else:
        return "None"


if __name__ == "__main__":
    main()
