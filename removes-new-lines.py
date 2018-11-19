import re
words_total = []
with open('RetroReportSample-SupremeCourt.txt', 'r',encoding="utf8") as file:
    lines = file.readlines()
    for line in lines:
        line = re.sub(r'[\n”]', '', line)
        # line = re.sub(r'[”]', '', line)
        words = line.split(' ')
        # for word in words:
        #     word.replace('\n', '')
        words_total += words

with open('RetroReportSample-SupremeCourt-modified.txt', 'w', encoding="utf-8") as file:
    final = ' '.join(word for word in words_total)
    # print (final)
    file.write(final)
