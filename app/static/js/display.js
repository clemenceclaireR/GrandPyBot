function displayBotEntry(entry, url)
// Display bot entries
{
    // get or create needed elements
    var chatWindow = document.getElementById('chatwindow');
    var textZone = document.createElement('div');
    var titleZone = document.createElement('div');
    var wikiLink = document.createElement('a');
    // give an id to the new elements
    titleZone.classList.add('grandpybot_title');
    textZone.classList.add('grandpybot');
    // set Grandpy name before its entry
    titleZone.innerHTML = "Grandpy \n";
    textZone.textContent = entry;
    // append new elements to its parent
    chatWindow.appendChild(titleZone);
    chatWindow.appendChild(textZone);
    textZone.appendChild(wikiLink);
    // set link element to store Wikipedia hyperlink
    wikiLink.classList.add('wikilink');
    wikiLink.setAttribute('href', url);
    if (url === '') {
        wikiLink.innerHTML = "";
    } else {
        wikiLink.innerHTML = " [En savoir plus sur Wikipédia]";
    }
    // get scrollbar always on bottom
    chatWindow.scrollTop = chatWindow.scrollHeight - chatWindow.clientHeight;
}

function displayUserEntry(entry)
// Display user entries
{
    // get or create needed elements
    var chatWindow = document.getElementById('chatwindow');
    var titleZone = document.createElement('div');
    var textZone = document.createElement('div');
    // give an id to the new elements
    titleZone.classList.add('user_title');
    textZone.classList.add('user');
    // set Grandpy name before its entry
    titleZone.innerHTML = "Moi \n";
    textZone.textContent = entry;
    // append new elements to its parent
    chatWindow.appendChild(titleZone);
    chatWindow.appendChild(textZone);
}

function initMap(coord)
// Display Google's map and its marker corresponding to coordinates
{
    // get or create needed elements
    var chatWindow = document.getElementById('chatwindow');
    var mapZone = document.createElement('div');
    // give an id to the new elements
    mapZone.classList.add('map');
    // set display style
    mapZone.style.display = 'block';
    // append new element to its parent
    chatWindow.appendChild(mapZone);
    // set display options for the map and the marker
    var map = new google.maps.Map(mapZone, {
        zoom: 16,
        center: coord
        });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
        });
}

function displayGifLoader()
// Display gif loader when Ajax is treating a request
{
    // get or create needed elements
    var chatWindow = document.getElementById('chatwindow')
    var loaderZone = document.createElement('div');
    var loader = document.createElement('img');
    // give an id to the loader and set others needed attributes
    loaderZone.setAttribute('id', 'ajax-loader');
    loader.setAttribute('src', '../static/img/ajax_loading_icon.gif');
    loader.setAttribute('alt', "Ajax loader");
    // append new elements to its parent
    loaderZone.appendChild(loader);
    chatWindow.appendChild(loaderZone);
}

function removeGifLoader()
// Remove gif loader when AJAX request is done
{
    var loaderZone = document.getElementById('ajax-loader');
    loaderZone.remove();
}