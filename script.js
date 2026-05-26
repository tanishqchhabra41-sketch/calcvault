function append(value){

    document.getElementById("screen").value += value;
}


function clearScreen(){

    document.getElementById("screen").value = "";
}


function removeLast(){

    let current =
    document.getElementById("screen").value;

    document.getElementById("screen").value =
    current.slice(0,-1);
}


function calculate(){

    let expression =
    document.getElementById("screen").value;

    fetch('/calculate', {

        method:'POST',

        headers:{
            'Content-Type':
            'application/x-www-form-urlencoded'
        },

        body:'expression=' +
        encodeURIComponent(expression)
    })

    .then(response => response.text())

    .then(data => {

        if(data === "VAULT"){

            alert("Secret Vault Opened 🔒");
        }

        else{

            document.getElementById("screen").value = data;
        }
    });
}
