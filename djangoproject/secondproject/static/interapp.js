

const API_KEY = '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';
const url =  'https://api.openai.com/v1/chat/completions';

let next_button = document.querySelector("#next button");
let count = 0;
const textareaElement = document.querySelector("textarea");

let userId = 0;
let questions = [];
let user = null;
let score = 0;

const selectElement = document.querySelector("#courses");
selectElement.addEventListener("change",function(){

    if(selectElement.value != ""){
        getMessage("Please give top 10 question that is asked in "+selectElement.value +" Interview");
    }
    
})


let question = document.querySelector("h1");

async function getMessage(inp){
    
    // Display the loading animation
        const loadingAnimation = document.getElementById('loading-animation');
        loadingAnimation.style.display = 'flex';


    try{

        const response = await fetch(url,{

            method : 'POST',
            headers : {
                'Authorization' : `Bearer ${API_KEY}`,
                'Content-Type' : 'application/json',

            },
            body: JSON.stringify({
                model : "gpt-3.5-turbo",
                messages : [{role : "user", content : inp}],
      
            })
        })

        const data = await response.json();

        loadingAnimation.style.display = 'none';
        // console.log(data);
        let questions_string = data.choices[0].message.content;
        questions = questions_string.split("?");
        // console.log(questions);
        question.textContent = "Q"+questions[count]+"?";


       
           

        
    }catch(error){
        loadingAnimation.style.display = 'none';
        console.log(error);
    }
}

next_button.addEventListener("click",function(){

    // if(selectElement.value==""){
    //     alert("select course first..");
    // }else{
        
        count++;
        if(questions.length<=count){

            alert("question completed your score is "+score);


            userId = localStorage.getItem("interviewkey");
            // console.log(typeof userId);
            fetchUser(userId);

        //    console.log(user);
        //    updateUser(user);


        }else{
            if(textareaElement.value==""){

                score += 0;

            }else{
              
                next_button.disabled = true;
                next_button.innerText = "Generating score";
                giveScore(questions[count-1],textareaElement.value);
            }
        
        }

    // console.log(textareaElement.value);
    // }
   
    
    
})

async function giveScore(ques,ans){

    console.log("givescore called");
    const promise = await fetch(url,{
        method:"POST",
        headers :{
            "Authorization":`Bearer ${API_KEY}`,
            "Content-Type":"application/json"
        },
        body:JSON.stringify({

            model : "gpt-3.5-turbo",
            messages : [{role : "user", content : `ques- ${ques} this is question and answer,can you give a score out 10 for this answer ${ans}`}]
      

        })

    })

    const data = await promise.json();
    let score_data = data.choices[0].message.content;
    const matches = score_data.match(/\d+/);
    const firstNumber = matches ? parseInt(matches[0]) : 0;
    score += Number(firstNumber);
    
    const confirmation = confirm(score_data);
    if(confirmation){

        question.textContent = "Q"+questions[count]+"?";
        textareaElement.value = ""; 
        next_button.disabled = false;
        next_button.innerText = "Next";
       
    }
    console.log(score);

}

 function fetchUser(id){


    const promise =  fetch("http://localhost:8080/getUser/"+id,{

        method : "GET",
        headers : {
            "Content-Type":"application/json"
        },
      
    }).then(res=>{
        if(res.status==201 || res.status==200){
            res.json().then(data=>{

                // data.
                user =  data;
                // console.log(user);
                updateUser(user);

            })
        }else{
            res.json().then(err=>{
                console.log(err);
                // return err;
            })
        }
    }).catch(err=>{
        // return err;
        console.log(err);
    })


    // const res =  promise.json();
    

    // console.log(res);

}



function updateUser(user){

    let attempt = user.attempt;
    if(attempt==null){
        attempt = 1;
    }else{
        attempt++;
    }
    let per = user.performance;
    per.push(score);
    // console.log(per)
    
    

const promise =  fetch("http://localhost:8080/updateUser/"+user.id,{

    method : "PUT",
    headers : {
        "Content-Type":"application/json"
    },
    body:JSON.stringify({

        "id":user.id,
        "performance":per,
        "attempt":attempt
    })
  
}).then(res=>{
    if(res.status==201 || res.status==200){
        res.json().then(data=>{

            // data.
            console.log(data);

        })
    }else{
        res.json().then(err=>{
            // console.log(err);
            return err;
        })
    }
}).catch(err=>{
    // return err;
    console.log(err);
})




}


