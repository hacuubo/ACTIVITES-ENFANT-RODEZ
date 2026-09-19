/* Service worker : coquille applicative hors ligne, données réseau d'abord. */
const VERSION = 'v1';
const SHELL_CACHE = 'shell-' + VERSION;
const DATA_CACHE = 'data-' + VERSION;
const SHELL = [
  './', './index.html', './styles.css', './app.js', './manifest.webmanifest',
  './icons/icon.svg', './icons/icon-192.png', './icons/icon-512.png',
  './vendor/leaflet/leaflet.min.css', './vendor/leaflet/leaflet.min.js',
  './vendor/leaflet/images/layers.png', './vendor/leaflet/images/layers-2x.png',
];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(SHELL_CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(keys.filter(k => k !== SHELL_CACHE && k !== DATA_CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  if (event.request.method !== 'GET') return;

  // Données : réseau d'abord, repli sur le cache.
  if (url.pathname.endsWith('/data/events.json')) {
    event.respondWith(
      fetch(event.request).then(res => {
        const copy = res.clone();
        caches.open(DATA_CACHE).then(c => c.put(url.pathname, copy));
        return res;
      }).catch(() => caches.match(url.pathname))
    );
    return;
  }
  // Tuiles de carte : jamais mises en cache (trop volumineuses).
  if (url.hostname.endsWith('tile.openstreetmap.org')) return;

  // Coquille : cache d'abord, puis réseau (et mise en cache).
  event.respondWith(
    caches.match(event.request, { ignoreSearch: true }).then(hit => hit || fetch(event.request).then(res => {
      if (res.ok && url.origin === location.origin) {
        const copy = res.clone();
        caches.open(SHELL_CACHE).then(c => c.put(event.request, copy));
      }
      return res;
    }))
  );
});
