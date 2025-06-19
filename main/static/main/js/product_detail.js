document.addEventListener('DOMContentLoaded', function() {
    // Получаем все элементы
    const thumbnails = document.querySelectorAll('.thumbnail');
    const mainImage = document.querySelector('.main-image');
    
    // Добавляем обработчик клика для каждой миниатюры
    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            // Удаляем класс active у всех миниатюр
            thumbnails.forEach(t => t.classList.remove('active'));
            
            // Добавляем класс active текущей миниатюре
            this.classList.add('active');
            
            // Обновляем основное изображение
            const img = this.querySelector('img');
            mainImage.src = img.src;
            mainImage.alt = img.alt;
        });
    });
    
    // Опционально: можно добавить навигацию стрелками
    let currentIndex = 0;
    
    function showImage(index) {
        // Проверяем границы
        if (index < 0) index = thumbnails.length - 1;
        if (index >= thumbnails.length) index = 0;
        
        // Обновляем текущий индекс
        currentIndex = index;
        
        // Обновляем активную миниатюру
        thumbnails.forEach((t, i) => {
            t.classList.toggle('active', i === currentIndex);
        });
        
        // Обновляем основное изображение
        const activeThumbnail = thumbnails[currentIndex];
        const img = activeThumbnail.querySelector('img');
        mainImage.src = img.src;
        mainImage.alt = img.alt;
    }
    
    
    document.querySelector('.main-image-container').insertAdjacentHTML('beforeend', navHTML);
    
    // Обработчики для кнопок навигации
    document.querySelector('.prev').addEventListener('click', () => showImage(currentIndex - 1));
    document.querySelector('.next').addEventListener('click', () => showImage(currentIndex + 1));
    
    // Инициализация - показываем первое изображение
    showImage(0);
});



