




// JS for any additional interactivity can go here

// Example: Stop and start the product slider on hover
const slider = document.querySelector('.slide-track');

slider.addEventListener('mouseenter', () => {
    slider.style.animationPlayState = 'paused';
});

slider.addEventListener('mouseleave', () => {
    slider.style.animationPlayState = 'running';
});






// JS to enhance the user experience

// Example: You can add functions to handle adding items to cart, liking products, etc.
document.querySelectorAll('.like').forEach((likeButton) => {
    likeButton.addEventListener('click', function() {
        this.classList.toggle('liked');
        this.querySelector('i').classList.toggle('fa-heart');
        this.querySelector('i').classList.toggle('fa-heart-o');
    });
});

document.querySelectorAll('.add-to-cart').forEach((cartButton) => {
    cartButton.addEventListener('click', function() {
        alert('Produit ajouté au panier!');
    });
});




// Bien etre





/**=======================================================================================*/


