key_words = ['75%,', 'Cotton', '12%,', 'Silk', '13%', 'Wool']
# placeholder list for the actual dataset.

# Updated material coeffecients
cotton = 0.75729839;
polyester = 0.02721845;
leather = 0.02308011;
wool = 0.16370883;
silk = 0.14313292;
nylon = 0.04013922;
acrylic = 0.16006172;
fur = 0.68536036;


# values for the different materials

def give_value(dataset):
    materials = 0
    cotton1 = []
    polyester1 = []
    leather1 = []
    wool1 = []
    silk1 = []
    nylon1 = []
    acrylic1 = []
    fur1 = []
    # create local copies of the material values

    for i in range(len(dataset)):
        key_word = dataset[i]
        if 'cotton' == key_word.lower():
            cotton1 = cotton * float(str(dataset[i - 1])[:-2]) * 1 / 100
            materials += cotton1
            print('Hi')

        elif 'polyester' == key_word.lower():
            polyester1 = polyester * float(str(dataset[i - 1])[:-2]) * 1 / 100
            materials += polyester1

        elif 'wool' == key_word.lower():
            wool1 = wool * 13 * 1 / 100
            materials += wool1

        elif 'nylon' == key_word.lower():
            nylon1 = nylon * float(str(dataset[i - 1])[:-2]) * 1 / 100
            materials += nylon1

        elif 'leather' == key_word.lower():
            leather1 = leather * float(str(dataset[i - 1])[:-2]) * 1 / 100
            materials += leather1

        elif 'fur' == key_word.lower():
            fur1 = fur * float(str(dataset[i - 1])[:-2]) * 1 / 100
            materials += fur1

        elif 'acrylic' == key_word.lower():
            acrylic1 = acrylic1 * float(str(dataset[i - 1])[:-2]) * 1 / 100

        elif 'silk' == key_word.lower():
            silk1 = silk * float(str(dataset[i - 1])[:-2]) * 1 / 100
            materials += silk1

    materials *= 100
    materials = round(materials, 0)
    return materials
