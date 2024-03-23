let map;
async function initMap() {
    // const locs = [];
    // $.get("/apioutlets/", function(data, status){
    //     let len = data.length;
    //     for (var i=0; i < len; i++){
    //         locs.push({ lat: data[i].lat, lng: data[i].long });
    //     }
    //     console.log(locs);
    // });
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    map = new Map(document.getElementById("map"), {
        zoom: 12,
        center: { lat: 3.118753, lng: 101.677459 },
        mapId: "SUBWAY",
    });
    
    var marker, circle, position;
    $.get("/apioutlets/", function(data, status){
        let len = data.length;
        for (var i=0; i < len; i++){
            position = { lat: data[i].lat, lng: data[i].long };
            marker = new AdvancedMarkerElement({
                map: map,
                position: position,
                title: data[i].name,
            });
            circle = new google.maps.Circle({
                strokeColor: "#FF0000",
                strokeOpacity: 0.3,
                strokeWeight: 2,
                fillColor: "#FF0000",
                fillOpacity: 0.0,
                map,
                center: position,
                radius: 2500,
            });
        }
    });
}

initMap();