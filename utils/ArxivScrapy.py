#encoding:utf-8
import urllib
import urllib.parse
import urllib.request
constUA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) " \
        "AppleWebKit/537.36 (KHTML, like Gecko) " \
        "Chrome/60.0.3112.113 Safari/537.36"
def paperDown(arxivID, paperPath):
    downloadLink = "https://arxiv.org/pdf/" + str(arxivID) + ".pdf"
    request = urllib.request.Request(downloadLink)
    request.add_header("User-Agent", constUA)
    get = urllib.request.urlopen(request)
    with open(paperPath, "wb") as f:
        f.write(get)
        f.close()
