from flask import Flask #, request, render_templates

app = Flask(__name__)
DEBUG = True

@app.route('/')
def contribution():
    #if request.method == 'POST':
    onyi = input("")
    x = {'Q': 'OCTOBER', 'O': 'NOVEMBER', 
        'P': 'DECEMBER', 'M': 'JANUARY', 'N': 'MARCH', 'R' : 'FEBRUARY', 'S' : 'APRIL'}
    if onyi == 'M':
        print(x['M'])
    elif onyi == 'O':
        print(x['O'])
    elif onyi == 'N':
        print(x['N'])
    elif onyi == 'Q':
        print(x['Q'])
    elif onyi == 'P':
        print(x['P'])
    elif onyi == 'R':
        print(x['R'])
    elif onyi == 'S':
        print(x['S'])
    else:
        print('not applicable')
    return (contribution())


if __name__ == '__main__':
     app.run(debug=True)

