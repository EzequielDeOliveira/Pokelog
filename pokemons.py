from pokedata import data

def nameFormat(name):
    return name.replace('\'','').replace(' ♀ ','').replace(' ♂ ','').lower()

pokemons = data["pokemon"]
f = open('pokelist.pl','w')


pokelist = []
typelist = []
heightlist = []
weightlist = []
nextEvolutionList = []
prevEvolutionList = []
imagelist = []

for pokemon in pokemons:
    pokelist.append(f'pokemon(\'{nameFormat(pokemon["name"])}\', \'{pokemon["num"]}\').')
    
    for poke_type in pokemon["type"]:
        typelist.append(f'type(\'{nameFormat(pokemon["name"])}\', \'{nameFormat(poke_type)}\').')
    
    heightlist.append(f'height(\'{nameFormat(pokemon["name"])}\', \'{pokemon["height"][0:-2] }\').')
    weightlist.append(f'weight(\'{nameFormat(pokemon["name"])}\', \'{pokemon["weight"][0:-3] }\').')
    

    try:
        if "prev_evolution" in pokemon:
            for prev_evolution in pokemon["prev_evolution"]:
                prevEvolutionList.append(
                    f'prev_evolution(\'{nameFormat(pokemon["name"])}\', \'{nameFormat(prev_evolution["name"])}\').')
        else:
            pass
    except:
        pass

    try:
        if "next_evolution" in pokemon:
            for next_evolution in pokemon["next_evolution"]:
                nextEvolutionList.append(
                    f'next_evolution(\'{nameFormat(pokemon["name"])}\', \'{nameFormat(next_evolution["name"])}\').')
        else:
            pass
    except:
        pass

    

    imagelist.append(f'image(\'{nameFormat(pokemon["name"])}\', \'{pokemon["img"]}\').')

print(":- dynamic pokemon/2.",file=f)
print(":- dynamic type/2.",file=f)
print(":- dynamic height/2.",file=f)
print(":- dynamic weight/2.",file=f)
print(":- dynamic next_evolution/2.",file=f)
print(":- dynamic prev_evolution/2.",file=f)
print(":- dynamic image/2.",file=f)
print(file=f)

for poke in pokelist:
    print(poke,file=f)

f.write('\n')

for poketype in typelist:
    print(poketype,file=f)

f.write('\n')

for height in heightlist:
    print(height,file=f)

f.write('\n')

for weight in weightlist:
    print(weight,file=f)

f.write('\n')

for evolution in nextEvolutionList:
    print(evolution,file=f)

f.write('\n')

for preEvolution in prevEvolutionList:
    print(preEvolution,file=f)

f.write('\n')

for image in imagelist:
    print(image,file=f)

f.close()