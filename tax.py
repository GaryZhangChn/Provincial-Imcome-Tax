from abc import abstractmethod, ABCMeta


class GetTax():
    def __init__(self):
        self.__tax = None
        self.__income = None
        self.__stage1 = None
        self.__rate1 = None
        self.__stage2 = None
        self.__rate2 = None
        self.__stage3 = None
        self.__rate3 = None
        self.__stage4 = None
        self.__rate4 = None
        self.__stage5 = None
        self.__rate5 = None
        self.__stage6 = None
        self.__rate6 = None

    def setStage(self, stage1, stage2, stage3, stage4=999999.9, stage5=999999.9, stage6=999999.9):

        self.__stage1 = stage1
        self.__stage2 = stage2
        self.__stage3 = stage3
        self.__stage4 = stage4
        self.__stage5 = stage5
        self.__stage6 = stage6

    def setRate(self, rate1, rate2, rate3, rate4=99.9, rate5=99.9, rate6=99.9):

        self.__rate1 = rate1
        self.__rate2 = rate2
        self.__rate3 = rate3
        self.__rate4 = rate4
        self.__rate5 = rate5
        self.__rate6 = rate6

    def enterIncome(self, income):
        self.__income = int(income)
        pass

    def calcTax(self):
        full_stage1_tax = self.__stage1 * self.__rate1
        full_stage2_tax = self.__stage2 * self.__rate2
        full_stage3_tax = self.__stage3 * self.__rate3
        full_stage4_tax = self.__stage4 * self.__rate4
        full_stage5_tax = self.__stage5 * self.__rate5
        if self.__income <= self.__stage1:
            self.__tax = self.__income * self.__rate1
        elif self.__income <= (self.__stage1 + self.__stage2):
            stage2tax = (self.__income - self.__stage1) * self.__rate2
            self.__tax = stage2tax + full_stage1_tax
        elif self.__income <= (self.__stage1 + self.__stage2 + self.__stage3):
            stage3tax = (self.__income - self.__stage2 - self.__stage1) * self.__rate3
            # print('Stage 3 is %.2f' % stage3tax)
            self.__tax = stage3tax + full_stage1_tax + full_stage2_tax
        elif self.__income <= (self.__stage1 + self.__stage2 + self.__stage3 + self.__stage4):
            stage4tax = (self.__income - self.__stage3 - self.__stage2 - self.__stage1) * self.__rate4
            # print('Stage 4 is %.2f' % stage4tax)
            self.__tax = stage4tax + full_stage1_tax + full_stage2_tax + full_stage3_tax
        elif self.__income <= self.__stage5:
            stage5tax = (self.__income - self.__stage4 - self.__stage3 - self.__stage2 - self.__stage1) * self.__rate5
            print('Stage 5 is %.2f' % stage5tax)
            self.__tax = stage5tax + full_stage1_tax + full_stage2_tax + full_stage3_tax + full_stage4_tax
        elif self.__income < self.__stage6:
            stage6tax = (self.__income - self.__stage5 - self.__stage4 - self.__stage3 - self.__stage2 - self.__stage1) * self.__rate6
            print('Stage 6 is %.2f' % stage6tax)
            self.__tax = stage6tax + full_stage1_tax + full_stage2_tax + full_stage3_tax + full_stage4_tax + full_stage5_tax
        return self.__tax


class TaxFactory(metaclass=ABCMeta):
    def __init__(self):
        self.__stage1 = None
        self.__stage2 = None
        self.__stage3 = None
        self.__rate1 = None
        self.__rate2 = None
        self.__rate3 = None
        self.__rate4 = None
        self.__rate5 = None
        self.__rate6 = None
        self.__tax = None

    @abstractmethod
    def set_income(self, income):
        pass

    @abstractmethod
    def get_tax(self):
        pass


