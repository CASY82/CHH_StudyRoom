while True:
    sentense = input()

    if sentense == 'EOI':
        break

    sentense = sentense.lower()

    if 'nemo' in sentense:
        print('Found')
    else:
        print('Missing')