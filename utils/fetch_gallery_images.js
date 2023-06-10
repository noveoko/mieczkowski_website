let products = [];
let divs = document.querySelectorAll('.highslide-gallery');
divs.forEach((div) => {
    let productImages = [];
    let description = '';
    let images = div.getElementsByTagName('img');
    for(let i = 0; i < images.length; i++) {
        let img = images[i];
        if (i === 0) {
            description = img.alt;
        }
        productImages.push(img.src);
    }
    let product = {
        description: description,
        images: productImages
    }
    products.push(product);
});
console.log(JSON.stringify(products));