'''
Assume shortenToDate's input will always be a string, e.g. "Friday May 2, 7pm". 
Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2".
'''
def shorten_to_date(long_date):
    return long_date.split(',')[0]