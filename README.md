# Pinoice - A Tagalog Programming Language
Pinoice is a rooftop-level tagalog-based syntax yet-procedural cautiously interpreted programming language where Filipino programmers can play with. 

It is in the top of Python which is a high-level also so Pinoice is considered as the 'rooftop-level' programming language. It's design is for readability for Filipinos to understand how programming languages really works in their native language. With that being said, I will try my best to make the grammar more Tagalog.

> The reason why Pinoice is made from scratch is to make the language allow more grammar to use and more easy to read as it will use more Filipino grammar (Hopefully it can.)

## Example
```
@ Pinoice
baryabol operation_1 ay 2 + 5 * 5
baryabol operation_2 ay 3

@ Will print 30, Pinoice accurately follow the MDAS math.
ipahayag ang operation_1 + operation_2
```

### Equivalent to
```python
# Python
operation_1 = 2 + 5 * 5
operation_2 = 3

# Will print 30, Python accurately follow the MDAS math.
print(operation_1 + operation_2)
```

## Todos
- [x] Lexer
- [x] Parser
    - [x] Parse Tree (AST)
- [x] Baryabols
    - [x] AST Node
    - [x] Assign
    - [x] Access
    - [ ] Types
- [x] Builtins
    - [x] Ipahayag (print function)
        - [x] AST Node
        - [x] Interpreter Visitor
    - [ ] Itala (input function) _Currently on my stash_
        - [x] AST Node
        - [ ] Interpreter Visitor
- [x] Kung-Ibapa statements (If-else statements)
    - [x] Kung (If)
    - [ ] Ibapa (Else if)
    - [ ] Iba (Else)
- [x] Tukuyin (Functions)
- [ ] Bawat loops (For loops)
- [ ] Habang loops (While loops)

# Installation

### Prerequisites
- Python3.x

Clone the Pinoice repository in your local machine to get started. (Pinoice is not in Pip yet.)
```bash
git clone git@github.com:jabezborja/Pinoice.git
```

After that, you can now start coding with Pinoice.

But first, go to interpreter folder.

In windows:
```
cd interpreter
```

Then

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
> There is no Functions, and loops yet.

### Variables
Variables in Pinoice are called Baryabols (well, because it is tagalog).
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

### Kung Statements
Just like other languages, we have Kung statements too.

Kung statements works like Lua programming with 'THEN' and 'END'

But in Pinoice, it is 'TAPOS' and 'PAGTATAPOS'

To perform a kung statements
```
kung <condition> tapos
    ...
pagtatapos
```

Just basic as that. Let's try to make something with 'Kung Statements'
```
baryabol pangalan ay "Jabez"

kung pangalan ay "Jabez" tapos
    ipahayag ang "Kumusta, Jabez!"
pagtatapos
```

And it works like a charm. You can try it yourself!

# Changelog
*Oct 8, 2021*
- Kung statements (If statements)
- Tukuyin (Functions)

*Oct 5, 2021*
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
