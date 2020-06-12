function displayBotEntry(entry, url)
// Display bot entries
{
    var chatWindow = document.getElementById('chatwindow');
    var textZone = document.createElement('div');
    var titleZone = document.createElement('div');
    var wikiLink = document.createElement('a');
    titleZone.classList.add('grandpybot_title');
    textZone.classList.add('grandpybot');
    titleZone.innerHTML = "Grandpy \n";
    textZone.textContent = entry;
    chatWindow.appendChild(titleZone);
    chatWindow.appendChild(textZone);
    textZone.appendChild(wikiLink);
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
    var chatWindow = document.getElementById('chatwindow');
    var titleZone = document.createElement('div');
    var textZone = document.createElement('div');
    titleZone.classList.add('user_title');
    textZone.classList.add('user');
    titleZone.innerHTML = "Moi \n";
    textZone.textContent = entry;
    chatWindow.appendChild(titleZone);
    chatWindow.appendChild(textZone);
}

function initMap(coord)
// Display Google's map and its marker corresponding to coordinates
{
    var chatWindow = document.getElementById('chatwindow');
    var mapZone = document.createElement('div');
    mapZone.classList.add('map');
    mapZone.style.display = 'block';
    chatWindow.appendChild(mapZone);
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
    var chatWindow = document.getElementById('chatwindow')
    var loaderZone = document.createElement('div');
    var loader = document.createElement('img');
        loaderZone.setAttribute('id', 'ajax-loader');
    loader.setAttribute('src', '../static/img/ajax_loading_icon.gif');
    loader.setAttribute('alt', "Ajax loader");
    loaderZone.appendChild(loader);
    chatWindow.appendChild(loaderZone);
}

function removeGifLoader()
// Remove gif loader when AJAX request is done
{
    var loaderZone = document.getElementById('ajax-loader');
    loaderZone.remove();
}