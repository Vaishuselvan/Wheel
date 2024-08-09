#!C:/Users/vaish/AppData/Local/Programs/Python/Python311/python.exe
import cgi
import cgitb
import pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="wheel")
cur = con.cursor()
form = cgi.FieldStorage()
print("content-type:text/html \r\n\r\n")
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>forms2</title>
    <style>
        *{
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, 
            sans-serif;
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
           /* text-decoration: none;*/
            color:rgb(0, 0, 0)
        }
    </style>
</head>
<body bgcolor="#F8F4E1">
    <h1>FORMS</h1>
    <h2>Log-in</h2>
    <div class="form">
        <form action="" class="fm"  method="post" enctype="multipart/form-data">
            <label for="username">UserName</label>
            <input type="text" name="username" id="in1" required><br><br>
            <label for="password">Password</label>
            <input type="password" name="password" id="in1" required><br><br>
            <div class="end">
                <input type="submit" name="submit">
                <input type="reset" id="reset">
                <p id="log">Click here to <a href="intern1.html">Register</a>
                </p>

            </div>


        </form>
    </div>
</body>
</html>''')
username = form.getvalue("username")
password = form.getvalue("password")
submit = form.getvalue("submit")

if submit is not None:

    login = '''select id from userregister where email = '%s' and createpass = '%s' ''' % (username, password)
    cur.execute(login)
    con.commit()
    a = cur.fetchone()
    if a[0] is not None:
        print('''<script> alert("Login Successfully");location.href ="dashboard.py?id=%s" </script>''' % a[0])
    con.close()
