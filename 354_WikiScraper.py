"""
Design a system to crawl and copy all of Wikipedia using a distributed network of
machines.

More specifically, suppose your server has access to a set of client machines. Your
client machines can execute code you have written to access Wikipedia pages, download
and parse their data, and write the results to a database.

Some questions you may want to consider as part of your solution are:
- How will you reach as many pages as possible?
- How can you keep track of pages that have already been visited?
- How will you deal with your client machines being blacklisted?
- How can you update your database when Wikipedia pages are added or updated?

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

The server has three purposes: (1) Distributing VPNs to the client machines/workers,
(2) recommending possible unscraped areas to said workers, and (3) caching results to
keep track of webpages that have been visited. The first is a "back-up" plan in case a
worker is blacklisted; upon receiving a specific number of error codes, the worker
sends a request to the server for a new VPN, and the server responds accordingly. The
second is another "back-up" plan in case a specific number of webpages that a worker
visits have already been visited by other workers; this will utilize a server-side
machine learning algorithm that generalizes visited webpages into broad categories so
that the server can distribute new starting-point webpages that are not yet in those
categories. The third touches a bit on (2) as it relates to visited webpages; the
server will manage a distributed caching system which stores the hashes of the
contents of visited webpages (easy lookups and comparisons for updated webpages, low
space).

The actual scraping algorithm utilized by each worker will essentially be
never-ending BFS. If (1) or (2) occurs, handle it according to the above rules and
continue BFS. BFS + effectively choosing start points so that each worker's probability
of collision is minimized = maximum "ground" covered.
"""