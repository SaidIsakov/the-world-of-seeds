from django.test import TestCase
# {% load static %}

# <section class="hero-section">
#         <div class="product-card tomato-card" data-product="tomato">
#             <a href="{{ product.get_absolute_url }}">
#             <div class="product-image">
#                     <img src="{% static "main/img/f1.webp" %}">
#             </div>    
#             </a>
#                 <div class="product-overlay">
#                     <div class="product-title-hero">РОЗОВЫЙ<br>ТОМАТ РОЗЕТТ<br>F1</div>
#                     <div class="product-details">
#                         <div class="product-price">2400 ₽</div>
#                     <div>

#                             <button class="btn-details" href="{{ product.get_absolute_url }}">ПОДРОБНЕЕ</button>
#                             {% comment %} <button class="btn-add-cart" onclick="addToCart('tomato', 'Розовый томат Розетт F1', 2400)">В КОРЗИНУ</button> {% endcomment %}
#                         </div>
#                     </div>
#                 </div>
#             </div>
        

#         <div class="product-card fungicide-card" data-product="fungicide">
#             <a href="{{ product.get_absolute_url }}">
#             <div class="product-image">
#                 <img src="{% static "main/img/th82.jpg" href="{{ product.get_absolute_url }}" %}" ></img>
#             </div>
#         </a>
#                 <div class="product-overlay">
#                     <div class="product-title-hero">ФУНГИЦИД<br>ТРИХОДЕРМИН<br>TH82</div>
#                     <div class="product-details">
#                         <div class="product-price">660 ₽</div>
#                         <div>
#                             <button class="btn-details" href="{{ article.get_absolute_url }}">ПОДРОБНЕЕ</button>
#                             {% comment %} <button class="btn-add-cart" onclick="addToCart('fungicide', 'Фунгицид Триходермин TH82', 660)">В КОРЗИНУ</button> {% endcomment %}
#                         </div>
#                     </div>     
#                 </div>
            
        
    

#     </section>



# <!-- Fungicide Product Card -->
#     <div class="product-card fungicide-card" data-product="fungicide">
#         <a href="{{ product.get_absolute_url }}">
#             <div class="product-image">
#                 <img src="{% static 'main/img/th82.jpg' %}" alt="Фунгицид Триходермин TH82">
#             </div>
#         </a>
#         <div class="product-overlay">
#             <div class="product-title-hero">ФУНГИЦИД<br>ТРИХОДЕРМИН<br>TH82</div>
#             <div class="product-details">
#                 <div class="product-price">660 ₽</div>
#                 <div>
#                     <a href="{{ product.get_absolute_url }}" class="btn-details">ПОДРОБНЕЕ</a>
#                     {% comment %}
#                     <button class="btn-add-cart" onclick="addToCart('fungicide', 'Фунгицид Триходермин TH82', 660)">В КОРЗИНУ</button>
#                     {% endcomment %}
#                 </div>
#             </div>
#         </div>
#     </div>