var CLIENT_VERSION = "v0.9.20";
var SERVER_VERSION = "v0.9.20";
var MAPBOX_BASEMAPS = [{name: 'Charted', alias:'ESRI Charted Territory',description: 'Oooo lovely', id:'https://www.arcgis.com/sharing/rest/content/items/1c365daf37a744fbad748b67aa69dac8/resources/styles/root.json', provider:'esri'},
    {name: 'Topographic', alias:'ESRI Topographic',description: 'Oooo lovely', id:'https://www.arcgis.com/sharing/rest/content/items/0f52cd2d17ea4773944a1d0e0fb99ea4/resources/styles/root.json', provider:'esri'},
    {name: 'Streets', alias:'Mapbox Streets',description: 'A complete basemap, perfect for incorporating your own data.', id:'mapbox/streets-v10', provider:'mapbox'},
    {name: 'Outdoors', alias:'Mapbox Outdoors', description: 'General basemap tailored to hiking, biking, and sport.', id:'mapbox/outdoors-v10', provider:'mapbox'},
    {name: 'Dark',alias:'Mapbox Dark', description: 'Subtle dark backdrop for data visualizations.', id:'mapbox/dark-v9', provider:'mapbox'},
    {name: 'Light', alias:'Mapbox Light',description: 'Subtle light backdrop for data visualizations.', id:'mapbox/light-v9', provider:'mapbox'},
    {name: 'North Star', alias:'Mapbox North Star',description: 'Slightly modified North Star with no Bathymetry.', id:'blishten/cjg6jk8vg3tir2spd2eatu5fd', provider:'Joint Research Centre'},
    {name: 'Satellite', alias:'Mapbox Satellite',description: 'A beautiful global satellite and aerial imagery layer.', id:'mapbox/satellite-v9', provider:'mapbox'},
    {name: 'Satellite Streets', alias:'Mapbox Satellite Streets',description: 'Global imagery enhanced with road and label hierarchy.', id:'mapbox/satellite-streets-v9', provider:'mapbox'}];
var MARXAN_SERVERS = [{name: 'JRC Development Server', port: 8081, host: '61c92e42cb1042699911c485c38d52ae.vfs.cloud9.eu-west-1.amazonaws.com', protocol:'https:', description: 'Main development server for Marxan Web.',type:'remote'},
                      {name: 'The Nature Conservancy, USA', port: 8080, host: 'pending', protocol:'https:', description: 'Central service for TNC',type:'remote'},
                      {name: 'SPREP Regional Hub, Samoa', port: 8080, host: 'nonexistant', protocol:'https:', description: 'Regional node for BIOPAMA',type:'remote'},
                     {name:'Marxan Web Training Course', port: 8080, host: 'andrewcottam.com',protocol:'https:', description:'Marxan Server specifically for training hosted on Google Cloud Platform. All projects will be deleted at the end.', type:'remote'}];
var WDPA = {latest_version:'September 2019',downloadUrl:'https://www.protectedplanet.net/downloads/WDPA_Sep2019?type=shapefile', tilesUrl:'https://geospatial.jrc.ec.europa.eu/geoserver/gwc/service/wmts?','metadataUrl':'https://www.protectedplanet.net/c/monthly-updates/2019/september-2019-update-of-the-wdpa'};
var MBAT = "sk.eyJ1IjoiYmxpc2h0ZW4iLCJhIjoiY2piNm1tOGwxMG9lajMzcXBlZDR4aWVjdiJ9.Z1Jq4UAgGpXukvnUReLO1g";
var MBAT_PUBLIC = "pk.eyJ1IjoiYmxpc2h0ZW4iLCJhIjoiMEZrNzFqRSJ9.0QBRA2HxTb8YHErUFRMPZg";
var NOTIFICATIONS = [
    {id:1, html:"The <a href='https://andrewcottam.github.io/marxan-web/documentation/docs_betatest.html' target='_blank'>Beta Test Programme</a> ends at the end of October. Let us know what you think!", type:"News", expires: "10/31/2019", showForRoles: ["Admin","User","ReadOnly"]},
    {id:2, html:"Tonga has achieved its marine Aichi Target 11, maybe - see <a href='http://macbio-pacific.info/updates/' target='_blank'>here</a>", type:"News", expires: "", showForRoles: ["Admin","User","ReadOnly"]},
    {id:3, html:"New training course for Marxan Web, maybe", type:"Training", expires: "", showForRoles: ["Admin","User","ReadOnly"]}    
    ];
