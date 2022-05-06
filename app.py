from flask import Flask, render_template, request
import sqlite3
import datetime as dt
import json
import sys

#Global variables
app = Flask(__name__)

#User defined Functions
@app.route("/enquiry", methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/enquiry/submit', methods=['POST'])
def predict():
    FirstName = request.form['firstname']
    print(FirstName)
    LastName = request.form['lastname']
    FatherName = request.form['fathername']
    Email = request.form['Email']
    ContactNumber = request.form['contactnumber']
    Gender= request.form["gender"]
    Address = request.form['address']
    City = request.form['city']
    State = request.form['state']
    Institute = request.form['institute']
    Courses = request.form['courses']
    Year = request.form['year']
    CoursesTwo = request.form['listcourses']
    Reference = request.form['reference']
    # EntryDate = request.form['entrydate']
    o_date = dt.datetime.now()
    data = str(o_date).split(" ")[0].split("-")
    format_date = f"{data[2]}/{data[1]}/{data[0]}"
    EntryDate=(format_date)
    list = (FirstName,LastName,FatherName,Email,ContactNumber,Gender,Address,City,State,Institute,Courses,Year,CoursesTwo,Reference,EntryDate)
    print(list)
    try:
        con = sqlite3.connect('newdata.db')
        cur = con.cursor()
        mysql_query = """INSERT INTO studentsdata (fistname ,lastname ,fathername ,email , contactnumber,gender ,address ,city ,state,collagename ,course ,year ,listcourses ,reference,date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """
        values = list
        # cursor = connection.cursor()
        cur.execute(mysql_query, values)

        con.commit()
        print('Success')
        con.close()
        print("Success", "Record has been inserted")
    except Exception as e:
        print("Data Not Insert ", "Record Not Insert")
    print(list)
    return render_template('thankyou.html')

@app.route('/admin', methods=['GET'])
def Admin():
    return render_template('index1.html')


@app.route('/admin/dashboard', methods=['GET'])
def admin():
    con = sqlite3.connect('newdata.db')
    cursor = con.cursor()
    cursor.execute("select * from studentsdata ORDER BY id DESC")
    row_headers = [x[0] for x in cursor.description]
    results = cursor.fetchall()
    print(results)
    json_data = []
    for r in results:
        json_data.append(dict(zip(row_headers,r)))

    return render_template('index2.html', records=json_data, colnames=row_headers)
    # for result in results:
    #     json_data.append(dict(zip(row_headers,result)))
    #     print(json_data)
    #
    # sys.stdout = open('./static/js/declare.js','w')
    #
    # jsonobj = json.dumps(json_data)
    # return render_template('index2.html')
    #return render_template( "index2.html" , data = data )
    # for r in results:
    #     print(r)
    #     return render_template('index2.html',row0= r[0],row1=r[1],row2=r[2],row3=r[3],row4=r[4],row5=r[5],row6=r[6],row7=r[7],row8=r[8],row9=r[9],row10=r[10],row11=r[11],row12=r[12],row13=r[13],row14=r[14])

#Main function
if __name__== "__main__":
    app.run(debug=True)


