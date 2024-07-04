# PKGBUILD para el paquete downloader-yt

pkgname=downloader-yt
pkgver=1.0
pkgrel=1
pkgdesc="Un paquete que saluda con la hora actual y el nombre proporcionado."
arch=('any')
url="https://example.com/downloader-yt"
license=('MIT')
depends=('python' 'python-pytube')

package() {
    cd "$srcdir"
    echo "Instalando el paquete... $srcdir "
    mkdir -p "$pkgdir/usr/bin"
    cp download-yt.py "$pkgdir/usr/bin/downloader-yt"
    chmod +x "$pkgdir/usr/bin/downloader-yt"
}
