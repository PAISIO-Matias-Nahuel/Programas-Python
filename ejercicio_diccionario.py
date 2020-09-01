import pprint

message = 'sdfasdjfhasdfhalsdjfhaslkjdhalskdjfhalskdjfhalskjdfhlsajkdfhlsakjdfhlaskdjhaslkjdfhalskjdfhalskjdfhalskdjfhalsjdfhalskjdfhalskjdfhlaskjdfhalskjdfhalskjdfhalskjdfhalskjdfhalskjdfhalskjdfhalskdjfhalskdjfhaslkdjfhaslkjdfhaslkjdfhsdlvbrjhybwligbgrligbrilreilvgbhivilvuwilrrlwigerliubvlibv vtilfvb ibib elifb riuefbewlrifb eribwerilfblibr flwerifb lribferuifb elifbilf wiulefb wibf lerifb erifb ilerfb lerbfewilrfb lbf ierubflwieb liwebf libeflwefbewif beirfb lwerbf lierbfwrbfqlkrfbiubfwgyt gb2rgw rewb ryuwergb rygb ergfb eiwbrfebferufb '
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

## pprint.pprint(count) misma cosa que abajo

rjtext = pprint.pformat(count)
print(rjtext)
