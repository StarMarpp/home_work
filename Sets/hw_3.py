#f = 75 #75 семей выписывают газету
#n = 27 #27 журналов
#mag = 13 #13 журналов и газет

newspaper = set(range(int(input('Сколько семей выписывают газету '))))
magazine = set(range(int(input('Сколько выписывают журнолов '))))
both = set(range(int(input('Сколько выписывают газет и журналов '))))

print(len(newspaper.difference(both)) + len(magazine))




















