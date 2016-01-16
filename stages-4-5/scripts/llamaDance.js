function changeImage() {
    var image = document.getElementById('myImage');
    if (image.src.match('YcxNnQt')) {
        image.src = 'http://i.imgur.com/BBLXmzG.jpg';
    } else {
        image.src = 'http://i.imgur.com/YcxNnQt.jpg';
    }
}
