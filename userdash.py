#!C:/Users/vaish/AppData/Local/Programs/Python/Python311/python.exe
import cgi
import cgitb
from typing import Any
import pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="wheel")
cur = con.cursor()
form = cgi.FieldStorage()
k = form.getvalue("id")
print("content-type:text/html \r\n\r\n")
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin and User Dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://fontawesome.com/icons/magnifying-glass?f=classic&s=thin">
    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <style>
        *{
            padding: 0;
            margin: 0;
            font-family: 'Poppins', sans-serif;
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
                        rgba(0, 7, 14, 0.75)), url('./img.jpg');
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
            color: #FFFFFF;
        }
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
            border: #543310 2px solid;
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
        #sec{
            color:rgb(190, 73, 10);
        }
        .img-wrapper{
            margin-top: 20px;
            width: 100%;
            height: 50%;
            display: flex;
            justify-content: baseline;
        }
        .media{
            width: 30%;
            height: 30%;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 10px;
            overflow: hidden;
            position: relative;
        }
        .media:hover {
            cursor: pointer;
        }
        .overlay {
            background: rgba(0, 0, 0, 0.7);
            position: absolute;
            height: 100%;
            width: 100%;
            z-index: 3;
            opacity: 0;
            transition: all ease-in-out 0.5s;
        }
        .media:hover .overlay {
            opacity: 1;
        }
        img{
            width: 40%;
            height: 40%;
            border-radius: 40%;
            z-index: -1;
            margin: auto;
            transform: scale(1);
            transition: all ease-in-out 0.5s;
        }
        .media:hover img {
            transform: scale(1.1);
            filter: blur(2px);
        }
        .image-details {
            text-align: center;
            color: white;
            font-size: 20px;
            z-index: 4;
            position: absolute;
            top: 100%;
            opacity: 0;
            transition: all ease-in-out 0.5s;
        }
        .media:hover .image-details {
            top: 40%;
            opacity: 1;
        }
        @media only screen and (max-width: 900px) {
            .media {
                width: 70%;
                height: 70%;
            }
        }
        .search{
            margin: 50px;
            display: flex;
            justify-content: center;
        }
        input{
            width: 30%;
            height: 5vh;
            border-color: #7a450e;
            border: solid 2px;
            border-radius: 20px;
            padding-left: 10px;
        }
        .foot{
            margin-top: 100px;
            background-color: #7a450e;
            height: 50%;
        }
        .cards-collection{
            width:100%;
            height: 70vh;
            background-color: linear-gradient(to right, #512c04 , rgb(230, 101, 31));
            display: flex;
            justify-content: space-evenly;
        }
        .card{
            width: 50%;
            height: 50%;
            border-radius: 10px;
            margin: 10px;
            display: flex;
            justify-content: space-evenly;
        }
        .box {
            width: 100%;
            height: 100%;
        }
        .rating {
            margin: 15px;
            color:#7a450e;
        }
        .hotel-name{
            font-size: 30px;
            font-weight: 500;
        }
        .sec1{
            font-size: 10px;
            color: rgb(222, 204, 0);
        }

        /* User Dashboard Styles */
        .user-dashboard{
            padding: 20px;
            background-color: #f4f4f4;
        }
        .user-dashboard h2{
            font-size: 30px;
            color: #333;
        }
        .user-dashboard .section{
            background-color: #fff;
            margin: 1em 0;
            padding: 1em;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .user-dashboard .section h3{
            border-bottom: 1px solid #ddd;
            padding-bottom: 0.5em;
        }
        .dash-img{
            width: 90px;
            height: 90px;
            border-radius: 90px;
            background-color: #7a450e;
        }
        #profile{
            width: 50px;
            height: 50px;
            border-radius: 50px;

        }
    </style>
</head>
<body>
    <header class="head">
        <div class="logo">
            <center><img src="./foodlogo.png" alt="logo" class="img"></center>
        </div>
    </header>
    <!-- User Dashboard Section -->
    <div class="user-dashboard">
        <h2>User Dashboard</h2>''')
photo = f"select * from imgreg where id ='{k}'"
cur.execute(photo)
img = cur.fetchall()

for i in img:
    gt = "database/" + i[10]
    print(f'''<div class="dash-img">
            <center><img src="{gt}" alt="" id="profile"></center>
        </div>''')

    print('''<div class="section">
            <h3>Profile</h3>
            <p>Welcome, [User Name]</p>
            <p>Email: [User Email]</p>
            <p><a href="#">Edit Profile</a></p>
        </div>
        <div class="section" id="myorder">
            <h3>Order History</h3>
            <ul>
                <li>Order #1234 - Completed</li>
                <li>Order #5678 - In Progress</li>
                <li>Order #9101 - Cancelled</li>
            </ul>
        </div>
        <div class="section" id="fav">
            <h3>Favorites</h3>
            <ul>
                <li>Favorite Item 1</li>
                <li>Favorite Item 2</li>
                <li>Favorite Item 3</li>
            </ul>
        </div>
    </div>
    <footer class="foot">
        <div class="row1">
            <div class="col1">
                <h3>Conclusion</h3>
                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Necessitatibus at cumque illo voluptas modi odit ut nam delectus, sed aut dolorem recusandae possimus quibusdam molestias dolorum quidem cum a placeat eligendi? Explicabo, voluptas quos! Optio vero deleniti eaque quidem officiis?</p>
            </div>
            <div class="col1">
                <h3>Contact</h3>
                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. A odit similique magni.</p>
            </div>
        </div>
    </footer>
</body>
</html>
''')
