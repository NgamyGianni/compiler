f = open("test.txt", "r")

specialChars = {
    'newLine' : {'regRule' : '/\r\n/g', 'value' :'\n'},
    'case' : {'regRule' : '/case/g', 'value' :'case'},
    # endInstruct:    {regRule: /;/g,  value:';'},
    # equal:          {regRule: /=/g, value:'='},
    # point:           {regRule: /\./g, value:'.'},
    # virgule:           {regRule: /\,/g, value:','},
    # quotationMark:  {regRule: /\"/g, value:'"'},
    # openParenthese:  {regRule: /\(/g, value:'"'},
    # closeParenthese:  {regRule: /\)/g, value:'"'}
}

def hello():
    print("yoyoyo")
    print(specialChars['case']['regRule'])

hello()
