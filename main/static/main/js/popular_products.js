document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.popular-section');
    if (!container) return;
    
    const grid = container.querySelector('.products-grid');
    const prevBtn = container.querySelector('.prev-btn');
    const nextBtn = container.querySelector('.next-btn');
    
    let currentPosition = 0;
    let cardWidth = 0;
    let cardsPerView = 0;
    
    function initCarousel() {
        const firstCard = grid.querySelector('.grid-product-card');
        if (!firstCard) return;
        
        cardWidth = firstCard.offsetWidth + 20; // + gap
        cardsPerView = Math.floor(container.offsetWidth / cardWidth);
        
        updateNavigation();
    }
    
    function updateNavigation() {
        const totalCards = grid.querySelectorAll('.grid-product-card').length;
        const maxPosition = Math.ceil(totalCards / cardsPerView) - 1;
        
        if (prevBtn) prevBtn.disabled = currentPosition === 0;
        if (nextBtn) nextBtn.disabled = currentPosition >= maxPosition;
    }
    
    function moveCarousel() {
        grid.style.transform = `translateX(-${currentPosition * cardWidth * cardsPerView}px)`;
        updateNavigation();
    }
    
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            if (currentPosition > 0) {
                currentPosition--;
                moveCarousel();
            }
        });
    }
    
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            const totalCards = grid.querySelectorAll('.grid-product-card').length;
            const maxPosition = Math.ceil(totalCards / cardsPerView) - 1;
            
            if (currentPosition < maxPosition) {
                currentPosition++;
                moveCarousel();
            }
        });
    }
    
    // Инициализация и обработка ресайза
    initCarousel();
    window.addEventListener('resize', initCarousel);
});
