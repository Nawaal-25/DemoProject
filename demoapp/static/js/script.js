function udata()
{
    var uname=document.getElementById('username').value;
    var email=document.getElementById('email').value;
    var password=document.getElementById('password').value;
    // console.log("Username is ",uname);
    // document.write("User name is ",uname);
    // document.write("<br>Email is ",email);
    // document.write("<br>Password name is ",password);
    document.getElementById('h1').innerHTML=uname;
    document.getElementById('h2').innerHTML=email;
    document.getElementById('h3').innerHTML=password;
}
    