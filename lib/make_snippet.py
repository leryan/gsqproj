def Make_snippet(string):
    lst=string.split()
    if len(lst)<= 5:
        return string
    else:
        return ' '.join(lst[:5])+'...'