
import re
def main():
    html = input("HTML: ")
    html = html.strip()
    site = (extract(html))
    if site != None:
        site = site.replace('www.youtube.com','youtu.be')
    print(site)



def extract(html):
    # https{0,1} looks for http followed by 0 or 1 's'
    # \S+ looks for 1 or more non-whitespace characters
    # \" searches for the quotation marks within html that surround the web address in html

    matches = re.search(r"src=\"(https{0,1}://www.youtu\S+)\"", html)
    if matches:
        print()
        site =matches.groups()
        return site[0]
    else:
       return None


if __name__ == '__main__':
    main()