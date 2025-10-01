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

// toggle mobile menu
(function(){
  const btn = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.top-nav');
  if (!btn || !nav) return;
  btn.addEventListener('click', (e) => {
    nav.classList.toggle('open');
    btn.classList.toggle('active');
    // чтобы клик по пустому месту закрывал меню
    if (nav.classList.contains('open')) {
      setTimeout(() => {
        document.addEventListener('click', closeOnOutside);
      }, 0);
    } else {
      document.removeEventListener('click', closeOnOutside);
    }
  });
  function closeOnOutside(e){
    if (!nav.contains(e.target) && !btn.contains(e.target)) {
      nav.classList.remove('open');
      btn.classList.remove('active');
      document.removeEventListener('click', closeOnOutside);
    }
  }
})();

document.querySelectorAll('.toggle-details').forEach(button => {
    button.addEventListener('click', () => {
        const card = button.closest('.course-card');
        const details = card.querySelector('.course-details');

        // закрываем все открытые
        document.querySelectorAll('.course-details').forEach(d => {
            if (d !== details) {
                d.style.display = 'none';
                d.previousElementSibling.textContent = 'Посмотреть подробнее';
            }
        });

        // переключаем текущее
        if (details.style.display === 'block') {
            details.style.display = 'none';
            button.textContent = 'Посмотреть подробнее';
        } else {
            details.style.display = 'block';
            button.textContent = 'Скрыть';
        }
    });
});


const phone = "79894689525"; 
const text = "Здравствуйте! Хочу записаться на курс.";
document.querySelectorAll(".whatsapp-btn").forEach(link => {
  link.href = `https://wa.me/${phone}?text=${encodeURIComponent(text)}`;
});

const address = document.getElementById('address').textContent;
document.getElementById('showMap').addEventListener('click', () => {
    const url = `https://2gis.ru/search/${encodeURIComponent(address)}`;
    window.open(url, '_blank');
});
