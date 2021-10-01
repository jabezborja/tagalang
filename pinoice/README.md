## For writing the grammar example of Pinoice to use as a reference when doing some Pinoice

# Variables
```
baryabol na letra name ay "Jabez"
baryabol na numero edad ay 17
```
> The <na> is for determining the type of the variable as we have 6 types:
> The letra, numero, ano, hanay, wala, and kahitano
> that equals to String, Integer, Boolean, Array, None or Null and Any respectively in 
> other languages for type safe purposes as I'm a big fan of Typescript haha.

But it is ignorable as the default value of a 'baryabol' is 'kahitano' or Any.
```
baryabol name ay "Jabez"
```

# Printing
```
ipahayag ang name + edad
```

# If-else statement
```
kung name ay "Jabez" tapos
    ipahayag ang "Kumusta, " + name
odikaya name ay "Linus" tapos
    ipahayag ang "Uyy, pre! Salamat sa Git mo."
iba tapos
    ipahayag ang "Di kita kilala, pasensya na."
pagtatapos
```

# For loops
```
baryabol listahan_ni_aling_cely ay ["100 sa milk", "200 sa gatas", "300 sa bear brand"]

sakada listahan_ni_aling_cely bilang lista tapos
    ipahayag ang "Binili ni aling cely ang " + lista
patatapos
```

# While loops
```
baryabol count ay 0

habang count ay hindi 10 tapos
    count ay count + 1
pagtatapos
```

# Functions
```
tukuyin ipagadd kasama num_1, num_2 tapos
    bumalik kasama num_1 + num_2
pagtatapos

baryabol num_1 ay 10
baryabol num_2 ay 10

// Prints 20
ipahayag ang ipagadd kasama num_1, num_2
```

## For clarification, in Python it is equivalent to
```py
def ipagadd(num_1, num_2):
    return num_1 + num_2

num_1 = 10
num_2 = 10

print(ipagadd(num_1, num_2))
```
