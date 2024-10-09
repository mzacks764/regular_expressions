
import re
def main():
    html = input("HTML: ")
    html = html.strip()
    site = (extract(html))
    try:
        site = site.replace('youtube.','youtu.')
        print(site)
    except AttributeError:
        print('None from main')



def extract(html):
    matches = re.search(r"src=\"(https*://www.youtu\S+)\"", html)
    if matches:
        print()
        site =matches.groups()
        return site[0]
    else:
       return None









if __name__ == '__main__':
    main()