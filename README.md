# Pinoice - A Tagalog Programming Language
## (Former TagaLang)
A tagalog-based syntax programming language where Filipino programmers can play with. Pinoice is based on Python3 Programming Language.

## Example
```
baryabol<letra> pangalan: "Jabez"
baryabol<numero> edad: 17

baryabol<kahitano> PangalanAtEdad: "Si " + pangalan + " ay " + edad + " na taong gulang"

ipahayag(PangalanAtEdad)
```

### Equivalent to
```java
// Java
String pangalan = "Jabez";
int edad = 17
String pangalanatedad = "Si " + pangalan = " ay " + edad + " na taong gulang"

System.out.println(pangalanatedad)
```
```python
# Python
pangalan: str = "Jabez" 
edad: int = 17

pangalanatedad = "Si " + pangalan + " ay " + edad + " na taong gulang"

print(pangalanatedad)
```

## Todos
- [x] Baryabols (Variables)
    - [x] Baryabol types
    - [x] Assign
- [ ] Builtins
    - [ ] Ipahayag (print function)
    - [ ] Lagdaan (input function)
- [ ] Kung-Ibapa statements (If-else statements)
- [ ] Bawat loops (For loops)
- [ ] Habang loops (While loops)
- [ ] Makina (Functions)

# Installation

### Prerequisites
- Python3.x

Clone the TagaLang repository in your local machine to get started. (TagaLang is not in Pip yet.)
```bash
git clone git@github.com:jabezborja/Pinoice.git
```

After that, you can now start coding with TagaLang.

Try to run the file you want.
```bash
py pin.py <file-name>
```

To test it out, run the `program.tag` first
```bash
py pin.py program.tag
```

And it should interpret the program.

# How To Use
> There is no Functions, If-else, and loops yet.

### Variables
Variables in TagaLang are called Baryabols (well, because it is tagalog.) It works like Javascript at some point where
you can declare a variable with no specific type of declare with specific type.

Types in Tagalang are not different in other languages, just the syntax.
```
String -> letra
Integer -> numero
Boolean -> ano
Any -> kahitano
```

You can declare a variable with just this:
```
baryabol name: "Nice"
```

If you want to declare a specific type for the variable, you can:
```
baryabol<letra> name: "Nice"
```

If the type is not agreed with the expression then it will throw an error.

To test it out, you can print it with `ipahayag`.

### Ipahayag
Ipahayag is like `print()` in Python. Just simple.

To print a string or letra
```
ipahayag("Nice")
```

To print a variable
```
ipahayag(variable_name)
```

or

```
ipahayag("Ako ay " + name)