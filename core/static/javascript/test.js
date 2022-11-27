const client = new WebTorrent()

// Sintel, a free, Creative Commons movie
const torrentId = 'magnet:?xt=urn:btih:1c333ff936b8634d206378350579e2ffc118bfc1'

client.add(torrentId, function(torrent) {
  const file = torrent.files.find(function(file) {
    return file.name.endsWith('.mkv')
  })

  file.renderTo("#video", {
    autoplay: true,
    muted: true
  })
})