#!C:/Users/vaish/AppData/Local/Programs/Python/Python311/python.exe
import cgi
import cgitb
import os
import pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="wheel")
cur = con.cursor()
form = cgi.FieldStorage()

print("Content-Type: text/html\r\n\r\n")
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FORMS</title>
    <style>
        *{
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande'
            , 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        }
        h1{
            text-align: center;
            font-weight: 700;
            font-size: 50px;
        }
        h2{
            text-align: center;
            font-weight: 500;
            font-size: 30px;
            color: #5e5b5b;
        }
        .form{
            height: 80%;
            width: 100%;
            display: flex;
            justify-content: space-evenly;
        }
        .fm{
            color: rgb(116, 116, 0);
            gap: 8px;
        }
        button{
            padding-top: 5px;
            margin: 18px 20px;
            border: 2px solid olive;
            border-radius: 5px;
            color: aliceblue;
            background-color: black;
        }
        #reset{
            padding-top: 5px;
            margin: 18px 20px;
            border: 2px solid olive;
            border-radius: 5px;
            color: aliceblue;
            background-color: black;
        }
        #log{
            color: rgb(123, 18, 18);
        }
        a{
            color: rgb(0, 0, 0)
        }
    </style>
</head>
<body bgcolor="#F8F4E1">
    <h1>FORMS</h1>
    <h2>Registration / Log-in</h2>
    <div class="form">
        <fieldset>
            <legend>Register</legend>
        <form action="" class="fm" method="post" enctype="multipart/form-data">
            <label for="firstname">First Name</label>
            <input type="text" name="firstname" id="in1"><br><br>
            <label for="lastname">Last Name</label>
            <input type="text" name="lastname" id="in1"><br><br>
            <label for="pass">Create Password</label>
            <input type="password" name="pwd" id="in1"><br><br>
            <label for="pass">Confirm Password</label>
            <input type="password" name="cpd" id="in1"><br><br>
            <label for="Phone">Phone</label>
            <input type="number" name="phone" id="in1"><br><br>
            <label for="email">Email</label>
            <input type="email" name="email" id="in1"><br><br>
            <p>Country</p>
            <select name="country" id="sel">
                <option value="" disabled selected>--select--</option>
                <optgroup label="Country">
                <option value="India">India</option>
                <option value="Canada">Canada</option>
                <option value="USA">USA</option>
                <option value="New Zealand">New Zealand</option>
                <option value="England">England</option>
            </optgroup>
            </select>
            <p>City</p>
            <input type="text" required name="city"><br><br>
            <p>Address</p>
            <textarea name="address" id="txt" rows="5" cols="30"></textarea>
            <p>Upload file</p>
            <input type="file" id="myfile" name="photo">
            <div class="end">
                <input type="submit" id="btn" name="submit">
                <input type="reset" id="reset">
                <p id="log">Click here to <a href="log.html" target="_blank">Log-in</a>
                </p>
            </div>
        </form>
    </fieldset>
    </div>
</body>
<script>
    function register(){
        let b = document.getElementById('in1').value;
        if(b == ""){
            alert("Fill the required fields");
        }
        else{
            alert("Successfully registered");
        }
    }
</script>
</html>
''')
submit = form.getvalue("submit")

if submit != None:
    if len(form) != 0:
        firstname = form.getvalue("firstname")
        lastname = form.getvalue("lastname")
        pwd = form.getvalue("pwd")
        cpd = form.getvalue("cpd")
        phone = form.getvalue("phone")
        email = form.getvalue("email")
        country = form.getvalue("country")
        city = form.getvalue("city")
        address = form.getvalue("address")
        photo = form['photo']

        if photo.filename:
            photo_filename = os.path.basename(photo.filename)
            open("Database/" + photo_filename, "wb").write(photo.file.read())
            phtf = '''insert into imgreg(firstname, lastname, pwd, cpd, phone, email, country, city, address, 
            photo)  values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' % (
                firstname, lastname, pwd, cpd, phone, email, country, city, address, photo_filename)
            cur.execute(phtf)
            con.commit()
            print('''<script> alert("Register Successfully"); </script>''')
    con.close()
