from currency_converter import CurrencyConverter

class Options:

    Converter_Access = CurrencyConverter()

    def TakeInput(self):
        try: 
            Take_Amount = int(input("Enter Amount of money: "))
            From_Convert = input("Enter your Currency: ")
            To_Convert = input("Enter the Currency you want to convert it to: ")
            res = self.Converter(Take_Amount, From_Convert, To_Convert)
            print(res)
        except ValueError:
            print("make sure to enter a proper number input or proper currency Conversion")
        finally:
            print("program finished executing")

    def Converter(self, Amount, From, To):
        result = round(self.Converter_Access.convert(Amount, From, To))    
        return result

Prototype_V1 = Options()

Prototype_V1.TakeInput()