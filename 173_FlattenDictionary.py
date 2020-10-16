# Follow-up: Could this be accomplished IN-PLACE?
# I still haven't devised a method to accomplish this yet...

def flatten(dic):
    """Given a nested dicionary DIC, flattens said DIC.

    *Namespaces the keys with a period (.)*

    >>> dic = {
    ...     "key": 3,
    ...     "foo": {
    ...         "a": 5,
    ...         "bar": {
    ...             "baz": 8
    ...         }
    ...     }
    ... }
    >>> dic = flatten(dic)
    >>> pretty_print(dic)
    {
        "key": 3,
        "foo.a": 5,
        "foo.bar.baz": 8
    }
    """
    assert dic, 'Cannot flatten an empty dictionary DIC.'

    flat_dic = {}
    def flatten_recur(dic, path):
        if type(dic) != dict:
            flat_dic[path] = dic
        else:
            for k in dic:
                new_path = f"{path}.{k}" if path else k
                flatten_recur(dic[k], new_path)

    flatten_recur(dic, "")
    return flat_dic

def pretty_print(dic):
    """Pretty-prints a given 1D dicionary DIC.
    """

    keys = list(dic.keys())

    print('{')
    for k in keys[:-1]:
        print(f'    "{k}": {dic[k]},')
    print(f'    "{keys[-1]}": {dic[keys[-1]]}')
    print('}')