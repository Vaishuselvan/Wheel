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
    <link rel="stylesheet" href="https://fontawesome.com/icons/magnifying-glass?f=classic&s=thin">
    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <style>
        *{
    padding: 0;
    margin: 0;
    font-family: 'poppins';
}
.head{
    background-color: #543310;
}
.logo{
    width: 30px;
    height: 30px;
    border-radius: 30px;
    float: right;
    padding: 5px 3px;
    margin-right:30px ;
    background-color: rgb(141, 116, 83);
    margin-top: 5px;
}
.nav-link{
    color: #F8F4E1;
    font-size: 20px;
    gap: 20px;
}
.dashboard{
  width: 40px;
  height: 40px;
  border-radius: 40px;
  background-color: #F8F4E1;
  float: right;
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
#sec{
    color:rgb(190, 73, 10);
}
.img-wrapper{
    margin-top: 20px;
    width: 100%;
    height: 50%;
    display: flex;
    justify-content: baseline;
    /* background-color: rgb(185, 106, 63); */
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
.rating
{
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
h6{
  text-align: center;
  color: #FFFFFF;
}

  </style>
</head>''')
print('''
<body>
    <header class="head">
        <div class="logo">
         <a href="userdash.py?id=%s"> <h6>D </h6></a>
        </div>''' %j)
print('''
        <div class="hypl">
            <ul class="nav justify-content-center">
                <li class="nav-item">
                    <a href="#" class="nav-link">Home</a>
                </li>
                <li class="nav-item">
                    <a href="#lookbar" class="nav-link">Search</a>
                </li>
                <li class="nav-item">
                    <a href="./log.html" class="nav-link">Login</a>
                </li>
                <li class="nav-item">
                    <a href="./intern1.html" class="nav-link">Register</a>
                </li>
                <!-- <li class="nav-item">
                    <a href="./reg.html" class="nav-link">Register</a>
                </li> -->
                <li class="nav-item">
                    <button class="btn"><i class="fa fa-cart"></i></button>
                </li>
            </ul>
        </div>
    </header>
        <div class="contain">
            <h1>Wellcome <span id="sec">Foodee</span></h1>
            <h2><span id="sec">Eat</span> and Enjoy</h2>
        </div>
        <div class="img-wrapper">
            <div class="media">
                <div class="overly"></div>
                <img src="Database/image/kerala.jpg" alt="">
                <div class="img-detail">
                    <p></p>
                </div>
            </div>
            <div class="media">
                <div class="overly"></div>
                <img src="Database/image/fish.webp" alt="">
                <br>
                <div class="img-detail">
                    <p></p>
                </div>
            </div>
            <div class="media">
                <div class="overly"></div>
                <img src="Database/image/biryani.png" alt="">
                <br>
                <div class="img-detail">
                    <p></p>
                </div>
            </div>
            <div class="media">
                <div class="overly"></div>
                <img src="Database/image/thai.png" alt="">
                <div class="img-detail">
                    <p></p>
                </div>
            </div>
            <div class="media">
                <div class="overly"></div>
                <img src="Database/image/noodles.png" alt="">
                <div class="img-detail">
                    <p></p>
                </div>
            </div>
            <div class="media">
                <div class="overly"></div>
                <img src="Database/image/idly.webp" alt="">
                <div class="img-detail">
                    <p></p>
                </div>
            </div>
        </div>
        <div class="search">
            <input type="text" id="lookbar" placeholder="Search"><span id="sec"><i class="fa fa-search" style="padding-left: 5px; margin-top: 2px; cursor: pointer;"></i></span>
        </div>
        <div class="cards-collection">
            <div class="card">
                <div class="box">
                    <img src="Database/image/burger2.jpg" alt="img">
                </div>
                <div class="rating">
                    <h4 id="hotel-name">BurgerKing</h4><br>
                    <span id="sec1"><i class="fa fa-star"></i></span>
                    <span id="sec1"><i class="fa fa-star"></i></span>
                    <span id="sec1"><i class="fa fa-star"></i></span>
                    <span id="sec1"><i class="fa fa-star"></i></span>
                </div>
            </div>
            <div class="card">
                <div class="box">
                    <img src="Database/image/milkshakes.jpg" alt="">
                </div>
                <div class="rating">
                    <h4 id="hotel-name">Rosemilky</h4><br>
                    <span id="sec1"><i class="fa fa-star"></i></span>
                    <span id="sec1"><i class="fa fa-star"></i></span>
                    <span id="sec1"><i class="fa fa-star"></i></span>
                    <span id="sec1"><i class="fa fa-star"></i></span>
                    <span id="sec1"><i class="fa fa-star"></i></span>
                </div>
            </div>
            <div class="card">
                <div class="box">
                    <img src="Database/image/cakes.jpeg" alt="">
                </div>  
                <div class="rating">
                    <h4 id="hotel-name">Cake-Buzz</h4><br>
                    <span id="sec1"><i class="fa fa-star"></i></span>
                    <span id="sec1"><i class="fa fa-star"></i></span>
                    <span id="sec1"><i class="fa fa-star"></i></span>
                </div>     
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
</html>
''')