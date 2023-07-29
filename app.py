from flask import Flask,request,render_template


app=Flask(__name__)


@app.route('/')
def welcome():
    return "welcome to Flask"

@app.route('/cal',methods=["Get"])
def math_operator():
    operation=request.json("operation")
    number1=request.jason("num1")
    number2=reuest.jason("num2")

    if operation=="add":
        result=number1+number2
    elif operation=="multiply":
        result=number1*number2
    elif operation=="division":
        result=number1/number2
    else:
        result=number1-number2
    return result   
print(__name__) 
if __name__=='__main__':
    app.run(debug=True)

            

if __name__ == '__main__':
    app.run()

