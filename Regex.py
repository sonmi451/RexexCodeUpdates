import re

regexSetValue = re.compile(r'(.*[A-Za-z0-9_][.])(([A-Za-z0-9_]+)[(][)])(.setValue.*[;])')
regexRowInGrid = re.compile(r'(.*[A-Za-z0-9_][.])(([A-Za-z0-9_]+)[(][)])(.markActiveRow.*[;])')
regexTabActivate = re.compile(r'(.*[A-Za-z0-9_][.])(([A-Za-z0-9_]+)[(][)])(.activate.*[;])')
regexQuickfilter = re.compile(r'(.*[A-Za-z0-9_][.])((QuickFilter)[(][)])(.ApplyFilterForTaskRecorder.*[;])')

startBrace, countup = 0, 0

with open('TestUpdate.txt', 'w') as out:
    with open('Test.txt') as readIn:
        for line in readIn:
            if re.search(regexSetValue, line):
                SetValueToEdit = re.search(regexSetValue, line)
                replace = str("getStringEdit(\""+ SetValueToEdit.group(3) +"\")")
                newMethod = (SetValueToEdit.group(1) + replace + SetValueToEdit.group(4))
                print("Found old form adaptor " + replace)
                print("replace with new method ",newMethod)
                out.write(newMethod)
            if re.search(regexRowInGrid, line):
                RowInGridToEdit = re.search(regexRowInGrid, line)
                replace = str("getStringEdit(\""+ RowInGridToEdit.group(3) +"\")")
                newMethod = (RowInGridToEdit.group(1) + replace + RowInGridToEdit.group(4))
                print("Found old form adaptor " + replace)
                print("replace with new method ",newMethod)
                out.write(newMethod)
            #Tab activate
            if re.search(regexClickButton, line):
                TabActivateToEdit = re.search(regexClickButton, line)
                replace = str("getTabPage(\""+ TabActivateToEdit.group(3) +"\")")
                newMethod = (TabActivateToEdit.group(1) + replace + TabActivateToEdit.group(4))
                print("Found old form adaptor " + replace)
                print("replace with new method ", newMethod)
                out.write(newMethod)
            #Quickfilter
            if re.search(regexQuickfilter, line):
                QuickfilterToEdit = re.search(regexQuickfilter, line)
                replace = str("getQuickFilter(\""+ QuickfilterToEdit.group(3) +"\")")
                newMethod = (QuickfilterToEdit.group(1) + replace + QuickfilterToEdit.group(4))
                print("Found old form adaptor " + replace)
                print("replace with new method ",newMethod)
                out.write(newMethod)
            else:
                out.write(line)
