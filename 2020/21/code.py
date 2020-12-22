# input
with open('input.txt') as f:
    lines = f.readlines()

# processing
allergens = {}
ingredients_list = []
for line in lines:
    ingredients, contains = line.split('(contains ')
    ingredients = ingredients.split()
    ingredients_list.extend(ingredients)

    contains = [x.strip(',)') for x in contains.split()]
    for contained in contains:
        if contained not in allergens:
            allergens[contained] = set(ingredients)
        else:
            allergens[contained] &= set(ingredients)

# part 1
matched = set()
while True:
    for allergen, ingredients in allergens.items():
        if len(ingredients) == 1:
            matched.update(ingredients)
            continue

        allergens[allergen] = allergens[allergen] - matched

    if len(matched) == len(allergens):
        break
ans1 = sum([ingredient not in matched for ingredient in ingredients_list])

# part 2
alphabetical = sorted(allergens.keys())
ans2 = ','.join([allergens[x].pop() for x in alphabetical])

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
