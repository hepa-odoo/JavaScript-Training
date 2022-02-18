async function registerCustomer()
{
    let fname=document.getElementById('FirstName').value;
    let lname=document.getElementById('LastName').value;
    let email=document.getElementById('InputEmail1').value;
    let password=document.getElementById('InputPassword1').value;

    let createCustomer = new Promise(function (resolve,reject) 
    {
        let req = new XMLHttpRequest();
        req.open('POST', 'registerInDatabase',true);
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        req.onload = function() {
        if (req.status == 200) {
            setTimeout(()=>resolve("success"),1000);
        } else {
            reject("Error: " + req.status);
        }
        }
        req.send("fname="+fname+"&lname="+lname+"&email="+email+"&password="+password);
    });
    document.getElementById('text-result').innerHTML="Registering Customer....";
    let result_msg=await createCustomer.catch((error)=>{
        alert(error);
        return "error";
    });
    if(result_msg=="error") document.getElementById('text-result').innerHTML="Error in registering customer!!!";
    else
    {
        document.getElementById('text-result').innerHTML="Gathering Customers list....";
        let getCustomers = new Promise(function (resolve,reject) 
        {
            let reqGetCustomers = new XMLHttpRequest();
            reqGetCustomers.open('GET', 'getCustomers',true);
            reqGetCustomers.onload = function() {
            if (reqGetCustomers.status == 200) {
                setTimeout(()=>resolve(this.responseText),1000);
            } else {
                reject("Error: " + reqGetCustomers.status);
            }
            }
            reqGetCustomers.send("fname="+fname+"&lname="+lname+"&email="+email+"&password="+password);
        });
        let customers_html=await getCustomers;
        document.getElementById('text-result').innerHTML=customers_html;
    }
}