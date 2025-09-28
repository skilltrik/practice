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
