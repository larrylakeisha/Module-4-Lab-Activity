# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

# Fixed typo in authors
# Erased extra }
# Added in between author and date in Line 22
# Added expression for the dates to print

'''
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
     }
for author, date in authors.items():
    print ("%s" % author + " died in " + "%s." % date)

'''


for date in range(1863, 1889):
    authors = {
        "Charles Dickens": "1870",
        "William Thackeray": "1863",
        "Anthony Trollope": "1882",
        "Gerard Manley Hopkins": "1889", }

for author in range(date):
    print("%s" % authors + " died in " + "%d." % date)
