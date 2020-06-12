$('#submit').on('click', function()
// Get user input when "Envoyer" button is clicked
{
    var userQuery = document.getElementById('user_query').value;
    if (userQuery !== "") {
        userQueryTreatment(userQuery);
    }
});

$(document).on('keydown', function(event)
// Handles user submission when "RETURN" is pressed
{
    var userQuery = document.getElementById('user_query').value;
    var key = event.keyCode;
    if (key === 13 && userQuery !== "") {
        userQueryTreatment(userQuery);
    }
});

function userQueryTreatment(userQuery)
// Display user query in chat window, clear form and init ajax request
{
    displayUserEntry(userQuery);
    var userZone = document.getElementById("user_query");
    userZone.value = "";
    ajaxPostRequest('/ajax', userQuery, botResponseTreatment);
}

function ajaxPostRequest(url, data, callback)
// Display gif loader, prepare and send ajax 'POST' request
{
    displayGifLoader();
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
        console.error("Network failure with URL " + url);
    });
    req.send(data);
}

function getRandomAnswer(array) {
  return array[Math.floor(Math.random() * Math.floor(3))];
}

function botResponseTreatment(response_data)
// Get AJAX response, remove gif loader and display answer
{
    var validAnswer = ["Bien-sûr mon poussin ! La voici : ",
                      "C'est là que j'ai connu ta grand-mère, figure-toi ! C'est à cette adresse : ",
                      "Tiens, j'en ai justement entendu parler dans le journal de midi ! C'est à cet endroit : "]
    var notFoundAnswer = ["Désolé, parfois je perds un peu le fil.",
                        "Hein ? J'ai les circuits auditifs oxydés ...",
                        "Mon kernel n'est pas très coopératif aujourd'hui ..."]
    var noExtractFound = ["Hmm, je connais cet endroit mais je ne me souviens plus de son histoire ... Mais je peux t'en raconter d'autres si tu veux !",
                            "Pas le temps pour les histoires, mes batteries sont à plat !",
                            "De mon temps, quand on ne connaissait pas quelque-chose, il fallait demander sur la place du village ! Je crois que ça s'appelle Quora maintenant, ou peut-être Reddit ..."]
    var extractFound = ["Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? ",
                        "Ah, ça y est, j'ai fini de télécharger mes souvenirs. ",
                        "Laisse moi retrouver l'entrée dans ma base de donnée ... J'y suis. "]

    var data = JSON.parse(response_data);

    // debug
    console.log("contenu de data :", data);
    removeGifLoader();
    if (data !== "") {
        displayBotEntry(getRandomAnswer(validAnswer) + data['address'] + ".", "")
        initMap(data['coords']);
        // debug
        console.log(data['coords'])
        console.log(data['extract']);
        console.log(data['address']);
        console.log(data['url']);
        //
        if (data['extract'] !== "") {
            displayBotEntry((getRandomAnswer(extractFound) + data['extract']), data['url']);

        } else {
            displayBotEntry(getRandomAnswer(noExtractFound))
        }
    } else {
        displayBotEntry( getRandomAnswer(notFoundAnswer), "")
    }
}

