import sys
sys.setrecursionlimit(1000000)

# https://www.geeksforgeeks.org/de-bruijn-sequence-set-1/

def debruijn_sequence(C, k):
    """Given a list of characters C and a positive integer K, returns a possible
    De Bruijn sequence, where a De Bruijn sequence is a cyclic sequence in which
    every possible K-length string of characters in C occurs exactly once.

    >>> debruijn_sequence(['0', '1'], 3)
    '0011101000'
    >>> debruijn_sequence(['a', 'b', 'c', 'd', 'e'], 5)
    'aaaaeeeeedeededeeeddededdeedddedddddeeeecdeeecedeecddeeceedecdedeceddecdddeceececdececeeedcdeedcededcddedcecedceeddcdeddcedddcddddcecddceecdcdecdcedcdcddcdceeeccdeeccedeccddeccececcdcecceedccdedcceddccdddccecdccdcdcceecccdecccedcccddccceccccdccccceeeebdeeebceeebedeebddeebcdeebeceebdceebcceebeedebdedebcedebeddebdddebcddebecdebdcdebccdebeecebdecebcecebedcebddcebcdcebeccebdccebcccebeebebdebebcebebeeedbdeedbceedbededbddedbcdedbecedbdcedbccedbebedbeeddbdeddbceddbedddbddddbcdddbecddbdcddbccddbebddbeecdbdecdbcecdbedcdbddcdbcdcdbeccdbdccdbcccdbebcdbeebdbdebdbcebdbedbdbddbdbcdbdbeeecbdeecbceecbedecbddecbcdecbececbdcecbccecbebecbdbecbeedcbdedcbcedcbeddcbdddcbcddcbecdcbdcdcbccdcbebdcbdbdcbeeccbdeccbceccbedccbddccbcdccbecccbdcccbccccbebccbdbccbeebcbdebcbcebcbedbcbddbcbcdbcbecbcbdcbcbccbcbeeebbdeebbceebbedebbddebbcdebbecebbdcebbccebbebebbdbebbcbebbeedbbdedbbcedbbeddbbdddbbcddbbecdbbdcdbbccdbbebdbbdbdbbcbdbbeecbbdecbbcecbbedcbbddcbbcdcbbeccbbdccbbcccbbebcbbdbcbbcbcbbeebbbdebbbcebbbedbbbddbbbcdbbbecbbbdcbbbccbbbebbbbdbbbbcbbbbbeeeeadeeeaceeeabeeeaedeeaddeeacdeeabdeeaeceeadceeacceeabceeaebeeadbeeacbeeabbeeaeedeadedeacedeabedeaeddeadddeacddeabddeaecdeadcdeaccdeabcdeaebdeadbdeacbdeabbdeaeeceadeceaceceabeceaedceaddceacdceabdceaecceadcceaccceabcceaebceadbceacbceabbceaeebeadebeacebeabebeaedbeaddbeacdbeabdbeaecbeadcbeaccbeabcbeaebbeadbbeacbbeabbbeaeeaeadeaeaceaeabeaeaeeedadeedaceedabeedaededaddedacdedabdedaecedadcedaccedabcedaebedadbedacbedabbedaeaedaeeddadeddaceddabeddaedddaddddacdddabdddaecddadcddaccddabcddaebddadbddacbddabbddaeaddaeecdadecdacecdabecdaedcdaddcdacdcdabdcdaeccdadccdacccdabccdaebcdadbcdacbcdabbcdaeacdaeebdadebdacebdabebdaedbdaddbdacdbdabdbdaecbdadcbdaccbdabcbdaebbdadbbdacbbdabbbdaeabdaeeadadeadaceadabeadaedadaddadacdadabdadaeeecadeecaceecabeecaedecaddecacdecabdecaececadcecaccecabcecaebecadbecacbecabbecaeaecadaecaeedcadedcacedcabedcaeddcadddcacddcabddcaecdcadcdcaccdcabcdcaebdcadbdcacbdcabbdcaeadcadadcaeeccadeccaceccabeccaedccaddccacdccabdccaecccadcccaccccabcccaebccadbccacbccabbccaeaccadaccaeebcadebcacebcabebcaedbcaddbcacdbcabdbcaecbcadcbcaccbcabcbcaebbcadbbcacbbcabbbcaeabcadabcaeeacadeacaceacabeacaedacaddacacdacabdacaecacadcacaccacabcacaeeebadeebaceebabeebaedebaddebacdebabdebaecebadcebaccebabcebaebebadbebacbebabbebaeaebadaebacaebaeedbadedbacedbabedbaeddbadddbacddbabddbaecdbadcdbaccdbabcdbaebdbadbdbacbdbabbdbaeadbadadbacadbaeecbadecbacecbabecbaedcbaddcbacdcbabdcbaeccbadccbacccbabccbaebcbadbcbacbcbabbcbaeacbadacbacacbaeebbadebbacebbabebbaedbbaddbbacdbbabdbbaecbbadcbbaccbbabcbbaebbbadbbbacbbbabbbbaeabbadabbacabbaeeabadeabaceababeabaedabaddabacdababdabaecabadcabaccababcabaebabadbabacbababbabaeeeaadeeaaceeaabeeaaedeaaddeaacdeaabdeaaeceaadceaacceaabceaaebeaadbeaacbeaabbeaaeaeaadaeaacaeaabaeaaeedaadedaacedaabedaaeddaadddaacddaabddaaecdaadcdaaccdaabcdaaebdaadbdaacbdaabbdaaeadaadadaacadaabadaaeecaadecaacecaabecaaedcaaddcaacdcaabdcaaeccaadccaacccaabccaaebcaadbcaacbcaabbcaaeacaadacaacacaabacaaeebaadebaacebaabebaaedbaaddbaacdbaabdbaaecbaadcbaaccbaabcbaaebbaadbbaacbbaabbbaaeabaadabaacabaababaaeeaaadeaaaceaaabeaaaedaaaddaaacdaaabdaaaecaaadcaaaccaaabcaaaebaaadbaaacbaaabbaaaeaaaadaaaacaaaabaaaaa'
    """
    assert C, 'C canot be an empty set.'
    assert k > 0, 'K must be a positive integer.'
    assert len(C)**k <= 50000, 'Finding a De Bruijn sequence with these parameters would be too computationally-intensive.'

    n = len(C)
    visited, edges = set(), []
    def dfs(node, n):
        for i in range(n):
            s = node + C[i]
            if s not in visited:
                visited.add(s)
                dfs(s[1:], n)
                edges.append(i)

    starting_node = C[0] * (k-1)
    dfs(starting_node, n)

    res = ''
    for i in range(n**k):
        res += C[edges[i]]
    res += starting_node
    return res