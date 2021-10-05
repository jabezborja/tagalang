# Pinoice - A Tagalog Programming Language
Pinoice is a rooftop-level tagalog-based syntax yet-procedural cautiously interpreted programming language where Filipino programmers can play with. 

It is in the top of Python which is a high-level also so Pinoice is considered as the 'rooftop-level' programming language. It's design is for readability for Filipinos to understand how programming languages really works in their native language. With that being said, I will try my best to make the grammar more Tagalog.

> The reason why Pinoice is made from scratch is to make the language allow more grammar to use and more easy to read as it will use more Filipino grammar (Hopefully it can.)

## Example
```
baryabol na letra pangalan ay itala ang "pangalan? "
baryabol na numero edad ay itala ang "edad? "

ipahayag ang "Si " + pangalan + " ay " + edad + " na taong gulang"
```

### Equivalent to
```python
# Python
pangalan = input("pangalan? ") 
edad = input("edad? ")

print("Si " + pangalan + " ay " + edad + " na taong gulang")
```

## Todos
- [x] Lexer
- [x] Parser
    - [ ] AST
- [x] Baryabols (Baryabols doesn't use ASTs yet, but Ops works and I'm planning to rewrite the entire implementation.)
    - [x] Baryabol types
    - [x] Assign
- [x] Builtins
    - [x] Ipahayag (print function)
    - [x] Itala (input function)
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
Array -> hanay
None or Null -> Wala
Any -> kahitano
```

You can declare a variable with just this:
```
baryabol name ay "Nice"
```

If you want to declare a specific type for the variable, you can:
```
baryabol na letra name ay "Nice"
```

If the type is not agreed with the expression then it will throw an error.

To test it out, you can print it with `ipahayag`.

### Ipahayag
Ipahayag is like `print()` in Python. Just simple.

To print a string or letra
```
ipahayag ang "Nice"
```

To print a variable
```
ipahayag ang variable_name
```

or

```
ipahayag ang "Ako si " + name
```

# Changelog
*Oct 2, 2021*
- Ipahayag (print)
- Itala (input)
- Better exceptions
- Code docs

*Oct 2, 2021*
- Redesign the language

*Oct 1, 2021*
- Baryabol callers (They can now call each other)
- Better errors
- Ready the Repo template structure for PyPi submission
- Process timer

*Sept 30, 2021*
- Rewrote the entire language
- Lexer
- Parser
- Baryabols (Variables)
- Baryabols types (Letra (string), Numero (integer), Ano (Boolean), KahitAno (Any))

*Sept 28, 2021*
- Recontinue of the Project as Pinoice

*Sept, 2020*
- Start of the Project as TagaLag
- No Lexers or Parsers, just poor old creaky language. Scanning method.
