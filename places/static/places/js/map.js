// places/static/places/js/map.js

class MoroccoMap {
    constructor(mapElementId, options = {}) {
        this.mapElementId = mapElementId;
        this.map = null;
        this.markers = [];
        this.options = {
            center: [31.7917, -7.0926], // Centre du Maroc
            zoom: 6,
            minZoom: 5,
            maxZoom: 18,
            ...options
        };
    }
    
    init() {
        // Initialiser la carte
        this.map = L.map(this.mapElementId).setView(this.options.center, this.options.zoom);
        
        // Ajouter la couche de base
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap',
            maxZoom: this.options.maxZoom
        }).addTo(this.map);
        
        return this;
    }
    
    addPlaceMarker(place, iconType = 'place') {
        if (!place.latitude || !place.longitude) return null;
        
        const icon = this.createIcon(iconType);
        const marker = L.marker([place.latitude, place.longitude], { icon })
            .addTo(this.map)
            .bindPopup(this.createPopup(place));
        
        this.markers.push(marker);
        return marker;
    }
    
    createIcon(type) {
        const colors = {
            'city': '#006233',    // Vert Maroc
            'place': '#C1272D',   // Rouge Maroc
            'stadium': '#D4AF37', // Or Maroc
            'hotel': '#1E3A8A'    // Bleu Maroc
        };
        
        const icons = {
            'city': 'fa-city',
            'place': 'fa-landmark',
            'stadium': 'fa-futbol',
            'hotel': 'fa-hotel'
        };
        
        const color = colors[type] || colors.place;
        const iconClass = icons[type] || icons.place;
        
        return L.divIcon({
            className: 'custom-marker',
            html: `
                <div style="
                    background-color: ${color};
                    width: 30px;
                    height: 30px;
                    border-radius: 50%;
                    border: 3px solid white;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                ">
                    <i class="fas ${iconClass}" style="color: white; font-size: 14px;"></i>
                </div>
            `,
            iconSize: [30, 30],
            iconAnchor: [15, 30],
            popupAnchor: [0, -30]
        });
    }
    
    createPopup(place) {
        return `
            <div style="min-width: 200px;">
                <h5 style="margin: 0 0 5px 0; color: #006233;">${place.name}</h5>
                <p style="margin: 0 0 10px 0; color: #666;">
                    <i class="fas fa-city"></i> ${place.city}
                </p>
                <div style="margin-bottom: 10px;">
                    <small>
                        <i class="fas fa-map-pin"></i> 
                        Lat: ${place.latitude}, Lng: ${place.longitude}
                    </small>
                </div>
                <a href="/places/${place.id}/" class="btn btn-sm btn-primary" style="width: 100%;">
                    <i class="fas fa-info-circle"></i> Voir détails
                </a>
            </div>
        `;
    }
    
    addCities(cities) {
        cities.forEach(city => {
            this.addPlaceMarker(city, 'city');
        });
    }
    
    addPlaces(places) {
        places.forEach(place => {
            this.addPlaceMarker(place, 'place');
        });
    }
    
    fitBounds() {
        if (this.markers.length > 0) {
            const group = new L.featureGroup(this.markers);
            this.map.fitBounds(group.getBounds().pad(0.1));
        }
    }
    
    addControls() {
        // Contrôle de zoom personnalisé
        L.control.zoom({ position: 'topright' }).addTo(this.map);
        
        // Échelle
        L.control.scale({ imperial: false }).addTo(this.map);
    }
}

// Export pour utilisation globale
if (typeof window !== 'undefined') {
    window.MoroccoMap = MoroccoMap;
}