class TaxNL(TaxFactory):
    def __init__(self):
        super().__init__()
        self.__stage1 = 37929
        self.__rate1 = 0.087
        self.__stage2 = 37929
        self.__rate2 = 0.145
        self.__stage3 = 59574
        self.__rate3 = 0.158
        self.__stage4 = 54172
        self.__rate4 = 0.173
        self.__stage5 = 189604
        self.__rate5 = 0.183
        self.__rate6 = 0.183
        self.__tax = GetTax()
        self.__tax.setStage(self.__stage1, self.__stage2, self.__stage3, self.__stage4, self.__stage5)
        self.__tax.setRate(self.__rate1, self.__rate2, self.__rate3, self.__rate4, self.__rate5, self.__rate6)

    def set_income(self, income):
        self.__tax.enterIncome(income)
        pass

    def get_tax(self):
        tax = self.__tax.calcTax()
        return tax


class TaxPE(TaxFactory):
    def __init__(self):
        super().__init__()
        self.__stage1 = 31984
        self.__rate1 = 0.098
        self.__stage2 = 31985
        self.__rate2 = 0.138
        self.__stage3 = 63969
        self.__rate3 = 0.167
        self.__rate4 = 0.167
        self.__rate5 = 0.167
        self.__rate6 = 0.167

        self.__tax = GetTax()
        self.__tax.setStage(self.__stage1, self.__stage2, self.__stage3)
        self.__tax.setRate(self.__rate1, self.__rate2, self.__rate3, self.__rate4, self.__rate5, self.__rate6)

    def set_income(self, income):
        self.__tax.enterIncome(income)
        pass

    def get_tax(self):
        tax = self.__tax.calcTax()
        return tax


class TaxNS(TaxFactory):
    def __init__(self):
        super().__init__()
        self.__stage1 = 29590
        self.__rate1 = 0.0879
        self.__stage2 = 29590
        self.__rate2 = 0.1495
        self.__stage3 = 33820
        self.__rate3 = 0.1667
        self.__stage4 = 57000
        self.__rate4 = 0.175
        self.__stage5 = 150000
        self.__rate5 = 0.21
        self.__rate6 = 0.21
        self.__tax = GetTax()
        self.__tax.setStage(self.__stage1, self.__stage2, self.__stage3, self.__stage4, self.__stage5)
        self.__tax.setRate(self.__rate1, self.__rate2, self.__rate3, self.__rate4, self.__rate5, self.__rate6)

    def set_income(self, income):
        self.__tax.enterIncome(income)
        pass

    def get_tax(self):
        tax = self.__tax.calcTax()
        return tax


class TaxNB(TaxFactory):
    def __init__(self):
        super().__init__()
        self.__stage1 = 43401
        self.__rate1 = 0.0968
        self.__stage2 = 43402
        self.__rate2 = 0.1482
        self.__stage3 = 54319
        self.__rate3 = 0.1652
        self.__stage4 = 19654
        self.__rate4 = 0.1784
        self.__stage5 = 160776
        self.__rate5 = 0.203
        self.__rate6 = 0.203
        self.__tax = GetTax()
        self.__tax.setStage(self.__stage1, self.__stage2, self.__stage3, self.__stage4, self.__stage5)
        self.__tax.setRate(self.__rate1, self.__rate2, self.__rate3, self.__rate4, self.__rate5, self.__rate6)

    def set_income(self, income):
        self.__tax.enterIncome(income)
        pass

    def get_tax(self):
        tax = self.__tax.calcTax()
        return tax


class TaxQC(TaxFactory):
    def __init__(self):
        super().__init__()
        self.__stage1 = 44545
        self.__rate1 = 0.15
        self.__stage2 = 44535
        self.__rate2 = 0.2
        self.__stage3 = 19310
        self.__rate3 = 0.24
        self.__stage4 = 108390
        self.__rate4 = 0.2575
        self.__rate5 = 0.2575
        self.__rate6 = 0.2575
        self.__tax = GetTax()
        self.__tax.setStage(self.__stage1, self.__stage2, self.__stage3, self.__stage4)
        self.__tax.setRate(self.__rate1, self.__rate2, self.__rate3, self.__rate4, self.__rate5, self.__rate6)

    def set_income(self, income):
        self.__tax.enterIncome(income)
        pass

    def get_tax(self):
        tax = self.__tax.calcTax()
        return tax


