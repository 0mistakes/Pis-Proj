 $(document).ready(function() {
            $('#contact-form').submit(function(e) {
                e.preventDefault();

                var name = $('#name').val();
                var phone = $('#phone').val();
                var email = $('#email').val();
                var contactMethod = $('input[name="contact-method"]:checked').val();

                var postData = {
                    'fields': {
                        'TITLE': 'Бесплатная консультация',
                        'NAME': name,
                        'PHONE': [{'VALUE': phone, 'VALUE_TYPE': 'WORK'}],
                        'EMAIL': [{'VALUE': email, 'VALUE_TYPE': 'WORK'}],
                        'COMMENTS': 'Предпочитаемый метод связи: ' + contactMethod
                    },
                    'params': {
                        'REGISTER_SONET_EVENT': 'Y'
                    }
                };

                $.ajax({
                    url: 'https://b24-1dk1va.bitrix24.ru/rest/1/28ck3wiw97e5ztfz/crm.lead.add.json',
                    type: 'POST',
                    data: JSON.stringify(postData),
                    dataType: 'json',
                    contentType: 'application/json',
                    success: function(response) {
                        $('#contactModal').modal('hide');
                        showNotification('Заявка успешно создана. Мы свяжемся с вами в ближайшее время!', 'success');
                        // Добавьте здесь код для обработки успешного создания лида, если требуется
                    },
                    error: function(xhr, status, error) {
                        showNotification('Произошла ошибка при создании заявки: ' + error, 'error');
                        // Добавьте здесь код для обработки ошибки, если требуется
                    }
                });
            });

            $('.consult').click(function() {
                $('#contactModal').modal('show');
            });

            function showNotification(message, type) {
                Toastify({
                    text: message,
                    duration: 5000,
                    gravity: 'bottom-right',
                    position: 'right',
                    backgroundColor: type === 'success' ? '#28a745' : '#dc3545',
                    className: 'text-white',
                    close: true,
                }).showToast();
            }
        });
function selectCategory(categoryName) {
        document.getElementById('selected_category_name').value = categoryName;
    }
function selectCity(cityName) {
    document.getElementById('selected_city').value = cityName;
}

function selectPriceOrder(order) {
    document.getElementById('selected_price_order').value = order;
}

const rentingMenuItem = document.querySelector('.menu__item:nth-child(4)');
const submenu = rentingMenuItem.querySelector('.submenu');

rentingMenuItem.addEventListener('mouseenter', () => {
  submenu.style.display = 'block';
});

rentingMenuItem.addEventListener('mouseleave', () => {
  submenu.style.display = 'none';
});
//---Menu

const burger = document.querySelector('.menu-icon');
const menu = document.querySelector('.menu');
const body = document.body
const price = document.querySelector('.prices');

if (burger && menu) {
	burger.addEventListener('click', () => {
		burger.classList.toggle('_active');
		menu.classList.toggle('_active');
		body.classList.toggle('_lock');
		prices.classList.toggle('_hidden')
	})
}

//---Filter dropdown

const filter = document.querySelector('.filter');

if (filter) {
	const items = filter.querySelectorAll('.block-filter')

	items.forEach(item => {
		item.addEventListener('click', event => {
			item.querySelector('.block-filter__dropdown').classList.toggle('_active');
			item.querySelector('.block-filter__icon').classList.toggle('_active');

			if (event.target.classList.contains('block-filter__item')) {
				item.querySelector('.block-filter__value').textContent = event.target.textContent;
			}
		})
	})
}

//---Swiper

const popularSlider = new Swiper('.popular-slider', {
	spaceBetween: 20,
	slidesPerView: 1,
	// Navigation arrows
	navigation: {
		nextEl: '.popular-slider-next',
		prevEl: '.popular-slider-prev',
	},
	breakpoints: {
		992: {
			slidesPerView: 3,
		},
		660: {
			slidesPerView: 2,
		}
	}
});

const reviewsSlider = new Swiper('.slider-reviews', {
	spaceBetween: 20,
	slidesPerView: 1,
	autoHeight: true,
	navigation: {
		nextEl: '.slider-reviews-next',
		prevEl: '.slider-reviews-prev',
	},
});

//---Gallery

const galleryItems = document.querySelectorAll(".gallery__item");

if (galleryItems.length > 0) {
	galleryItems.forEach(item => {
		new Swiper(item, {
			slidesPerView: 1, 
			autoplay: {
				delay: 5000,
			},
			effect: 'fade',
		})
	})
}

const images = document.querySelectorAll('.filtr_search .type_of_object img');
const filterLinks = document.querySelectorAll('.filtr_search .filter_link');

// Добавляем обработчик события для каждого изображения
images.forEach((img, index) => {
  img.addEventListener('click', () => {
    // Скрываем все блоки filter_link, кроме того, который находится внутри кликнутого элемента
    filterLinks.forEach((link, linkIndex) => {
      if (linkIndex !== index) {
        link.style.display = 'none';
      }
    });
  });
});

 // Получаем ссылку на кнопку и все значения формы
