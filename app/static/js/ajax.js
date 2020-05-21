$('#submit').on('click', function()
// Get user input when "Envoyer" button is clicked
{
    var userQuery = document.getElementById('user_query').value;
    if (userQuery !== "") {
        userValidated(userQuery);
    }
});

$(document).on('keydown', function(event)
// Handles user submission with 'RETURN' key
{
    var userQuery = document.getElementById('user_query').value;
    var key = event.keyCode;
    if (key === 13 && userQuery !== "") {
        userValidated(userQuery);
    }
});

function userValidated(userQuery)
// Display user query in chat window, clear form and init ajax request
{
    displayUser(userQuery);
    var userZone = document.getElementById("user_query");
    userZone.value = "";
    ajaxPost('/ajax', userQuery, responseTreatment);
}

function ajaxPost(url, data, callback)
// Display gif loader, prepare and send ajax 'POST' request
{
    displayLoader();
    var req = new XMLHttpRequest();
    req.open('POST', url);
    req.addEventListener('load', function() {
        if ((req.status >= 200 && req.status < 400)) {
            callback(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener('error', function() {
        console.error("Erreur réseau avec l'URL " + url);
    });
    req.send(data);
}


function responseTreatment(data)
// Get AJAX response, remove gif loader and display answer
{
    var data = JSON.parse(data);
    // debug
    console.log("contenu de data :", data);
    removeLoader();
    if (data !== "") {
        displayPybot("Bien-sûr mon poussin ! La voici : " + data['address'] + "." )
        initMap(data['coords']);
        // debug
        console.log(data['coords'])
        console.log(data['extract']);
        console.log(data['address']);
        if (data['extract'] !== "") {
            displayPybot(data['extract']);
        }
    } else {
        displayPybot("Désolé, parfois je perds un peu le fil.")
    }
}