class TaxON(TaxFactory):
    def __init__(self):
        super().__init__()
        self.__stage1 = 44740
        self.__rate1 = 0.0505
        self.__stage2 = 44742
        self.__rate2 = 0.0915
        self.__stage3 = 60518
        self.__rate3 = 0.1116
        self.__stage4 = 70000
        self.__rate4 = 0.1216
        self.__stage5 = 220000
        self.__rate5 = 0.1316
        self.__rate6 = 0.1316
        self.__tax = GetTax()
        self.__tax.setStage(self.__stage1, self.__stage2, self.__stage3, self.__stage4, self.__stage5)
        self.__tax.setRate(self.__rate1, self.__rate2, self.__rate3, self.__rate4, self.__rate5, self.__rate6)

    def set_income(self, income):
        self.__tax.enterIncome(income)
        pass

    def get_tax(self):
        tax = self.__tax.calcTax()
        return tax


class TaxMB(TaxFactory):
    def __init__(self):
        super().__init__()
        self.__stage1 = 33389
        self.__rate1 = 0.108
        self.__stage2 = 38775
        self.__rate2 = 0.1275
        self.__stage3 = 72164
        self.__rate3 = 0.174
        self.__rate4 = 0.174
        self.__rate5 = 0.174
        self.__rate6 = 0.174

        self.__tax = GetTax()
        self.__tax.setStage(self.__stage1, self.__stage2, self.__stage3)
        self.__tax.setRate(self.__rate1, self.__rate2, self.__rate3, self.__rate4, self.__rate5, self.__rate6)

    def set_income(self, income):
        self.__tax.enterIncome(income)
        pass

    def get_tax(self):
        tax = self.__tax.calcTax()
        return tax


class TaxSK(TaxFactory):
    def __init__(self):
        super().__init__()
        self.__stage1 = 45225
        self.__rate1 = 0.105
        self.__stage2 = 83989
        self.__rate2 = 0.125
        self.__stage3 = 129214
        self.__rate3 = 0.145
        self.__rate4 = 0.145
        self.__rate5 = 0.145
        self.__rate6 = 0.145

        self.__tax = GetTax()
        self.__tax.setStage(self.__stage1, self.__stage2, self.__stage3)
        self.__tax.setRate(self.__rate1, self.__rate2, self.__rate3, self.__rate4, self.__rate5, self.__rate6)

    def set_income(self, income):
        self.__tax.enterIncome(income)
        pass

    def get_tax(self):
        tax = self.__tax.calcTax()
        return tax


class TaxAB(TaxFactory):
    def __init__(self):
        super().__init__()
        self.__stage1 = 131220
        self.__rate1 = 0.1
        self.__stage2 = 26244
        self.__rate2 = 0.12
        self.__stage3 = 52488
        self.__rate3 = 0.13
        self.__stage4 = 104976
        self.__rate4 = 0.14
        self.__stage5 = 314928
        self.__rate5 = 0.15
        self.__rate6 = 0.15
        self.__tax = GetTax()
        self.__tax.setStage(self.__stage1, self.__stage2, self.__stage3, self.__stage4, self.__stage5)
        self.__tax.setRate(self.__rate1, self.__rate2, self.__rate3, self.__rate4, self.__rate5, self.__rate6)

    def set_income(self, income):
        self.__tax.enterIncome(income)
        pass

    def get_tax(self):
        tax = self.__tax.calcTax()
        return tax


class TaxBC(TaxFactory):
    def __init__(self):
        super().__init__()
        self.__stage1 = 41725
        self.__rate1 = 0.0506
        self.__stage2 = 41726
        self.__rate2 = 0.077
        self.__stage3 = 12361
        self.__rate3 = 0.105
        self.__stage4 = 20532
        self.__rate4 = 0.1229
        self.__stage5 = 41404
        self.__rate5 = 0.147
        self.__rate6 = 0.168
        self.__tax = GetTax()
        self.__tax.setStage(self.__stage1, self.__stage2, self.__stage3, self.__stage4, self.__stage5)
        self.__tax.setRate(self.__rate1, self.__rate2, self.__rate3, self.__rate4, self.__rate5, self.__rate6)

    def set_income(self, income):
        self.__tax.enterIncome(income)
        pass

    def get_tax(self):
        tax = self.__tax.calcTax()
        return tax
