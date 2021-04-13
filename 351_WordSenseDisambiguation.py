"""
In order to get this to work accurately, the use of an advanced NLP algorithm may be
necessary; therefore, this problem statement is far too niche. However, if i were to
approach this in a more naive, DSA perspective, this is what I would probably do:

1. Download a corpus that relates English words to its dependencies (sets of words
   that vary depending on the context in which the source word is used)
2. For every ambiguous word, iterate over all its contexts, scanning for all
   dependencies found in the target sentence
        2a. Label each word with the context that found the most dependencies
3. Return the mapping between all ambiguous words and their most probable contexts

As mentioned in (1), the use of word dependencies is crucial to the function of this
algorithm. Since all that is given are definitions relating to the words, not enough
information is provided.
"""