from enum import Enum

class Operation(Enum):
    BUY = 0
    SELL = 1


class Ticket():

    def __init__(self, unit_cost: float, quantity: int, operation: Operation, tax: float):
        self.unit_cost = unit_cost
        self.quantity = quantity
        self.operation = operation
        self.tax = tax
    

    def set_tax(self, tax: float) -> None:
        self.tax = tax

    def get_tax(self) -> float:
        return self.tax
    
    def set_unit_cost(self, unit_cost: float) -> None:
        self.unit_cost = unit_cost

    def get_unit_cost(self) -> float:
        return self.unit_cost
    
    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity

    def get_quantity(self) -> int:
        return self.quantity
    
    def calculate_total_value(self)-> float:
        return self.unit_cost * self.quantity

    def calculate_value_with_tax(self)-> float:
        return self.unit_cost * self.quantity * (1 - self.tax)

    def print(self) -> str:
        return f"unit_cost: {self.unit_cost}, Quantity: {self.quantity}, Tax: {self.tax}"



import json

class Calculate():
    ticketsArr = []
    accumulatedLoss = 0
    accumulatedBuyQuantity = 0
    averageCost = 0
    totalValue = 0

    result = []

    def __init__(self, tax: float):
        self.tax = tax
        inputJSON = '''[
                {"operation": "buy", "unitCost": 10.00, "quantity": 10000},
                {"operation": "sell", "unitCost": 5.00, "quantity": 5000},
                {"operation": "sell", "unitCost": 15.00, "quantity": 2000},
                {"operation": "sell", "unitCost": 20.00, "quantity": 2000}
            ]'''

        jsonObj = json.loads(inputJSON)

        for item in jsonObj:
            self.ticketsArr.append(Ticket(item['unitCost'], item['quantity'], operation=Operation.SELL if item['operation'] == 'sell' else Operation.BUY, tax=0.05 if item['operation'] == 'sell' else 0.0))

        print(self.ticketsArr[0].print())

        for ticket in self.ticketsArr:
            if ticket.operation == Operation.BUY:
                print("Buying...")
                self.accumulatedBuyQuantity += self.accumulatedBuyQuantity + ticket.quantity
                self.totalValue = self.totalValue + ticket.calculate_current_total_value()
                self.averageCost = (self.averageCost*self.accumulatedBuyQuantity + ticket.get_unit_cost()*ticket.get_quantity()) / (self.accumulatedBuyQuantity() + ticket.get_quantity())
                self.result.append(0)
            
            elif ticket.operation == Operation.SELL:
                print("Selling...")
                
                if(ticket.get_unit_cost() < self.averageCost): # Prejuizo
                    self.accumulatedLoss += (ticket.get_unit_cost() - self.averageCost) * ticket.get_quantity()
                    self.result.append(0)
                    continue # PULA AO PROXIMO TICKET

                if ticket.calculate_total_value() < 20000:
                    # VENDA ISENTA
                    self.result.append(0)
                else:
                    # PAGAR IMPOSTO
                    profit = (self.averageCost - ticket.get_unit_cost()) * ticket.get_quantity()
                    
                    if(profit > 0):
                    # HOUVE ALGUM LUCRO
                        self.accumulatedLoss = self.accumulatedLoss - profit
                        


    def get_result(self) -> list[int]:
        return self.result    
    
calc = Calculate()
print(calc.get_result())