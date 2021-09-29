# TagaLang - A Tagalog Programming Language
A tagalog-based syntax programming language where Filipino programmers can play with. TagaLang is based on Python3 Programming Language.

## Example
```
baryabol<letra> pangalan = "Jabez"
baryabol<numero> edad = 17

ipahayag("Si " + pangalan + " ay " + edad + " taong gulang")
```

### Equivalent to
```java
// Java
String pangalan = "Jabez";
int edad = 17

System.out.println("Si " + pangalan + " ay " + edad + " taong gulang")
```
```python
# Python
pangalan: str = "Jabez" 
edad: int = 17

print("Si " + pangalan + " ay " + edad + " taong gulang")
```

# Installation

### Prerequisites
- Python3.x

Clone the TagaLang repository in your local machine to get started. (TagaLang is not in Pip yet.)
```bash
git clone git@github.com:jabezborja/TagaLang.git
```

After that, you can now start coding with TagaLang.

Try to run the file you want.
```bash
py tag.py <file-name>
```

To test it out, run the `program.tag` first
```bash
py tag.py program.tag
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
Boolean -> OoAtHindi
```

You can declare a variable with just this:
```
baryabol name = "Nice"
```

If you want to declare a specific type for the variable, you can:
```
baryabol<letra> name = "Nice"
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
