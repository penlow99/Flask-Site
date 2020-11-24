 
from flask import Flask, render_template, url_for, redirect


############################
### Initialize flask app ###
############################
app = Flask(__name__)


##############
### ROUTES ###
##############
@app.route('/')
def go_home():
    return redirect('/index')
#-----------------------------------------------------------------
@app.route('/index')
def index():
    return render_template('index.html', title="Patrick's Place")
#-----------------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    formObj = LoginForm()
    if formObj.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            formObj.username.data, formObj.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', user=user, form=formObj)
#-----------------------------------------------------------------

# app import check
if __name__ == '__main__':
    app.run()