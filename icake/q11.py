# I wrote a crawler that visits web pages, stores a few keywords
# in a database, and follows links to other web pages. I noticed
# that my crawler was wasting a lot of time visiting the same pages
# over and over, so I made a set, visited, where I'm storing URLs 
# I've already visited. Now the crawler only visits a URL if it
# hasn't already been visited.

# Thing is, the crawler is running on my old desktop computer in 
# my parents' basement (where I totally don't live anymore), and 
# it keeps running out of memory because visited is getting so huge.

# How can I trim down the amount of space taken up by visited?

class Trie:
    def __init__(self):
        self.root = {}
    
    def add_url(self, url):
        node = self.root
        is_new_url = False

        # walk char by char in the given string
        for char in url:
            if char not in node:
                # found a new url
                node[char] = {}
                is_new_url = True
            node = node[char]

        if "**DONE**" not in node:
            # found a new url
            node["**DONE**"] = {}
            is_new_url = True

        return is_new_url

# I first thought of using hashes, but realized that strong hashes
# may often take more space than the URL itself. So we won't be saving
# much space. Then indexed the URL by the parent website. That did
# bring down the space, but not by a whole lot. I took a hint to 
# break it down to single character, and the index them at every level.

# Need to revisit this with different solutions.

        
