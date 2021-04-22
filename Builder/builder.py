# When piece-wise construction of an object is complicated
# a builder provides an API for doing it succinctly


class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def _str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            j = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{j}{self.text}")

        for element in self.elements:
            lines.append(element._str(indent + 1))

        lines.append(f"{i}</{self.name}>")

        return "\n".join(lines)

    def __str__(self):
        return self._str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

    def __str__(self):
        return str(self.__root)


builder = HtmlElement.create("ul")
builder.add_child("li", "this is the first element").add_child(
    "li", "this is the second element"
).add_child("li", "this is the third element")


print(f"Builder: {builder}")
