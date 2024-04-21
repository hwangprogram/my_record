while True:
    sentence = input()

    if sentence == '#':
        break
    else:
        cnt = 0

        for word in sentence:
            if word.lower() in ['a', 'e', 'i', 'o', 'u']:
                cnt += 1
        print(cnt)