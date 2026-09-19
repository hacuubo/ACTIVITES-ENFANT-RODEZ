/* Sorties Enfants Rodez — application PWA (vanilla JS, sans build) */
(function () {
  'use strict';

  const DATA_URL = 'data/events.json';
  const RODEZ = [44.3506, 2.5750];
  const CAT_META = {
    spectacle: { label: 'Spectacle', emoji: '🎭' },
    atelier:   { label: 'Atelier',   emoji: '🎨' },
    musee:     { label: 'Musée',     emoji: '🏛️' },
    lecture:   { label: 'Lecture',   emoji: '📚' },
    cinema:    { label: 'Cinéma',    emoji: '🎬' },
    sport:     { label: 'Sport',     emoji: '⚽' },
    nature:    { label: 'Nature',    emoji: '🌳' },
    fete:      { label: 'Fête',      emoji: '🎡' },
    stage:     { label: 'Stage',     emoji: '🏕️' },
    jeux:      { label: 'Jeux',      emoji: '🎲' },
    autre:     { label: 'Sortie',    emoji: '✨' },
  };
  const AUDIENCE_LABEL = { enfant: 'Enfant', famille: 'En famille', ados: 'Ados', amis: 'Entre amis' };
  const AGE_RANGES = { '1-2': [1, 2], '3-5': [3, 5], '6-10': [6, 10], '11-15': [11, 15] };

  const state = {
    events: [],
    updatedAt: null,
    view: 'calendar',
    month: startOfMonth(new Date()),
    selected: todayISO(),
    mapDay: todayISO(),
    ages: new Set(['all']),
    favorites: loadFavorites(),
    map: null,
    markers: null,
  };

  // ---------- Utils ----------
  function pad(n) { return String(n).padStart(2, '0'); }
  function toISO(d) { return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()); }
  function fromISO(s) { const [y, m, d] = s.split('-').map(Number); return new Date(y, m - 1, d); }
  function todayISO() { return toISO(new Date()); }
  function startOfMonth(d) { return new Date(d.getFullYear(), d.getMonth(), 1); }
  function addDays(iso, n) { const d = fromISO(iso); d.setDate(d.getDate() + n); return toISO(d); }
  function isoWeekday(iso) { const w = fromISO(iso).getDay(); return w === 0 ? 7 : w; } // 1=lundi … 7=dimanche
  function fmtDayLong(iso) {
    return fromISO(iso).toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' });
  }
  function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
  function fmtDayShort(iso) { return fromISO(iso).toLocaleDateString('fr-FR', { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' }); }
  function fmtMonth(d) { return cap(d.toLocaleDateString('fr-FR', { month: 'long', year: 'numeric' })); }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])); }
  function loadFavorites() {
    try { return new Set(JSON.parse(localStorage.getItem('favorites') || '[]')); } catch { return new Set(); }
  }
  function saveFavorites() {
    try { localStorage.setItem('favorites', JSON.stringify([...state.favorites])); } catch { /* stockage indisponible */ }
  }
  function ageLabel(e) {
    if (e.age_min <= 1 && e.age_max >= 15) return 'Tous âges';
    if (e.age_max >= 15) return `dès ${e.age_min} ans`;
    return `${e.age_min}-${e.age_max} ans`;
  }
  function catOf(e) { return CAT_META[e.category] ? e.category : 'autre'; }
  function mapsUrl(e) {
    const q = e.lat && e.lng ? `${e.lat},${e.lng}` : `${e.venue}, ${e.address}`;
    return 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(q);
  }

  // ---------- Filtrage ----------
  function matchesAge(e) {
    if (state.ages.has('all')) return true;
    for (const key of state.ages) {
      const r = AGE_RANGES[key];
      if (r && e.age_min <= r[1] && e.age_max >= r[0]) return true;
    }
    return false;
  }
  function occursOn(e, iso) {
    const end = e.end_date || e.date;
    if (iso < e.date || iso > end) return false;
    if (Array.isArray(e.days_of_week) && e.days_of_week.length) return e.days_of_week.includes(isoWeekday(iso));
    return true;
  }
  function eventsOn(iso, withFilter = true) {
    return state.events
      .filter(e => occursOn(e, iso) && (!withFilter || matchesAge(e)))
      .sort((a, b) => (a.time || '00:00').localeCompare(b.time || '00:00') || a.title.localeCompare(b.title));
  }

  // ---------- Rendu : cartes événements ----------
  const tpl = document.getElementById('tpl-event');
  function renderEventCard(e, dayIso) {
    const node = tpl.content.firstElementChild.cloneNode(true);
    const cat = catOf(e);
    node.style.setProperty('--cat', `var(--cat-${cat})`);
    node.dataset.id = e.id;
    node.querySelector('.event__time').textContent = e.time ? e.time.replace(':', 'h') : 'Journée';
    node.querySelector('.event__title').textContent = e.title;
    node.querySelector('.event__summary').textContent = e.summary;
    node.querySelector('.badge--city').textContent = '📍 ' + e.city;
    node.querySelector('.badge--age').textContent = ageLabel(e);
    node.querySelector('.badge--cat').textContent = CAT_META[cat].emoji + ' ' + CAT_META[cat].label;
    const fav = node.querySelector('.event__fav');
    const on = state.favorites.has(e.id);
    fav.textContent = on ? '★' : '☆';
    fav.classList.toggle('is-on', on);
    fav.setAttribute('aria-pressed', on);
    fav.addEventListener('click', () => toggleFavorite(e.id));
    node.querySelector('.event__main').addEventListener('click', () => openSheet(e, dayIso));
    return node;
  }
  function renderList(container, events, dayIso, emptyText) {
    container.innerHTML = '';
    if (!events.length) {
      const p = document.createElement('p');
      p.className = 'events__empty';
      p.textContent = emptyText;
      container.appendChild(p);
      return;
    }
    events.forEach(e => container.appendChild(renderEventCard(e, dayIso)));
  }

  // ---------- Vue calendrier ----------
  const calGrid = document.getElementById('cal-grid');
  const calTitle = document.getElementById('cal-title');
  function renderCalendar() {
    calTitle.textContent = fmtMonth(state.month);
    calGrid.innerHTML = '';
    const y = state.month.getFullYear(), m = state.month.getMonth();
    const first = new Date(y, m, 1);
    const offset = (first.getDay() + 6) % 7; // lundi = 0
    const daysInMonth = new Date(y, m + 1, 0).getDate();
    const today = todayISO();
    for (let i = 0; i < offset; i++) {
      const pad = document.createElement('div'); pad.className = 'day day--pad'; calGrid.appendChild(pad);
    }
    for (let d = 1; d <= daysInMonth; d++) {
      const iso = toISO(new Date(y, m, d));
      const evs = eventsOn(iso);
      const btn = document.createElement('button');
      btn.className = 'day';
      btn.type = 'button';
      btn.dataset.date = iso;
      btn.setAttribute('aria-label', cap(fmtDayLong(iso)) + (evs.length ? `, ${evs.length} activité(s)` : ''));
      if (iso === today) btn.classList.add('is-today');
      if (iso === state.selected) btn.classList.add('is-selected');
      if (evs.length) btn.classList.add('has-events');
      let html = `<span>${d}</span>`;
      if (evs.length) {
        const cats = [...new Set(evs.map(catOf))].slice(0, 4);
        html += '<span class="day__dots">' + cats.map(c => `<span class="day__dot" style="--dot:var(--cat-${c})"></span>`).join('') + '</span>';
        html += `<span class="day__count">${evs.length}</span>`;
      } else {
        html += '<span class="day__dots"></span>';
      }
      btn.innerHTML = html;
      btn.addEventListener('click', () => { state.selected = iso; renderCalendar(); renderDayList(); });
      calGrid.appendChild(btn);
    }
  }
  function renderDayList() {
    const evs = eventsOn(state.selected);
    document.getElementById('daylist-title').textContent = cap(fmtDayLong(state.selected)) + (evs.length ? ` · ${evs.length} activité${evs.length > 1 ? 's' : ''}` : '');
    renderList(document.getElementById('daylist'), evs, state.selected, 'Aucune activité trouvée ce jour-là pour cet âge. Essayez un autre jour ou « Tous ».');
  }
  document.getElementById('cal-title').addEventListener('click', () => { state.month = startOfMonth(new Date()); state.selected = todayISO(); renderCalendar(); renderDayList(); });
  document.getElementById('cal-prev').addEventListener('click', () => { state.month = new Date(state.month.getFullYear(), state.month.getMonth() - 1, 1); renderCalendar(); });
  document.getElementById('cal-next').addEventListener('click', () => { state.month = new Date(state.month.getFullYear(), state.month.getMonth() + 1, 1); renderCalendar(); });

  // ---------- Vue jour + carte ----------
  const dayInput = document.getElementById('day-input');
  function ensureMap() {
    if (state.map) return;
    if (typeof L === 'undefined') {
      document.getElementById('map').innerHTML = '<p class="map__fallback">Carte indisponible pour le moment.</p>';
      return;
    }
    state.map = L.map('map', { zoomControl: true, tap: true }).setView(RODEZ, 11);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(state.map);
    state.markers = L.layerGroup().addTo(state.map);
  }
  function renderMapDay() {
    const iso = state.mapDay;
    document.getElementById('day-label').textContent = (iso === todayISO() ? "Aujourd'hui · " : '') + fmtDayShort(iso);
    dayInput.value = iso;
    const evs = eventsOn(iso);
    document.getElementById('map-count').textContent = evs.length ? `${evs.length} activité${evs.length > 1 ? 's' : ''} ce jour.` : 'Aucune activité ce jour.';
    renderList(document.getElementById('maplist'), evs, iso, 'Aucune activité trouvée ce jour-là pour cet âge.');
    ensureMap();
    if (!state.map) return;
    state.markers.clearLayers();
    const bounds = [];
    evs.forEach(e => {
      if (typeof e.lat !== 'number' || typeof e.lng !== 'number') return;
      const cat = catOf(e);
      const icon = L.divIcon({
        className: '',
        html: `<div class="marker" style="--cat:var(--cat-${cat})"><span>${CAT_META[cat].emoji}</span></div>`,
        iconSize: [30, 30], iconAnchor: [15, 30], popupAnchor: [0, -28],
      });
      const mk = L.marker([e.lat, e.lng], { icon, title: e.title });
      mk.bindPopup(`<strong>${esc(e.title)}</strong>${e.time ? esc(e.time.replace(':', 'h')) + ' · ' : ''}${esc(e.venue)}, ${esc(e.city)}<br>${esc(ageLabel(e))} · ${esc(e.price)}<br><button class="popup__btn" data-open="${esc(e.id)}">Voir la fiche</button>`);
      mk.on('popupopen', ev => {
        const btn = ev.popup.getElement().querySelector('[data-open]');
        if (btn) btn.addEventListener('click', () => openSheet(e, iso));
      });
      state.markers.addLayer(mk);
      bounds.push([e.lat, e.lng]);
    });
    setTimeout(() => {
      state.map.invalidateSize();
      if (bounds.length > 1) state.map.fitBounds(bounds, { padding: [30, 30], maxZoom: 14 });
      else if (bounds.length === 1) state.map.setView(bounds[0], 13);
      else state.map.setView(RODEZ, 11);
    }, 50);
  }
  document.getElementById('day-prev').addEventListener('click', () => { state.mapDay = addDays(state.mapDay, -1); renderMapDay(); });
  document.getElementById('day-next').addEventListener('click', () => { state.mapDay = addDays(state.mapDay, 1); renderMapDay(); });
  document.getElementById('day-today').addEventListener('click', () => { state.mapDay = todayISO(); renderMapDay(); });
  dayInput.addEventListener('change', () => { if (dayInput.value) { state.mapDay = dayInput.value; renderMapDay(); } });

  // ---------- Vue favoris ----------
  function renderFavorites() {
    const container = document.getElementById('favlist');
    container.innerHTML = '';
    const favs = state.events.filter(e => state.favorites.has(e.id)).sort((a, b) => a.date.localeCompare(b.date) || (a.time || '').localeCompare(b.time || ''));
    if (!favs.length) {
      renderList(container, [], null, 'Aucun favori pour le moment. Touchez ☆ sur une activité pour l’ajouter.');
      return;
    }
    let lastDate = null;
    favs.forEach(e => {
      if (e.date !== lastDate) {
        const h = document.createElement('h3');
        h.className = 'events__group';
        h.textContent = cap(fmtDayLong(e.date)) + (e.end_date && e.end_date !== e.date ? ' → ' + fmtDayLong(e.end_date) : '');
        container.appendChild(h);
        lastDate = e.date;
      }
      container.appendChild(renderEventCard(e, e.date));
    });
  }
  function toggleFavorite(id) {
    if (state.favorites.has(id)) state.favorites.delete(id); else state.favorites.add(id);
    saveFavorites();
    document.querySelectorAll(`.event[data-id="${CSS.escape(id)}"] .event__fav`).forEach(b => {
      const on = state.favorites.has(id);
      b.textContent = on ? '★' : '☆'; b.classList.toggle('is-on', on); b.setAttribute('aria-pressed', on);
    });
    const sheetFav = document.querySelector('#sheet [data-fav]');
    if (sheetFav && sheetFav.dataset.fav === id) sheetFav.textContent = state.favorites.has(id) ? '★ Retirer des favoris' : '☆ Ajouter aux favoris';
    if (state.view === 'favorites') renderFavorites();
  }

  // ---------- Fiche détaillée ----------
  const sheet = document.getElementById('sheet');
  const sheetContent = document.getElementById('sheet-content');
  function openSheet(e, dayIso) {
    const cat = catOf(e);
    const when = [];
    if (e.end_date && e.end_date !== e.date) {
      when.push(`Du ${fmtDayLong(e.date)} au ${fmtDayLong(e.end_date)}`);
      if (Array.isArray(e.days_of_week) && e.days_of_week.length) {
        const names = ['', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche'];
        when.push('les ' + e.days_of_week.map(d => names[d]).join(', '));
      }
    } else {
      when.push(cap(fmtDayLong(e.date)));
    }
    const hours = e.time ? (e.time.replace(':', 'h') + (e.end_time ? ' – ' + e.end_time.replace(':', 'h') : '')) : 'Toute la journée';
    const tel = e.phone ? e.phone.replace(/\s+/g, '') : null;
    const fav = state.favorites.has(e.id);
    sheetContent.innerHTML = `
      <span class="badge badge--cat sheet__cat" style="--cat:var(--cat-${cat})">${CAT_META[cat].emoji} ${CAT_META[cat].label}</span>
      <h2 id="sheet-title">${esc(e.title)}</h2>
      <p class="sheet__when">📆 ${esc(when.join(' '))} · ⏰ ${esc(hours)}</p>
      <p class="muted">${esc(e.summary)}</p>
      ${e.description ? `<p class="sheet__desc">${esc(e.description)}</p>` : ''}
      <dl class="info">
        <dt>👶</dt><dd>${esc(ageLabel(e))} · ${esc(AUDIENCE_LABEL[e.audience] || e.audience || '')}</dd>
        <dt>📍</dt><dd><a href="${mapsUrl(e)}" target="_blank" rel="noopener">${esc(e.venue)}</a><small>${esc(e.address)} · ${esc(e.city)}</small></dd>
        <dt>💶</dt><dd>${esc(e.price || 'Non communiqué')}${e.booking_required ? '<small>Réservation obligatoire</small>' : ''}</dd>
        ${tel ? `<dt>📞</dt><dd><a href="tel:${esc(tel)}">${esc(e.phone)}</a></dd>` : ''}
        ${e.email ? `<dt>✉️</dt><dd><a href="mailto:${esc(e.email)}">${esc(e.email)}</a></dd>` : ''}
      </dl>
      ${Array.isArray(e.tags) && e.tags.length ? `<div class="tags">${e.tags.map(t => `<span class="badge">#${esc(t)}</span>`).join('')}</div>` : ''}
      <div class="sheet__actions">
        <a class="btn btn--primary btn--link" href="${mapsUrl(e)}" target="_blank" rel="noopener">🗺️ Y aller (Google Maps)</a>
        ${e.booking_url ? `<a class="btn btn--link" href="${esc(e.booking_url)}" target="_blank" rel="noopener">🎟️ Réserver</a>` : ''}
        ${e.url ? `<a class="btn btn--link" href="${esc(e.url)}" target="_blank" rel="noopener">🔗 Site officiel</a>` : ''}
        <button class="btn btn--link" type="button" data-fav="${esc(e.id)}">${fav ? '★ Retirer des favoris' : '☆ Ajouter aux favoris'}</button>
      </div>
      ${e.source ? `<p class="sheet__source">Source : <a href="${esc(e.source)}" target="_blank" rel="noopener">${esc(new URL(e.source).hostname)}</a>${e.source_checked ? ' · vérifié le ' + esc(fmtDayLong(e.source_checked)) : ''}</p>` : ''}
    `;
    sheetContent.querySelector('[data-fav]').addEventListener('click', () => toggleFavorite(e.id));
    sheet.hidden = false;
    document.body.style.overflow = 'hidden';
  }
  function closeSheet() { sheet.hidden = true; document.body.style.overflow = ''; }
  sheet.querySelectorAll('[data-close]').forEach(el => el.addEventListener('click', closeSheet));
  document.addEventListener('keydown', ev => { if (ev.key === 'Escape' && !sheet.hidden) closeSheet(); });

  // ---------- Navigation ----------
  function setView(view) {
    state.view = view;
    document.querySelectorAll('.tab').forEach(t => {
      const on = t.dataset.view === view;
      t.classList.toggle('is-active', on); t.setAttribute('aria-selected', on);
    });
    document.querySelectorAll('.view').forEach(v => { v.hidden = v.id !== 'view-' + view; v.classList.toggle('is-active', v.id === 'view-' + view); });
    if (view === 'map') { state.mapDay = state.selected || todayISO(); renderMapDay(); }
    if (view === 'favorites') renderFavorites();
    try { localStorage.setItem('view', view); } catch { /* ignore */ }
  }
  document.querySelectorAll('.tab').forEach(t => t.addEventListener('click', () => setView(t.dataset.view)));

  document.getElementById('age-chips').addEventListener('click', ev => {
    const chip = ev.target.closest('.chip'); if (!chip) return;
    const key = chip.dataset.age;
    if (key === 'all') state.ages = new Set(['all']);
    else {
      state.ages.delete('all');
      if (state.ages.has(key)) state.ages.delete(key); else state.ages.add(key);
      if (!state.ages.size) state.ages.add('all');
    }
    document.querySelectorAll('#age-chips .chip').forEach(c => c.classList.toggle('is-active', state.ages.has(c.dataset.age)));
    try { localStorage.setItem('ages', JSON.stringify([...state.ages])); } catch { /* ignore */ }
    rerender();
  });

  function rerender() {
    renderCalendar(); renderDayList();
    if (state.view === 'map') renderMapDay();
    if (state.view === 'favorites') renderFavorites();
  }

  // ---------- Chargement des données ----------
  async function loadData() {
    const label = document.getElementById('updated-at');
    try {
      const res = await fetch(DATA_URL + '?t=' + Date.now(), { cache: 'no-store' });
      if (!res.ok) throw new Error('HTTP ' + res.status);
      const json = await res.json();
      applyData(json);
      try { localStorage.setItem('events-cache', JSON.stringify(json)); } catch { /* quota */ }
    } catch (err) {
      let cached = null;
      try { cached = JSON.parse(localStorage.getItem('events-cache') || 'null'); } catch { /* ignore */ }
      if (cached) { applyData(cached); label.textContent += ' (hors ligne)'; }
      else label.textContent = 'Impossible de charger les activités.';
    }
  }
  function applyData(json) {
    state.events = (json.events || []).filter(e => e && e.id && e.date && e.title);
    state.updatedAt = json.updated_at || null;
    const label = document.getElementById('updated-at');
    if (state.updatedAt) {
      const d = new Date(state.updatedAt);
      label.textContent = `${state.events.length} activités · mis à jour le ${d.toLocaleDateString('fr-FR', { day: 'numeric', month: 'long' })}`;
    } else label.textContent = `${state.events.length} activités`;
    rerender();
  }

  // ---------- PWA : installation + service worker ----------
  let deferredPrompt = null;
  const installBtn = document.getElementById('btn-install');
  window.addEventListener('beforeinstallprompt', ev => { ev.preventDefault(); deferredPrompt = ev; installBtn.hidden = false; });
  installBtn.addEventListener('click', async () => {
    if (!deferredPrompt) return;
    deferredPrompt.prompt();
    await deferredPrompt.userChoice;
    deferredPrompt = null; installBtn.hidden = true;
  });
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));
  }

  // ---------- Init ----------
  try {
    const savedAges = JSON.parse(localStorage.getItem('ages') || 'null');
    if (Array.isArray(savedAges) && savedAges.length) {
      state.ages = new Set(savedAges);
      document.querySelectorAll('#age-chips .chip').forEach(c => c.classList.toggle('is-active', state.ages.has(c.dataset.age)));
    }
  } catch { /* ignore */ }
  renderCalendar(); renderDayList();
  loadData();
})();
