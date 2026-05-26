function appendValue(value){

    document.getElementById("display").value += value;
}


function clearDisplay(){

    document.getElementById("display").value = "";
}


function calculate(){

    let expression = document.getElementById("display").value;

    fetch('/check_code', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },

        body: `code=${expression}`

    })

    .then(response => response.text())

    .then(data => {

        if(data === "vault"){

            window.location.href = "/vault";
        }

        else{

            document.getElementById("display").value = data;
        }
    });
}function appendValue(value){

    document.getElementById("display").value += value;
}


function clearDisplay(){

    document.getElementById("display").value = "";
}


function calculate(){

    let expression = document.getElementById("display").value;

    fetch('/check_code', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },

        body: `code=${expression}`

    })

    .then(response => response.text())

    .then(data => {

        if(data === "vault"){

            window.location.href = "/vault";
        }

        else{

            document.getElementById("display").value = data;
        }
    });
}
