
API_KEY = ''
const url =  'https://api.openai.com/v1/chat/completions';

const regis_user_url = "http://localhost:8080/regisUser";
const login_user_url = "http://localhost:8080/signIn";

const submitButton = document.querySelector("#submit");
const outputElement = document.querySelector('.output');
const inputElement = document.querySelector('textarea');
const historyElement = document.querySelector('.history');
const buttonElement = document.querySelector('button');
const log_in_user = document.getElementById("user_name");
let signInBtn = document.getElementById("sign_in");

function changeInput(value){

    const inputElement = document.querySelector('input')
    inputElement.value = value;
}


async function getMessage(){
    


    try{

        const response = await fetch(url,{

            method : 'POST',
            headers : {
                'Authorization' : `Bearer ${API_KEY}`,
                'Content-Type' : 'application/json',

            },
            body: JSON.stringify({
                model : "gpt-3.5-turbo",
                messages : [{role : "user", content : inputElement.value}],
                // max_tokens : 100
            })
        })

        const data = await response.json();

        console.log(data);
        // outputElement.textContent = data.choices[0].message.content;
        if(data.choices[0].message.content && inputElement.value){
            const in_and_out = document.createElement("div");
            const uElement = document.createElement('p');
            const gElement = document.createElement('p');
            const hElement = document.createElement('p');
            uElement.textContent = `Q.  ${inputElement.value}`;
            hElement.textContent = inputElement.value;
            // alert(inputElement.value);
            gElement.textContent = data.choices[0].message.content;

            in_and_out.append(uElement);
            in_and_out.append(gElement);

            outputElement.append(in_and_out);
          

            hElement.addEventListener('click',()=>{
                changeInput(hElement.textContent);
            })
            historyElement.append(hElement)

        }
    }catch(error){
        console.log(error);
    }
}

// submitButton.addEventListener('click',getMessage)
// submitButton.addEventListener('keypress',function(e){
    // if(e.key == 'Enter'){
    //     console.log("enter presseed")
    // }

//     alert("prermfkdmf")
// })



inputElement.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        // console.log("clicked");
      event.preventDefault();
      document.getElementById("submit").click();
    }
  });

function clearInput(){
    inputElement.value = "";
}
buttonElement.addEventListener('click', clearInput)



signInBtn.addEventListener("click",function(){

    document.querySelector(".popup").classList.add("active");

});

document.querySelector(".popup .close-btn").addEventListener("click",function(){
    document.querySelector(".popup").classList.remove("active");

    // console.log("cross");
});


document.querySelector(".popup .already_account").addEventListener("click",function(){
    document.querySelector(".popup").classList.remove("active");
    document.querySelector(".popup_login").classList.add("active");

})

document.querySelector(".popup_login .close-btn").addEventListener("click",function(){
    document.querySelector(".popup_login").classList.remove("active");
});




////////////////////////////                           user register                                 /////////////////////////////////////


let user_submit = document.querySelector(".popup #address_submit");


function saveUser(){
   
    
let user_name = document.querySelector(".popup #name").value;
let user_email = document.querySelector(".popup #email").value;
let user_password = document.querySelector(".popup #password").value;


        fetch("http://localhost:8080/regisUser",{
            method : "POST",
            headers : {
                "content-type":"application/json"
            },
            body : JSON.stringify({
               
                "id":10,
                "name":user_name,
               "email":user_email,
                "password":user_password,
                "role":"ROLE_USER"
                
            })
        }).then(response=>{
            if(response.status == 201 || response.status == 200){
                response.json().then(data => {
                    alert("user successfully registered with name :"+data.name)
                })
            }else{
                response.json().then(data => alert("failed"))
            }
        }).catch(error=>{
            alert(error)
        });

        // const data = await response.json();
  
}
user_submit.addEventListener("click",saveUser);




////////////////////////////                           user login                                 /////////////////////////////////////


let user_email_login = document.querySelector(".popup_login #email");
let user_submit_login = document.querySelector(".popup_login #address_submit")

function userLogin(){

    let user_email_login = document.querySelector(".popup_login #email").value;
let user_password_login = document.querySelector(".popup_login #password").value;

    const promise = fetch(login_user_url,{
        method : "POST",
        headers : {
            "content-type": "application/json"
        },
        body : JSON.stringify({

                "email":user_email_login,
                "password":user_password_login
        })
        
    })


    promise.then(response=>{
        if(response.status==201 || response.status==200){
            response.json().then(data=>{
                // alert(data)
                const confirmation = confirm("login successfully "+data.name);
                if(confirmation){

                    signInBtn.setAttribute("opacity",0);
                    log_in_user.textContent = data.name;
                    localStorage.setItem("interviewkey",data.id);
                    
                }
            })
           
        }else{
            response.text().then(data => {
                if(data && data.length > 0){
                    alert("Login failed : "+data);
                }else{
                    alert("this email and password does not matching with our database.")
                }
                
            })
        }
       
    }).catch(error=>alert("error occured "+error));
}

user_submit_login.addEventListener("click",userLogin);


