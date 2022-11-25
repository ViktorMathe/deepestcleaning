function initMap(){
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        center: {
            lat: 52.64130885329782,
            lng: 1.2950372525097031
        }
    });
    
    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    var locations = [
        { lat: 52.64130885329782, lng: 1.2950372525097031},
    ];

    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    const markerCluster = new markerClusterer.MarkerClusterer({ map, markers });
}

setTimeout(function () {
    let messages = document.getElementById('popup');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3500);

hideMessage(function(){
    let msg = document.getElementById('msg');
    var auth = "{{ request.user.is_authenticated }}";

    if (auth) {
        msg.classList.add('hide')
    }
    else {
        msg.classList.remove('hide')
    }
})