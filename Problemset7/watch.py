import re


def main():
    print(parse(input("HTML: ")))


def parse(html):
    if matches := re.search(
        r"(https://(www\.)?youtube\.com/embed/[a-zA-Z0-9]+)+", html, re.IGNORECASE
    ):
        lst1 = list(matches.groups(0))
        lis = lst1[0].replace("www.", "")
        lst = lis.split("be.com/embed")
        result = lst[0] + ".be" + lst[1]
        if "youtu.be" in result:
            return result
    elif matches := re.search(
        r"(http://(www\.)?youtube\.com/embed/[a-zA-Z0-9]+)+", html, re.IGNORECASE
    ):
        lst1 = list(matches.groups(0))
        lis = lst1[0].replace("www.", "")
        lst = lis.split("be.com/embed")
        result = lst[0] + ".be" + lst[1]
        if "youtu.be" in result:
            if "http" in result:
                result = result.replace("http", "https")
                return result

    else:
        return None


if __name__ == "__main__":
    main()

# <iframe width="560" height="315" src="http://www.youtube.com/embed/xvFZjo5PgG0"
# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
# clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
