def decompress(text, start=0, times=1):
    for _ in range(times):
        i = start
        while i < len(text) and text[i] != ']':
            if text[i].isalpha():
                yield text[i]
            elif text[i].isdigit():
                sub_times = 0
                while i < len(text) and text[i].isdigit():
                    sub_times = sub_times * 10 + int(text[i])
                    i += 1
                i += 1  # skip left bracket
                for item in decompress(text, start=i, times=sub_times):
                    if str(item).isalpha():
                        yield item
                    else:
                        i = item
            i += 1
        if start > 0:
            yield i
