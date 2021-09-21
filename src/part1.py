def volume_kubus(x):
    """Return the volume of a cube

    Raise a RuntimeError exception with message "negatieve lengte" if x < 0.
    """
    if x < 0:
        print("negatieve lengte")
        raise RuntimeError
    
    else:
        result = x*x*x

    return result
    


def minutes_in_day(x):
    """Return the number of minutes in x days

    Raise a custom NegativeDuration exception if x < 0.
    """
    eendag = 1440
    if x < 0:
        raise RuntimeError
    
    else:
        result = x * eendag
    return result
    


def minutes_in_week(x):
    """Return the number of minutes in x weeks"""
    eenweek = 10080
    result = x * eenweek 
    return result
    


def list_of_squares(n):
    """Return a list of the first n squares

    >>> list_of_squares(3)
    [0, 1, 4]
    """
    a = [i*i for i in range(n)]
    return a



def product_of_list(l):
    """Return the product of all numbers in the list

    >>> product_of_list([2,3,4])
    24
    """
    a = 1
    for i in l:
        a *= i
    return a
    


def price_search(articles, name):
    """Return the price of the article in list articles

    >>> articles = [
        ["Doom", 25],
        ["Among Us", 5],
    ]
    >>> price_search("Doom")
    25
    """
    for i in articles:
        if i == name:
            return articles[1]
    return None
