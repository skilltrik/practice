const tg = window.Telegram.WebApp;

const products = [
  { id: 1, name: 'Яблоко', image: 'https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg' },
  { id: 2, name: 'Банан', image: 'https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg' },
  { id: 3, name: 'Апельсин', image: 'https://upload.wikimedia.org/wikipedia/commons/c/c4/Orange-Fruit-Pieces.jpg' },
  { id: 4, name: 'Клубника', image: 'https://upload.wikimedia.org/wikipedia/commons/2/29/PerfectStrawberry.jpg' }
];

const cart = {};
const productsContainer = document.getElementById('products-container');
const cartButton = document.getElementById('cart-button');
const productsPage = document.getElementById('products-page');
const cartPage = document.getElementById('cart-page');
const checkoutPage = document.getElementById('checkout-page');
const cartList = document.getElementById('cart-list');

function renderProducts() {
  productsContainer.innerHTML = '';
  products.forEach(product => {
    const count = cart[product.id] || 0;
    const productEl = document.createElement('div');
    productEl.className = 'product';
    productEl.innerHTML = `
      <img src="${product.image}" alt="${product.name}">
      <h3>${product.name}</h3>
    `;

    if (count === 0) {
      const addButton = document.createElement('button');
      addButton.className = 'add-btn';
      addButton.textContent = 'Добавить в корзину';
      addButton.onclick = () => {
        cart[product.id] = 1;
        updateCartUI();
      };
      productEl.appendChild(addButton);
    } else {
      const controls = document.createElement('div');
      controls.className = 'cart-controls';
      controls.innerHTML = `
        <button class="circle-btn" onclick="updateCount(${product.id}, -1)">−</button>
        <span>${count}</span>
        <button class="circle-btn" onclick="updateCount(${product.id}, 1)">+</button>
      `;
      productEl.appendChild(controls);
    }

    productsContainer.appendChild(productEl);
  });
}

function updateCount(id, delta) {
  cart[id] = (cart[id] || 0) + delta;
  if (cart[id] <= 0) delete cart[id];
  updateCartUI();
}

function updateCartUI() {
  renderProducts();
  const totalItems = Object.values(cart).reduce((sum, val) => sum + val, 0);
  cartButton.style.display = totalItems > 0 ? 'block' : 'none';
}

cartButton.onclick = () => {
  productsPage.style.display = 'none';
  cartPage.style.display = 'block';
  renderCart();
};

function renderCart() {
  cartList.innerHTML = '';
  if (Object.keys(cart).length === 0) {
    cartList.innerHTML = '<p style="text-align:center;">Корзина пуста</p>';
    return;
  }
  Object.keys(cart).forEach(id => {
    const product = products.find(p => p.id == id);
    const div = document.createElement('div');
    div.className = 'cart-item';
    div.textContent = `${product.name} ..... ${cart[id]} шт.`;
    cartList.appendChild(div);
  });
}

document.getElementById('checkout-button').onclick = () => {
  cartPage.style.display = 'none';
  checkoutPage.style.display = 'block';
};

document.getElementById('order-button').onclick = () => {
  const name = document.getElementById('name').value.trim();
  const phone = document.getElementById('phone').value.trim();
  if (!name || !phone) {
    alert('Заполните все поля');
    return;
  }

  const orderData = {
    name,
    phone,
    cart: Object.keys(cart).map(id => ({
      name: products.find(p => p.id == id).name,
      quantity: cart[id]
    }))
  };

  tg.sendData(JSON.stringify(orderData)); // Отправка данных в бота
  tg.close(); // Закрыть WebApp
};

renderProducts();

document.getElementById('back-to-products').onclick = () => {
  cartPage.style.display = 'none';
  productsPage.style.display = 'block';
};

document.getElementById('back-to-cart').onclick = () => {
  checkoutPage.style.display = 'none';
  cartPage.style.display = 'block';
};
