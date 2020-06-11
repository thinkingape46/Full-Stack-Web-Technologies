from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/thankyou')
def thankyou():
    user_name = request.args.get('un')

    if user_name.islower():
        is_lower = 'fail'
    else:
        is_lower = 'pass'

    if user_name.isupper():
        is_upper = 'fail'
    else:
        is_upper = 'pass'

    if user_name[-1] in str(list(range(0,10))):
        int_check = 'pass'
    else:
        int_check = 'fail'

    return render_template('username_check.html', l_check=is_lower, u_check=is_upper, is_int=int_check, un=user_name)

if __name__ == '__main__':
    app.run(debug=True)
