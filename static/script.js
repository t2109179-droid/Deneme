document.getElementById('btn-istek').addEventListener('click', function() {
    const btn = this;
    const sonucKutusu = document.getElementById('sonuc-kutusu');

    btn.innerText = 'Gönderiliyor...';

    // Python sunucusundaki /api/istek-at endpoint'ine istek atıyoruz
    fetch('/api/istek-at')
        .then(response => response.json())
        .then(data => {
            sonucKutusu.innerText = data.mesaj;
            btn.innerText = 'Python Sunucusuna İstek At';
        })
        .catch(err => {
            console.error('Hata:', err);
            sonucKutusu.innerText = 'Sunucuya ulaşılamadı!';
            btn.innerText = 'Tekrar Deneyin';
        });
});
