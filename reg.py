#!C:/Users/vaish/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql, os, smtplib
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="wheel")
cur = con.cursor()
form = cgi.FieldStorage()
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FORMS</title>
    <style>
        *{
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
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
            <input type="password" name="createpass" id="in1"><br><br>
            <label for="pass">Confirm Password</label>
            <input type="password" name="confpass" id="in1"><br><br>
            <label for="Phone">Phone</label>
            <input type="number" name="phone" id="in1"><br><br>
            <label for="email">Email</label>
            <input type="email" name="email" id="in1"><br><br>
            <p>Country</p>
            <select name="country" id="sel">

                <option value="" disabled selected>--select--</option>
                <optgroup label="Country">
                <option value="India">India</option>
                <option value="canada">Canada</option>
                <option value="usa">USA</option>
                <option value="Newzealand">New Zealand</option>
                <option value="england">England</option>
            </optgroup>
            </select>

            <p>City</p>
            <input type="text" required name="city"><br><br>
            <p>Address</p>
            <textarea name="address" id="txt" rows="5" cols="30"></textarea>

            <div class="end">
                <input type="submit" id="btn"  name="submit">
                <input type="reset" id="reset">
                <p id="log">Click here to <a href="log.html" target="_blank">Log-in</a>
                </p>

            </div>


        </form>
    </fieldset>
    </div>

   
</body>
<script>
    a = document.getElementById('btn').value;
    b = document.getElementById('in1').value;
    c = document.getElementById('sel').value;
    function register(){
        if(b == ""){
            alert("fill the required");
        }
        else{
            alert("Successfully registered")
        }
    }
</script>
</html>

''')
firstname = form.getvalue("firstname")
lastname = form.getvalue("lastname")
createpass = form.getvalue("createpass")
confpass = form.getvalue("confpass")
phone = form.getvalue("phone")
email = form.getvalue("email")
country = form.getvalue("country")
city = form.getvalue("city")
address = form.getvalue("address")
submit= form.getvalue("submit")

if submit != None:
    sub='''insert into userregister (firstname, lastname, createpass, confpass, phone, email, country, city, address) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')''' %(
    firstname, lastname, createpass, confpass, phone, email, country, city, address)
    cur.execute(sub)
    con.commit()
    print('''<script> alert(“Register Successfully”); </script>''')
    con.close()


if submit != None:
    mail = "vaishuselvan2003@gmail.com"
    pwd = "wofu nvrq mmni joeg"
    toadd = email
    subject = "regarding email and password"
    body = "Dear {}, \n\n  Your verified email and password, \n\n email: {} \n\n password: {}".format(firstname, email, confpass)
    msg = "subject: {}, \n\n {}".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(mail, pwd)
    server.sendmail(mail, toadd, msg)
    server.quit()
    print('''<script> alert("Mail sent successfully");</script>''')
con.close()


