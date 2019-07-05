var MAPBOX_BASEMAPS = [{name: 'Streets', description: 'A complete basemap, perfect for incorporating your own data.', id:'mapbox/streets-v10', provider:'mapbox'},
    {name: 'Outdoors', description: 'General basemap tailored to hiking, biking, and sport.', id:'mapbox/outdoors-v10', provider:'mapbox'},
    {name: 'Dark', description: 'Subtle dark backdrop for data visualizations.', id:'mapbox/dark-v9', provider:'mapbox'},
    {name: 'Light', description: 'Subtle light backdrop for data visualizations.', id:'mapbox/light-v9', provider:'mapbox'},
    {name: 'North Star', description: 'Slightly modified North Star with no Bathymetry.', id:'blishten/cjg6jk8vg3tir2spd2eatu5fd', provider:'Joint Research Centre'},
    {name: 'Satellite', description: 'A beautiful global satellite and aerial imagery layer.', id:'mapbox/satellite-v9', provider:'mapbox'},
    {name: 'Satellite Streets', description: 'Global imagery enhanced with road and label hierarchy.', id:'mapbox/satellite-streets-v9', provider:'mapbox'}];
var MARXAN_SERVERS = [{name: 'JRC Development Server', port: 8081, host: '61c92e42cb1042699911c485c38d52ae.vfs.cloud9.eu-west-1.amazonaws.com', protocol:'https:', description: 'Main development server for Marxan Web.',type:'remote'},
                      {name: 'The Nature Conservancy, USA', port: 8080, host: 'pending', protocol:'https:', description: 'Central service for TNC',type:'remote'},
                      {name: 'SPREP Regional Hub, Samoa', port: 8080, host: 'nonexistant', protocol:'https:', description: 'Regional node for BIOPAMA',type:'remote'},
                     {name:'Beta test', port: 8080, host: 'andrewcottam.com',protocol:'https:', description:'Beta test Marxan Server hosted on Google Cloud Platform. All projects will be deleted at the end.', type:'remote'}]
