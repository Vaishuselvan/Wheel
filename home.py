#!C:/Users/vaish/AppData/Local/Programs/Python/Python311/python.exe
import cgi
import cgitb
import pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="wheel")
cur = con.cursor()
form = cgi.FieldStorage()
j = form.getvalue("id")
print("content-type:text/html \r\n\r\n")
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
    <style>
        *{
    padding: 0;
    margin: 0;
    font-family: 'poppins';
}
.head{
    background-color: #543310;
}
.logo,
.img{
    width: 40px;
    height: 40px;
    border-radius: 40px;
    float: right;
    padding: 5px 3px;
    margin-right:30px ;
}
.nav-link{
    color: #F8F4E1;
    font-size: 20px;
    gap: 20px;
}
#btn{
    border-color:#F8F4E1;
    background: transparent;
    border-radius: 10px;
    border-width: 1px;
   margin-top: 5px;
    font-size: 18px;
    color: #F8F4E1;
}
.contain{
    width: 100%;
    height: 550px;
    z-index: 1;
  background-image: linear-gradient(45deg,
                    rgba(18, 21, 21, 0.9),
                    rgba(0, 7, 14, 0.75)), url('Database/image/img.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  color: #FFFFFF;
}
/*img{
    width: 100%;
    height: 600px;
}*/
.row{
    width: 50%;
    height:60px;
    display: inline-block;
    align-items: center;
    padding: 20px 10px;
    margin-left:70px ;
    justify-content: left;
}
.row1 {
  display: flex;
  height: 88%;
  align-items: center;
  justify-content: left;
}
.col1 {
  flex-basis: 50%;
}
.col{
    gap: 70px;
    display: inline-block;
    justify-content:space-between ;
    background-color: rgb(190, 73, 10);
    border-radius: 20px;
    border: #543310 2px soloid;
    width: 90px;
    height: 90px;
    padding: 20px 10px;
}
h2,
span{
    color:#F8F4E1;
}
.sec{
    color: #543310;
}
h1{
    color: #FFFFFF;
    font-size: 50px;
    font-weight: 900;
    padding: 70px 50px;
}
h2{
    color: #FFFFFF;
    font-size: 50px;
    font-weight: 900;
    padding: 70px;
}


  </style>
</head>
<body>
    <header class="head">
        <div class="logo">
            <img src="./foodlogo.png" alt="logo" class="img">
        </div>
        <div class="hypl">
            <ul class="nav justify-content-center">
                <li class="nav-item">
                    <a href="#" class="nav-link">Home</a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">Setting</a>
                </li>''')
print('''
                <li class="nav-item">
                    <button id="btn" onclick=""><a href="./log.py?id=%s">Login</a></button>
                </li>''' % j)
print('''
                <li class="nav-item">
                    <button id="btn" onclick=""><a href="./intern1.html">Register</a></button>
                </li>''')
print('''
                <li class="nav-item">
                    <button id="btn" onclick=""><a href="reg1.py?id=%s">Register</a></button>
                </li>''' % j)
print('''
            </ul>
        </div>
    </header>
        <div class="contain">
            <h1>Wellcome <span id="sec">Foodee</span></h1>
            <h2>Eat Sleep Repeat</h2>
        </div>
        <div>
            <div class="row">
                <div class="col">
                    <h2>30K</h2>
                    <span>veiw</span>
                </div>
                <div class="col">
                    <h2>400K</h2>
                    <span>Customer</span>
                </div>
                <div class="col">
                    <h2>3K</h2>
                    <sp >Onwers</span>
                </div>
        </div>

    <footer class="foot">
        <div class="row1">
            <div class="col1">
                <h3>Conclusion</h3>
                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Necessitatibus at cumque illo voluptas modi odit ut nam delectus, sed aut dolorem recusandae possimus quibusdam molestias dolorum quidem cum a placeat eligendi? Explicabo, voluptas quos! Optio vero deleniti eaque quidem officiis?</p>
            </div>
            <div class="col1">
                <h3>contact</h3>
                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. A odit similique magni.</p>
            </div>
        </div>
    </footer>
</body>
</html>''')
