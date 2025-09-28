// ==== Header скрывается при прокрутке вниз ====
let lastScrollY = window.scrollY;
const header = document.getElementById("site-header");

window.addEventListener("scroll", () => {
    if (window.scrollY > lastScrollY) {
        header.classList.add("hide"); // вниз
    } else {
        header.classList.remove("hide"); // вверх
    }
    lastScrollY = window.scrollY;
});

// ==== Эффект "главного пункта" в программе ====
document.addEventListener("scroll", function () {
    const items = document.querySelectorAll(".program-list li");
    const centerY = window.scrollY + window.innerHeight / 2;
    items.forEach((item) => {
        const rect = item.getBoundingClientRect();
        const top = rect.top + window.scrollY;
        const bottom = top + rect.height;
        if (centerY >= top && centerY <= bottom) item.classList.add("active");
        else item.classList.remove("active");
    });
});

// ==== Галерея с "выделенной" центральной картинкой ====
document.addEventListener('DOMContentLoaded', () => {
    const galleryItems = document.querySelectorAll(".gallery-item");
    const leftArrow = document.querySelector(".gallery-arrow.left");
    const rightArrow = document.querySelector(".gallery-arrow.right");

    let currentIndex = 0;

    function updateGallery() {
        galleryItems.forEach((item, index) => {
            item.classList.remove("center", "left", "right", "hidden");

            if (index === currentIndex) {
                item.classList.add("center");
            } else if (index === (currentIndex - 1 + galleryItems.length) % galleryItems.length) {
                item.classList.add("left");
            } else if (index === (currentIndex + 1) % galleryItems.length) {
                item.classList.add("right");
            } else {
                item.classList.add("hidden");
            }
        });
    }

    leftArrow.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + galleryItems.length) % galleryItems.length;
        updateGallery();
    });

    rightArrow.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % galleryItems.length;
        updateGallery();
    });

    // Инициализация
    updateGallery();

    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.querySelector('.lightbox-img');
    const closeBtn = document.querySelector('.lightbox .close');

    // Вешаем клик на все картинки галереи
    document.querySelectorAll('.gallery-item img').forEach(img => {
        img.addEventListener('click', () => {
            lightbox.style.display = 'flex';
            lightboxImg.src = img.src;
        });
    });

    // Закрытие по крестику
    closeBtn.addEventListener('click', () => {
        lightbox.style.display = 'none';
    });

    // Закрытие при клике вне картинки
    lightbox.addEventListener('click', e => {
        if (e.target === lightbox) {
            lightbox.style.display = 'none';
        }
    });
});




(function(){
const carousel = document.getElementById('showcaseCarousel');
const track = carousel.querySelector('.carousel-track');
const items = Array.from(track.children);
let btnPrev = carousel.querySelector('.carousel-arrow.left');
let btnNext = carousel.querySelector('.carousel-arrow.right');
let index = 0;


if (btnNext && !btnPrev) {
const newPrev = document.createElement('button');
newPrev.className = 'carousel-arrow left';
newPrev.setAttribute('aria-label', 'Предыдущая секция');
newPrev.innerHTML = '‹';
carousel.insertBefore(newPrev, carousel.firstChild);
btnPrev = newPrev;
}


function update(){ track.style.transform = `translateX(-${index * 100}%)`; }
btnPrev.addEventListener('click', ()=>{ index = (index - 1 + items.length) % items.length; update(); });
btnNext.addEventListener('click', ()=>{ index = (index + 1) % items.length; update(); });


items.forEach(section => {
const thumbs = section.querySelectorAll('.showcase-thumbs img');
const main = section.querySelector('.showcase-main');
thumbs.forEach(thumb => {
thumb.addEventListener('click', ()=>{
const large = thumb.dataset.large || thumb.src;
main.style.opacity = 0;
setTimeout(()=>{ main.src = large; main.style.opacity = 1; }, 120);
});
});
});


document.addEventListener('keydown', (e)=>{ if(e.key==='ArrowLeft') btnPrev.click(); if(e.key==='ArrowRight') btnNext.click(); });


(function addSwipe(el){
let startX=0, dx=0, threshold=40;
el.addEventListener('touchstart', e=>{ startX=e.touches[0].clientX; dx=0; });
el.addEventListener('touchmove', e=>{ dx=e.touches[0].clientX-startX; });
el.addEventListener('touchend', ()=>{ if(dx>threshold) btnPrev.click(); else if(dx<-threshold) btnNext.click(); });
})(carousel.querySelector('.carousel-viewport'));


update();
})();