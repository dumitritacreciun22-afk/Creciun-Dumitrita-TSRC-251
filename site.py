<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Luxury Brand Shop</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: Arial, sans-serif;
    }

    body {
      background: #f5f5f5;
      color: #222;
    }

    header {
      background: #111;
      color: white;
      padding: 20px 40px;
      position: sticky;
      top: 0;
      z-index: 1000;
    }

    .top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 15px;
    }

    .logo {
      font-size: 28px;
      font-weight: bold;
      letter-spacing: 2px;
    }

    nav a {
      color: white;
      text-decoration: none;
      margin: 0 12px;
      font-weight: bold;
      transition: 0.3s;
    }

    nav a:hover {
      color: #d4af37;
    }

    .cart-icon {
      background: #d4af37;
      color: #111;
      padding: 10px 16px;
      border-radius: 8px;
      font-weight: bold;
    }

    .hero {
      background: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)),
      url('https://images.unsplash.com/photo-1445205170230-053b83016050?auto=format&fit=crop&w=1400&q=80') center/cover no-repeat;
      color: white;
      text-align: center;
      padding: 100px 20px;
    }

    .hero h1 {
      font-size: 48px;
      margin-bottom: 15px;
    }

    .hero p {
      font-size: 20px;
      margin-bottom: 25px;
    }

    .hero button {
      padding: 14px 28px;
      border: none;
      background: #d4af37;
      color: #111;
      font-size: 16px;
      font-weight: bold;
      border-radius: 8px;
      cursor: pointer;
    }

    .section {
      width: 90%;
      max-width: 1300px;
      margin: 50px auto;
    }

    .section h2 {
      text-align: center;
      margin-bottom: 30px;
      font-size: 34px;
      color: #111;
    }

    .products {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 25px;
    }

    .product-card {
      background: white;
      border-radius: 14px;
      overflow: hidden;
      box-shadow: 0 4px 14px rgba(0,0,0,0.12);
      transition: 0.3s;
    }

    .product-card:hover {
      transform: translateY(-6px);
    }

    .product-card img {
      width: 100%;
      height: 320px;
      object-fit: cover;
    }

    .product-info {
      padding: 18px;
    }

    .product-info h3 {
      margin-bottom: 10px;
      font-size: 22px;
    }

    .price {
      color: #b22222;
      font-size: 22px;
      font-weight: bold;
      margin-bottom: 10px;
    }

    .product-info p {
      margin-bottom: 8px;
      color: #555;
      font-size: 15px;
    }

    .size {
      font-weight: bold;
      color: #222;
    }

    .product-info button {
      margin-top: 12px;
      width: 100%;
      padding: 12px;
      border: none;
      background: #111;
      color: white;
      border-radius: 8px;
      cursor: pointer;
      font-size: 15px;
      font-weight: bold;
      transition: 0.3s;
    }

    .product-info button:hover {
      background: #d4af37;
      color: #111;
    }

    .cart-section {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 30px;
      align-items: start;
    }

    .cart-box, .contact-box, .about-box {
      background: white;
      padding: 25px;
      border-radius: 14px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    }

    #cart-items {
      list-style: none;
      margin-top: 15px;
    }

    #cart-items li {
      padding: 12px 0;
      border-bottom: 1px solid #ddd;
      display: flex;
      justify-content: space-between;
      gap: 10px;
      font-size: 15px;
    }

    .cart-summary h3 {
      margin-bottom: 20px;
      font-size: 24px;
    }

    .total {
      font-size: 24px;
      font-weight: bold;
      margin: 20px 0;
      color: #b22222;
    }

    .checkout-btn, .clear-btn {
      width: 100%;
      padding: 12px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-size: 15px;
      font-weight: bold;
      margin-bottom: 10px;
    }

    .checkout-btn {
      background: #d4af37;
      color: #111;
    }

    .clear-btn {
      background: #111;
      color: white;
    }

    .about-box p,
    .contact-box p {
      margin-bottom: 10px;
      color: #555;
      line-height: 1.6;
    }

    .contact-box input,
    .contact-box textarea {
      width: 100%;
      padding: 12px;
      margin-top: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 8px;
      font-size: 15px;
    }

    .contact-box button {
      background: #111;
      color: white;
      border: none;
      padding: 12px 20px;
      border-radius: 8px;
      cursor: pointer;
      font-weight: bold;
    }

    footer {
      background: #111;
      color: white;
      text-align: center;
      padding: 25px 15px;
      margin-top: 50px;
    }

    @media (max-width: 900px) {
      .cart-section {
        grid-template-columns: 1fr;
      }

      .hero h1 {
        font-size: 34px;
      }

      .hero p {
        font-size: 18px;
      }

      .top-bar {
        flex-direction: column;
        align-items: flex-start;
      }

      nav {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
      }

      nav a {
        margin: 0;
      }
    }
  </style>
