def align_text(lines, width, alignment):
    if alignment == 'ліво':
        return [line.ljust(width) for line in lines]  
    elif alignment == 'центр':
        return [line.center(width + 40) for line in lines]  
    elif alignment == 'право':
        return [line.rjust(width + 80) for line in lines]  
