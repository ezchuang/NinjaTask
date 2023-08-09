function check_signup(form){
    if (! form.querySelector("#name_signup").value){
        alert("Please enter the  name for sign-up");
        return false;
    };
    if (! form.querySelector("#username_signup").value){
        alert("Please enter the  username for sign-up");
        return false;
    };
    if (! form.querySelector("#password_signup").value){
        alert("Please enter the  password for sign-up");
        return false;
    };
    alert("Sign-up successful")
    return true;
}

function check_signin(form){
    if (! form.querySelector("#username_signin").value){
        alert("Please enter the username for sign-in");
        return false;
    };
    if (! form.querySelector("#password_signin").value){
        alert("Please enter the password for sign-in");
        return false;
    };
    return true;
}