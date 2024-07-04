# PKGBUILD para el paquete downloader-yt

pkgname=downloader-yt
pkgver=1.0
pkgrel=1
pkgdesc="Descargador de videos de YouTube"
arch=('x86_64')
url="https://github.com/Edgarmejiav/downloader-yt"
license=('MIT')
depends=('python' 'yt-dlp')

package() {
    cd "$srcdir"
    mkdir -p "$pkgdir/usr/bin"
    cp download-yt.py "$pkgdir/usr/bin/downloader-yt"
    chmod +x "$pkgdir/usr/bin/downloader-yt"
}
