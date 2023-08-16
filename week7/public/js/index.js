function check_signup(form){
    let name = form.querySelector("#name_signup").value, username = form.querySelector("#username_signup").value, password = form.querySelector("#password_signup").value
    if (! name){
        alert("Please enter the name for sign-up");
        return false;
    };
    if (! username){
        alert("Please enter the username for sign-up");
        return false;
    };
    if (! password){
        alert("Please enter the password for sign-up");
        return false;
    };
    if (username === password){
        alert("Don't use username as password");
        return false;
    }
    // alert("Sign-up successful")
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