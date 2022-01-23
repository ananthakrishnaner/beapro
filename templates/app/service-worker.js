const staticCacheName = 'site-static';
const assets = [
    'https://fonts.googleapis.com/css?family=Lato:400,700&display=swap',
    'https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap',
    'https://fonts.gstatic.com/s/poppins/v15/pxiByp8kv8JHgFVrLDz8Z11lFd2JQEl8qw.woff2',
    'https://fonts.gstatic.com/s/poppins/v15/pxiByp8kv8JHgFVrLDz8Z1xlFd2JQEk.woff2',
    'https://fonts.gstatic.com/s/lato/v17/S6uyw4BMUTPHjx4wXg.woff2',


];


//Service worker install
self.addEventListener('install', evt => {
    evt.waitUntil(
        caches.open(staticCacheName).then(cache => {
            console.log('caches store');
            cache.addAll(assets);
        })
    );

});

//Activating Service worker

self.addEventListener('activate', evt => {
    console.log('service worker activated');
});

// fetch

self.addEventListener('fetch', evt => {
    console.log("fetch")
});
