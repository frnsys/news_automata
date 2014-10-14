import sys
import twitter

def main():
    try:
        import config
    except ImportError:
        print('No config found. Have you renamed `config-sample.py` to `config.py` and filled in your info?')
        return

    if len(sys.argv) < 2:
        print('Please tell me what example to run!')
        return

    try:
        globals()[sys.argv[1]]();
    except KeyError:
        print('Doesn\'t seem to be an example by that name.')
        return

def tweets():
    for tweet in twitter.tweets('frnsys'):
        print('\n')
        print(tweet)

if __name__ == '__main__':
    main()
