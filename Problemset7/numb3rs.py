import re
def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip):
        lst = ip.split(".")
        if int(0 < int(lst[0]) < 256):
            for i in lst:
                if 0 < int(i) or int(i) < 255:
                     return True
        else:
            return False

    else:
        return False
if __name__ == "__main__":
    main()
# 192.169.0.1
# 1.2.3.1
