import mark_safe, TABLE_HEADER


def printitems():

    if len(data['lists']) > 6:
        for i in range(len(data['lists'])):
            count.append(data['lists'][i])
    else:
        for i in range(len(data['lists'])):
            return items(data['lists'][i])

def items(dictt):
    if dictt['is_done']:
        return mark_safe(TABLE_HEADER + '''<a href="#"><li class="is_done_text">''' + dictt['name'] + '''</li></a></div>''' + TABLE_TAIL)
    else:
        return mark_safe(TABLE_HEADER + '''<a href="#"><li>''' + dictt['name'] + '''</li></a></div>''' + TABLE_TAIL)