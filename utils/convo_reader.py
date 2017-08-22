import json

def convert_to_json(raw):
    # Setup variable to return at end
    convo = []
    formatted = raw.split('Q: ')
    for a in formatted:
        if len(a) > 0:
            actual_data = a.split('\nR: ')
            # Separate out queries and generate multiple if ; exists
            queries = actual_data[0].split('; ')
            # Strip all newlines
            actual_data[1] = actual_data[1].replace('\n', '')
            replies = []
            for i in actual_data[1].split('; '):
                data = i.split('|')
                to_add = {'text': data[0], 'weight': 1}
                try:
                    converted = json.loads(data[1])
                    try:
                        to_add['image'] = converted['image']
                    except:
                        do_nothing = True
                except:
                    do_nothing = True
                replies += [to_add]
            convo += [{
                'starters': queries,
                'replies': replies
                }]
    return convo
