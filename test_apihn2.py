import simplejson as json
import httplib2

items = []

if __name__ == "__main__":
    h = httplib2.Http(".cache")
    resp, content = h.request("http://api.ihackernews.com/page", headers={'cache-control':'max-age=300'})
    print json.loads(content)
#    items.extend(json.loads(content)['items'])
#    print items


