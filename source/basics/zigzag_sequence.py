def find_zigzag_sequence(sequence, n):
    sequence.sort()
    mid = int(n/2)

    st = mid
    ed = n - 1

    while (st <= ed):
        sequence[st], sequence[ed] = sequence[ed], sequence[st]
        st = st + 1
        ed = ed - 1

    return [ number for number in sequence]