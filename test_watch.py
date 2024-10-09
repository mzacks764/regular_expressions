

from watch import extract

def test_valid():
    assert extract('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "http://www.youtube.com/embed/xvFZjo5PgG0"
    assert extract('<iframe width="560" height="315" src="https://www.youtube.com/xxx"></iframe>') == "https://www.youtube.com/xxx"

def test_invalid():
    assert extract('<iframe width="560" height="315"</iframe>') == None
def test_non_youtube():
    assert extract('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None