</head>
<body>

  <header>
    <div class="top-bar">
      <div class="logo">LUXURY BRAND</div>
      <nav>
        <a href="#home">Acasă</a>
        <a href="#produse">Produse</a>
        <a href="#despre">Despre</a>
        <a href="#contact">Contact</a>
        <a href="#cos">Coș</a>
      </nav>
      <div class="cart-icon">Coș: <span id="cart-count">0</span></div>
    </div>
  </header>

  <section class="hero" id="home">
    <h1>Magazin Online de Haine de Brand</h1>
    <p>Stil premium, calitate superioară și colecții moderne pentru un look perfect.</p>
    <button onclick="document.getElementById('produse').scrollIntoView({behavior:'smooth'})">Vezi Produsele</button>
  </section>

  <section class="section" id="produse">
    <h2>Produsele Noastre</h2>
    <div class="products">

      <div class="product-card">
        <img src="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=800&q=80" alt="Tricou premium">
        <div class="product-info">
          <h3>Tricou Premium White</h3>
          <div class="price">129 lei</div>
          <p>Tricou elegant pentru ținute casual și moderne.</p>
          <p><span class="size">Mărimi:</span> S, M, L, XL</p>
          <p><span class="size">Material:</span> 100% bumbac premium</p>
          <button onclick="addToCart('Tricou Premium White', 129)">Adaugă în coș</button>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=800&q=80" alt="Hanorac luxury">
        <div class="product-info">
          <h3>Hanorac Luxury Black</h3>
          <div class="price">249 lei</div>
          <p>Hanorac modern, confortabil și perfect pentru sezonul rece.</p>
          <p><span class="size">Mărimi:</span> M, L, XL</p>
          <p><span class="size">Material:</span> 80% bumbac, 20% poliester</p>
          <button onclick="addToCart('Hanorac Luxury Black', 249)">Adaugă în coș</button>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=800&q=80" alt="Jeansi brand">
        <div class="product-info">
          <h3>Jeansi Slim Blue</h3>
          <div class="price">219 lei</div>
          <p>Jeansi moderni, confortabili și potriviți pentru orice stil.</p>
          <p><span class="size">Mărimi:</span> 30, 32, 34, 36</p>
          <p><span class="size">Material:</span> 98% denim, 2% elastan</p>
          <button onclick="addToCart('Jeansi Slim Blue', 219)">Adaugă în coș</button>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.unsplash.com/photo-1529139574466-a303027c1d8b?auto=format&fit=crop&w=800&q=80" alt="Geaca brand">
        <div class="product-info">
          <h3>Geacă Urban Style</h3>
          <div class="price">349 lei</div>
          <p>Geacă premium cu design modern și protecție împotriva frigului.</p>
          <p><span class="size">Mărimi:</span> M, L, XL</p>
          <p><span class="size">Material:</span> Poliester rezistent, căptușeală interioară</p>
          <button onclick="addToCart('Geacă Urban Style', 349)">Adaugă în coș</button>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=800&q=80" alt="Rochie eleganta">
        <div class="product-info">
          <h3>Rochie Elegant Chic</h3>
          <div class="price">279 lei</div>
          <p>Rochie elegantă pentru evenimente și apariții rafinate.</p>
          <p><span class="size">Mărimi:</span> S, M, L</p>
          <p><span class="size">Material:</span> 65% viscoză, 35% poliester</p>
          <button onclick="addToCart('Rochie Elegant Chic', 279)">Adaugă în coș</button>
        </div>
      </div>

      <div class="product-card">
        <img src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=800&q=80" alt="Sacou modern">
        <div class="product-info">
          <h3>Sacou Classic Elite</h3>
          <div class="price">399 lei</div>
          <p>Sacou premium pentru un stil elegant și sofisticat.</p>
          <p><span class="size">Mărimi:</span> 46, 48, 50, 52</p>
          <p><span class="size">Material:</span> Lână fină și fibre premium</p>
          <button onclick="addToCart('Sacou Classic Elite', 399)">Adaugă în coș</button>
        </div>
      </div>

    </div>
  </section>

  <section class="section" id="cos">
    <h2>Coș de Cumpărături</h2>
    <div class="cart-section">
      <div class="cart-box">
        <h3>Produse adăugate</h3>
        <ul id="cart-items">
          <li>Coșul este gol.</li>
        </ul>
      </div>

      <div class="cart-box cart-summary">
        <h3>Sumar comandă</h3>
        <p>Total produse: <span id="cart-count-summary">0</span></p>
        <div class="total">Total: <span id="cart-total">0</span> lei</div>
        <button class="checkout-btn" onclick="checkout()">Finalizează comanda</button>
        <button class="clear-btn" onclick="clearCart()">Golește coșul</button>
      </div>
    </div>
  </section>

  <section class="section" id="despre">
    <h2>Despre Noi</h2>
    <div class="about-box">
      <p>Luxury Brand este un magazin online dedicat hainelor de brand, cu design premium și materiale de calitate superioară.</p>
      <p>Oferim produse moderne pentru bărbați și femei, atent selectate pentru stil, eleganță și confort.</p>
      <p>Misiunea noastră este să aducem moda de lux mai aproape de fiecare client.</p>
    </div>
  </section>

  <section class="section" id="contact">
    <h2>Contact</h2>
    <div class="contact-box">
      <p><strong>Email:</strong> contact@luxurybrand.ro</p>
      <p><strong>Telefon:</strong> 0712 345 678</p>
      <p><strong>Adresă:</strong> București, România</p>

      <input type="text" placeholder="Numele tău">
      <input type="email" placeholder="Emailul tău">
      <textarea rows="5" placeholder="Mesajul tău"></textarea>
      <button>Trimite mesajul</button>
    </div>
  </section>

  <footer>
    <p>&copy; 2026 Luxury Brand Shop | Toate drepturile rezervate</p>
  </footer>

  <script>
    let cart = [];

    function addToCart(name, price) {
      cart.push({ name, price });
      updateCart();
      alert(name + " a fost adăugat în coș.");
    }

    function updateCart() {
      const cartItems = document.getElementById("cart-items");
      const cartCount = document.getElementById("cart-count");
      const cartCountSummary = document.getElementById("cart-count-summary");
      const cartTotal = document.getElementById("cart-total");

      cartItems.innerHTML = "";

      if (cart.length === 0) {
        cartItems.innerHTML = "<li>Coșul este gol.</li>";
      } else {
        cart.forEach((item, index) => {
          const li = document.createElement("li");
          li.innerHTML = `
            <span>${item.name} - ${item.price} lei</span>
            <button onclick="removeFromCart(${index})" style="background:#b22222;color:white;border:none;padding:6px 10px;border-radius:6px;cursor:pointer;">Șterge</button>
          `;
          cartItems.appendChild(li);
        });
      }

      const total = cart.reduce((sum, item) => sum + item.price, 0);

      cartCount.textContent = cart.length;
      cartCountSummary.textContent = cart.length;
      cartTotal.textContent = total;
    }

    function removeFromCart(index) {
      cart.splice(index, 1);
      updateCart();
    }

    function clearCart() {
      cart = [];
      updateCart();
    }

    function checkout() {
      if (cart.length === 0) {
        alert("Coșul este gol.");
      } else {
        alert("Comanda a fost trimisă cu succes! Total de plată: " + cart.reduce((sum, item) => sum + item.price, 0) + " lei.");
      }
    }
  </script>

</body>
</html>