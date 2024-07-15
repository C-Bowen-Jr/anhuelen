import anhuelen as anh

# Test init, titles and to_lower()
print("Titles")
underline = anh.Anhuelen()
underline.title("Underline")

bold = anh.Anhuelen("BOLD")
bold.title("Bold")

red = anh.Anhuelen("red")
red.title("Red")

green = anh.Anhuelen("GREen")
green.title("Green")

yellow = anh.Anhuelen("yeLLOw")
yellow.title("Yellow")

blue = anh.Anhuelen("Blue")
blue.title("Blue")

magenta = anh.Anhuelen("magentA")
magenta.title("Magenta")

cyan = anh.Anhuelen("cyan")
cyan.title("Cyan")


# Body tests
cyan.inform("FORMality","Just FYI")
cyan.inform("This one isn't practical")
cyan.prompt("Option","Suggestion")
cyan.prompt("Try hitting [Enter]", "To get this")
cyan.prompt("Type a few letters then [Enter]","This is long, but it won't get left behind")
cyan.prompt("On your own answering this one")
