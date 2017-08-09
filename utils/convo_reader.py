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
                replies += [{'text': i, 'weight': 1}]
            convo += [{
                'starters': queries,
                'replies': replies
                }]
    return convo
