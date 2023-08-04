import sys


def main():
    domain = sys.argv[1]
    output = sys.argv[2]
    if domain == "1.com":
        subdomains = [
            "a.1.com",
            "b.1.com",
            "c.1.com",
            "d.1.com",
            "e.1.com",
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