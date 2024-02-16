from rock_relperm_class import*

Austin_chalk= Rock("chalk", 0.38, 50)

Austin_chalk.add_LET(2, 3, 4, 2, 3, 4)

print(Austin_chalk.LET.Swir)

Austin_chalk.print_properties()

Austin_chalk.LET.plotLET()