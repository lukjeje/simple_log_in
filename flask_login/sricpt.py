from flask import * 
import sqlite3  
  
app = Flask(__name__)
 
@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/singup')
def singup():
    return render_template('singup.html')

@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():
   try:   
    msg = "msg"  
    if request.method == "POST":  
            password = request.form["password"]  
            email = request.form["email"]        
            with sqlite3.connect("usersdb.db") as con:  
                  cur = con.cursor()   
                  cur.execute("INSERT into UsersDB (email, password) values (?,?)",(email, password))
                  con.commit()  
                  msg = "user successfully Added"
                  return redirect('')   
   except:  
       con.rollback()  
       msg = "email alredy existing"
       return render_template("singup.html", msg=msg)            
  

@app.route("/view")  
def view():  
    con = sqlite3.connect("usersdb.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from UsersDB")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  

@app.route("/ceckdetals",methods = ["POST","GET"])
def ceckdetals():
    email = request.form["email"]
    password = request.form["password"]
    info = "can't login"
    con = sqlite3.connect("usersdb.db")
    cur = con.cursor()
    statement = f"SELECT email from UsersDB WHERE email='{email}' AND Password = '{password}';"
    cur.execute(statement)
    if not cur.fetchone():  # An empty result evaluates to False.
      return render_template('index.html', info=info)
    else:
      return render_template('usr.html', email=email)

@app.route("/delete")
def delete():
    return render_template('delate.html')

@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("usersdb.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from UsersDB where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delate.html",msg = msg)      

if __name__ =='__main__':  
    app.run(debug = True)  