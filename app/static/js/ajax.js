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

function getRandomAnswer(array) {
  return array[Math.floor(Math.random() * Math.floor(3))];
}

function responseTreatment(data)
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
    var data = JSON.parse(data);

    // debug
    console.log("contenu de data :", data);
    removeLoader();
    if (data !== "") {
        displayPybot(getRandomAnswer(validAnswer) + data['address'] + "." )
        initMap(data['coords']);
        // debug
        console.log(data['coords'])
        console.log(data['extract']);
        console.log(data['address']);
        console.log(data['url']);
        //
        if (data['extract'] !== "") {
            displayPybot(data['extract']);
            var linkWiki = document.createElement('a');
            linkWiki.classList.add('wikilink');
            linkWiki.setAttribute('href',data['url']);
            linkWiki.href = data['url'] ;
            linkWiki.innerHTML = "[En savoir plus sur Wikipédia]";
            $("grandpybot").append(linkWiki);
            $("grandpybot").append('<p><a href=" + data[\'url\'] + "> [En savoir plus sur Wikipédia]</a> <br />)</p>');
            displayPybot('<p><a href=" + data[\'url\'] + "> [En savoir plus sur Wikipédia]</a> <br />)</p>')

            displayPybot("<a href=" + data['url'] + "> [En savoir plus sur Wikipédia]</a> <br />" );
            displayPybot(data['url']);
            //$('#wikilink').html('<a href=" + data[\'url\'] + "> [En savoir plus sur Wikipédia]</a> <br />');
        } else {
            displayPybot(getRandomAnswer(noExtractFound))
        }
    } else {
        displayPybot(getRandomAnswer(notFoundAnswer))
    }
}

function changeLink() {
     var link = document.getElementsByClassName('wikilink');
     link.href(data['url']) ;
     link.innerHTML("[En savoir plus sur Wikipédia]");
     link.setAttribute(href, data['url']);
}