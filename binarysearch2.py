animals = ["ant","bear","cat","dog","elephant","frog","giraffe","horse","iguana","jackal","kangaroo","lion","marmoset"]


def find(target, thelist):
    # calculate mid point
    if len(thelist) == 0:
        return False
        
    mid = len(thelist)//2
    if thelist[mid] == target:
        return True
    elif thelist[mid] > target:
        # it's in first half, so cut thelist  in half
        return find(target, thelist[:mid])
    else:
        # it's in second half, so cut thelist in half
        return find(target, thelist[mid+1:])

        
print(find("dingo", animals))