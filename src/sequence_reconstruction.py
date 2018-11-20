def sequence_reconstruction(org, seqs):
    """
    :type org: List[int]
    :type seqs: List[List[int]]
    :rtype: bool
    """

    # check if all and letters in org show up in seq
    letters = {i: False for i in org}
    for s in seqs:
        if len(s) > len(org):
            return False
        for l in s:
            if l not in letters:  # if letter out of bounds
                return False
            else:
                letters[l] = True
    for l in letters:
        if not letters[l]:
            return False  # if seq does not have a letter that is in org

    # check if each pair in org show up in seqs
    seq_pairs = set()
    for s in seqs:
        for i in range(len(s) - 1):
            seq_pairs.add((s[i], s[i + 1]))
    org_pairs = {(org[i], org[i + 1]): False for i in range(len(org) - 1)}
    for p in seq_pairs:
        if p in org_pairs:
            org_pairs[p] = True
    for p in org_pairs:
        if not org_pairs[p]:
            return False

    # check topological ordering
    for s in seqs:
        i = 0
        j = 0
        while i < len(org) and j < len(s):
            if org[i] == s[j]:
                j += 1
            i += 1
        if j != len(s):
            return False
    return True
