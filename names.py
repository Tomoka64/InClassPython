def namelist(names):
    #your code here
    toReturn = ''
    if(len(names) == 1):
        return names[0]['name']
    elif(len(names) == 2):
        toReturn = toReturn + names[0]['name'] + " & " + names[1]['name']
    elif(len(names) > 2):
        for i in range(0, len(names)-1):
            toReturn = toReturn + names[i]['name'] + ", "
        toReturn = toReturn[:-2] + " & " + names[len(names)-1]['name']
    return toReturn
#------------------------------------------------------------

names = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]
print(namelist(names))

names = [ {'name': 'Bart'}, {'name': 'Lisa'} ]
print(namelist(names))

names = [ {'name': 'Bart'} ]
print(namelist(names))

#---------------other solution------------------------------
# def namelist(names):
#     if len(names)==0: return ''
#     if len(names)==1: return names[0]['name']
#     return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']
#
# def namelist(names):
#   return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]
