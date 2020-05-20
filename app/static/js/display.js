function displayLoader()
// Display gif loader (used during AJAX request)
{
    var chatWindow = document.getElementById('chatwindow')
    var loaderZone = document.createElement('div');
    loaderZone.setAttribute('id', 'ajax-loader');
    var loader = document.createElement('img');
    loader.setAttribute('src', '../static/img/ajax_loading_icon.gif');
    loader.setAttribute('alt', "Ajax loader");
    loaderZone.appendChild(loader);
    chatWindow.appendChild(loaderZone);
}

function removeLoader()
// Remove gif loader when AJAX request finished
{
    var loaderZone = document.getElementById('ajax-loader');
    loaderZone.remove();
}

function displayUser(speech)
{
    var chatWindow = document.getElementById('chatwindow');
    var speechZone = document.createElement('div');
    speechZone.classList.add('user');
    speechZone.textContent = speech;
    chatWindow.appendChild(speechZone);
}

function displayPybot(speech)
{
    var chatWindow = document.getElementById('chatwindow');
    var speechZone = document.createElement('div');
    speechZone.classList.add('grandpybot');
    speechZone.textContent = speech;
    chatWindow.appendChild(speechZone);
}

function initMap(coord)
// Display the Google Map and marker corresponding to coordinates
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