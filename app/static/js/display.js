function displayPybot(entry, url)
// Display bot entries
{
    var chatWindow = document.getElementById('chatwindow');
    var textZone = document.createElement('div');
    var wikiLink = document.createElement('a');
    textZone.classList.add('grandpybot');
    textZone.textContent = entry;
    chatWindow.appendChild(textZone);
    textZone.appendChild(wikiLink);
    wikiLink.classList.add('wikilink');
    wikiLink.setAttribute('href', url);
    if (url == '') {
        wikiLink.innerHTML = "";
    } else {
        wikiLink.innerHTML = " [En savoir plus sur Wikipédia]";
    };
    chatWindow.scrollTop = chatWindow.scrollHeight - chatWindow.clientHeight;
}

function displayUser(entry)
// Display user entries
{
    var chatWindow = document.getElementById('chatwindow');
    var textZone = document.createElement('div');
    textZone.classList.add('user');
    textZone.textContent = entry;
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

function displayLoader()
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

function removeLoader()
// Remove gif loader when AJAX request is done
{
    var loaderZone = document.getElementById('ajax-loader');
    loaderZone.remove();
}