import sys


def main():
    domain = sys.argv[1]
    output = sys.argv[2]
    if domain == "google.com":
        subdomains = [
            "mail.google.com",
            "fonts.google.com",
            "cloud.google.com",
        ]
    elif domain == "2.com":
        subdomains = [
            "a.2.com",
            "b.2.com",
            "c.2.com",
            "d.2.com",
            "e.2.com",
        ]
    else:
        subdomains = [
            "example.com",
        ]
    with open(output, "w") as f:
        f.write("\n".join(subdomains))



if __name__ == "__main__":
    main()