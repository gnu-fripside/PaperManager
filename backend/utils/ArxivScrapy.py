# encoding:utf-8
import os
import urllib
import urllib.parse
import urllib.request
import hashlib
constUA = ( "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/60.0.3112.113 Safari/537.36" )


def paperDown(arxivID, paperDir):
    downloadLink = "https://arxiv.org/pdf/" + str(arxivID) + ".pdf"
    request = urllib.request.Request(downloadLink)
    request.add_header("User-Agent", constUA)
    get = urllib.request.urlopen(request).read()
    sha1obj = hashlib.sha1()
    sha1obj.update(get)
    hash = str(sha1obj.hexdigest())
    if not os.path.exists(paperDir):
        os.makedirs(paperDir)
    with open(os.path.join(paperDir, hash + ".pdf"), "wb") as f:
        f.write(get)
        f.close()
    return os.path.join(paperDir, hash + ".pdf")
if __name__ == "__main__":
    print(paperDown("1407.0028","paper"))
