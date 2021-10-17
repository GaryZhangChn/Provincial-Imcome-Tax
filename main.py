# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import tax
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

# def menu():

if __name__ == '__main__':
    incomeList = []
    for i in range(3, 11):
        income = i * 10000
        incomeList.append(income)
    family_NL = tax.TaxNL()
    family_PE = tax.TaxPE()
    family_NS = tax.TaxNS()
    family_NB = tax.TaxNB()
    family_QC = tax.TaxQC()
    family_ON = tax.TaxON()
    family_MB = tax.TaxMB()
    family_SK = tax.TaxSK()
    family_AB = tax.TaxAB()
    family_BC = tax.TaxBC()
    # family_YT = tax.TaxYT()
    # family_NT = tax.TaxNT()
    # family_NU = tax.TaxNU()
    # family_
    NL_data = []
    PE_data = []
    NS_data = []
    NB_data = []
    QC_data = []
    ON_data = []
    MB_data = []
    SK_data = []
    AB_data = []
    BC_data = []

    for i in incomeList:
        print(i)
        family_NL.set_income(i)
        family_PE.set_income(i)
        family_NS.set_income(i)
        family_NB.set_income(i)
        family_QC.set_income(i)
        family_ON.set_income(i)
        family_MB.set_income(i)
        family_SK.set_income(i)
        family_AB.set_income(i)
        family_BC.set_income(i)

        # individual data
        family_tax_NL = family_NL.get_tax()
        family_tax_PE = family_PE.get_tax()
        family_tax_NS = family_NS.get_tax()
        family_tax_NB = family_NB.get_tax()
        family_tax_QC = family_QC.get_tax()
        family_tax_ON = family_ON.get_tax()
        family_tax_MB = family_MB.get_tax()
        family_tax_SK = family_SK.get_tax()
        family_tax_AB = family_AB.get_tax()
        family_tax_BC = family_BC.get_tax()

        NL_data.append(family_tax_NL)
        PE_data.append(family_tax_PE)
        NS_data.append(family_tax_NS)
        NB_data.append(family_tax_NB)
        QC_data.append(family_tax_QC)
        ON_data.append(family_tax_ON)
        MB_data.append(family_tax_MB)
        SK_data.append(family_tax_SK)
        AB_data.append(family_tax_AB)
        BC_data.append(family_tax_BC)

    # FamilyIncome = np.array(incomeList)
    # NL = np.array(NL_data)
    plt.title("Provincial tax (Under 100k)")
    plt.xlabel("Taxable Income")
    plt.ylabel("Total Tax")
    plt.grid(axis='y')

    plt.plot(incomeList, NL_data,  label='NL')
    plt.plot(incomeList, PE_data, label='PEI')
    plt.plot(incomeList, NS_data,  label='NS')
    plt.plot(incomeList, NB_data,  label='NB')
    # plt.plot(incomeList, QC_data, '-o', label='QC')
    plt.plot(incomeList, ON_data, label='ON')
    plt.plot(incomeList, MB_data, label='MB')
    plt.plot(incomeList, SK_data, label='SK')
    plt.plot(incomeList, AB_data, label='AB')
    plt.plot(incomeList, BC_data, label='BC')
    plt.legend(bbox_to_anchor=(0., 0.7, 0.7, .102), loc='lower left',
               ncol=2, mode="expand", borderaxespad=0.)
    # plt.show()
    plt.savefig("Lowest Provincial Tax (under 100k).png", dpi=500)
