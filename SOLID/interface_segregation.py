# ISP
# instead of having one large interface
# with several members keep the interface granular
# -> split it into the smallest possible parts, so that
# people don't have to implement more than they need to


class Machine:
    def print(self, doc):
        self.doc = doc
        raise NotImplementedError()

    def scan(self, doc):
        raise NotImplementedError()

    def fax(self, doc):
        raise NotImplementedError()


# the base class machine works for this specific MuFuMa
class MultiFunctionMachine(Machine):
    def print(self, doc):
        pass

    def fax(self, doc):
        pass

    def scan(self, doc):
        pass


# but not for the standard printer -> it can neither fax nor scan
class Printer(Machine):
    def print(self, doc):
        # that works
        pass

    def fax(self, doc):
        # Printer cannot fax
        raise NotImplementedError("Printer cannot fax!")

    def scan(self, doc):
        # Printer cannot scan
        raise NotImplementedError("Printer cannot scan!")


# better -> follow the YAGNI approach (You Aren't Gonna Need It!)
# you can use @abstractmethod's to ensure that all the methods from the base
# class have to be overridden/implemented


class Printer:
    @abstractmethod
    def printout(self, doc):
        pass


class Scanner:
    @abstractmethod
    def scan(self, doc):
        pass


class Photocopier(Printer, Scanner):
    def printout(self, doc):
        print(doc)

    def scan(self, doc):
        scan(doc)


# another idea is to use them as individual attributes like so


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def printout(self, doc):
        pass

    @abstractmethod
    def scan(self, doc):
        pass


class MultiFunctionPrinter(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def printout(self, doc):
        self.printer.printout(doc)

    def scan(self, doc):
        self.scanner.scan(doc)
