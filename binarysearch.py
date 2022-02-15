animals = ["ant","bear","cat","dog","elephant","frog","giraffe","horse","iguana","jackal","kangaroo","lion","marmoset"]


def find(target):
    global animals
    # calculate mid point
    if len(animals) == 0:
        return False
        
    mid = len(animals)//2
    if animals[mid] == target:
        return True
    elif animals[mid] > target:
        # it's in first half, so cut animals list in half
        animals = animals[:mid]
    else:
        # it's in second half, so cut animals list in half
        animals = animals[mid+1:]
    return find(target)
        
print(find("dingo"))