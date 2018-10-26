from Cache import Cache
import random

if __name__ == '__main__':

    # Test the cache
    Keys = [i for i in range(10)]     # Total Entries
    sites = ['www.google.com ', 'www.yahoo.com ', 'www.goal.com ', 'www.mozilla.com ',
             'www.immigration.ca ', 'www.Ebay.com ', 'www.amazon.com ', 'www.google.com ',
             'www.espn.com ', 'www.natgeo.com ', 'www.BBCEarth.com ']

    # Cache object
    cache = Cache()

    print(cache.empty())

    print(str(cache.isEmpty()))
    for i, key in enumerate(Keys):
        if key in cache:
            continue
        else:
            value = ''.join([random.choice(sites)])
            print('\t',value)
            cache.update(key, value)

        print("{0}.Iteration, #{1} cached entries" .format(i+1, cache.size()))

    print('\n\n\t','*'*10,' CACHE LIST ','*'*10)
    for k, v in cache.viewCache().items():
        print("{0} : {1}".format(k,v))
