# Anhuelen

Anhuelen (meaning 'take in') is a lightweight and simple prompting module. Think create-react-app or likewise. It handles the coloring, and you only really need 3 functions (excluding the constructor).

## Usage
Include ```anhuelen.py``` in your source directory. Then import and call the constructor.
```Python
import anhuelen 
# or for brevity
import anhuelen as anh

prompts = anhuelen.Anhuelen()
```

## Constructor Parameters
When calling ```anhuelen.Anhuelen()```, the default title will be set to _underline_, but **bold** is also an option. Alternatively, the basic ansi colors are here: Red, Green, Yellow, Blue, Magenta, Cyan. For readability, these are actually the "bright" variants. To add any of these options, just supply a string with one of those options.

```Python
prompts = anhuelen.Anhuelen("bold")
```

Types:
 - bold
 - underline
 - red
 - green
 - yellow
 - blue
 - magenta
 - cyan

Capitalization doesn't matter. Anything that doesn't match one of the above types gets converted to the RESET parameter (which is the default text color and format).

## Title
The title's purpose is just to properly name you prompts as a whole. That or otherwise inform the user what in reference to are they responding questions for. It is not actually needed. If that's the case, you don't need to provide parameter to the constructor. ```title()``` is just a fancy ```print()```.

```Python
prompts.title("Create REACT App")
```

## Inform
Inform is a type of ```print()```. It can be provided either 1 or 2 strings. The first is the question for the prompt. The second is the provided answer. Note: This is not for user input. Think of this as just an FYI to the user. Say an earlier choice locked them into a single option. 

```Python
prompts.inform("EULA Roofie","Consent")
```

## Propmpt
Prompt is a type of ```input()```. It can be provided either 1 or 2 strings. The first is the question for the prompt. The second is a suggested or default answer. The user can hit the "enter" key without typing anything to accept the default, or type a new response.

```Python
prompts.prompt("Favorite Drink","Coffee")
prompts.prompt("Album Title")
```

## Plans
Currently there is no input error handling. I intend to add a reprompt function to cleanly redo the line if you get invalid input from a user.