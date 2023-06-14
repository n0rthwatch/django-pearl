(function ($) {
  /*==========  background  ==========*/
  $('[data-background]').each(function () {
    $(this).css('background-image', 'url(' + $(this).attr('data-background') + ')');
  });
  /*========== Nice Select ==========*/
  // $('select').niceSelect();
  /*==========  Search  ==========*/
  $('.header__area-menubar-right-box-search-icon.open').on('click', function () {
    $('.header__area-menubar-right-box-search-box').fadeIn().addClass('active');
  });
  $('.header__area-menubar-right-box-search-box-icon').on('click', function () {
    $(this).fadeIn().removeClass('active');
  });
  $('.header__area-menubar-right-box-search-box-icon i').on('click', function () {
    $('.header__area-menubar-right-box-search-box').fadeOut().removeClass('active');
  });
  $('.header__area-menubar-right-box-search-box form').on('click', function (e) {
    e.stopPropagation();
  });
  /*==========  sidebar popup  ==========*/
  $('.header__area-menubar-right-sidebar-popup-icon i').on('click', function () {
    $('.header__area-menubar-right-sidebar-popup').addClass('active');
  });
  $('.header__area-menubar-right-sidebar-popup .sidebar-close-btn').on('click', function () {
    $('.header__area-menubar-right-sidebar-popup').removeClass('active');
  });
  $('.header__area-menubar-right-sidebar-popup-icon i').on('click', function () {
    $('.sidebar-overlay').addClass('show');
  });
  $('.header__area-menubar-right-sidebar-popup .sidebar-close-btn').on('click', function () {
    $('.sidebar-overlay').removeClass('show');
  });
  // /*========== Responsive Menu  ==========*/
  $('.menu-responsive').meanmenu({
    meanMenuContainer: '.responsive-menu',
    meanScreenWidth: '991',
    meanMenuOpen: '<span></span><span></span><span></span>',
    meanMenuClose: '<i class="fal fa-times"></i>',
  });
  /*========== menu-bar sticky  ==========*/
  $(window).on('scroll', function () {
    var scrollDown = $(window).scrollTop();
    if (scrollDown < 135) {
      $('.header__sticky').removeClass('header__sticky-sticky-menu');
    } else {
      $('.header__sticky').addClass('header__sticky-sticky-menu');
    }
  });
  /*==========  Toggle menu  ==========*/
  $('.toggle-menu ul').hide();
  $('.toggle-menu a').click(function () {
    $(this).parent('.toggle-menu').children('ul').slideToggle('100');
    $(this).find('.change').toggleClass('fal fa-angle-down fal fa-angle-right');
  });
  /*==========  isotope  ==========*/
  $(window).on('load', function () {
    /*========== Project Grid  ==========*/
    var $grid = $('.deluxe__area-active').isotope({});
    /*========== Project Filter  ==========*/
    $('.deluxe__area-btn').on('click', 'li', function () {
      var filterValue = $(this).attr('data-filter');
      $grid.isotope({
        filter: filterValue,
      });
    });
    /*========== Project Active  ==========*/
    $('.deluxe__area-btn').on('click', 'li', function () {
      $(this).siblings('.active').removeClass('active');
      $(this).addClass('active');
    });
  });
  /*========== Deluxe Active Hover  ==========*/
  $('.deluxe__area-item').hover(function () {
    $('.deluxe__area-item').removeClass('deluxe__area-item-hover');
    $(this).addClass('deluxe__area-item-hover');
  });
  /*========== Blog Active Hover  ==========*/
  $('.blog__area-item').hover(function () {
    $('.blog__area-item').removeClass('blog__area-item-hover');
    $(this).addClass('blog__area-item-hover');
  });
  /*==========  counterUp  ==========*/
  var counter = $('.counter');
  counter.counterUp({
    time: 2500,
    delay: 100,
  });
  /*==========  video-popup  ==========*/
  $('.video-popup').magnificPopup({
    type: 'iframe',
  });
  /*==========  img-popup  ==========*/
  $('.img-popup').magnificPopup({
    type: 'image',
    gallery: {
      enabled: true,
    },
  });
  /*==========  Testimonial Two  ==========*/
  var swiper = new Swiper('.testimonial__slider', {
    slidesPerView: 1,
    loop: true,
    speed: 1000,
    spaceBetween: 30,
    pagination: {
      el: '.pagination',
      clickable: true,
    },
  });
  /*==========  Brand  ==========*/
  var swiper = new Swiper('.band__slider', {
    loop: true,
    speed: 1500,
    spaceBetween: 30,
    autoplay: {
      delay: 3500,
    },
    breakpoints: {
      0: {
        slidesPerView: 2,
      },
      575: {
        slidesPerView: 4,
      },
      992: {
        slidesPerView: 5,
      },
      1200: {
        slidesPerView: 6,
      },
    },
  });
  /*========== FAQ  ==========*/
  $('.room__details-right-faq-item-card-header').click(function () {
    if ($(this).next('.room__details-right-faq-item-card-header-content').hasClass('active')) {
      $(this).next('.room__details-right-faq-item-card-header-content').removeClass('active').slideUp();
      $(this).children('i').removeClass('far fa-long-arrow-up').addClass('far fa-long-arrow-down');
    } else {
      $('.room__details-right-faq-item-card-header-content').removeClass('active').slideUp();
      $('.room__details-right-faq-item-card-header i')
          .removeClass('far fa-long-arrow-up')
          .addClass('far fa-long-arrow-down');
      $(this).next('.room__details-right-faq-item-card-header-content').addClass('active').slideDown();
      $(this).children('i').removeClass('far fa-long-arrow-down').addClass('far fa-long-arrow-up');
    }
  });
  /*==========  theme loader  ==========*/
  $(window).on('load', function () {
    $('.theme-loader').fadeOut(500);
  });
  /*==========  Banner Slider  ==========*/
  if (jQuery('.banner-slider').length > 0) {
    let sliderActive1 = '.banner-slider';
    let sliderInit1 = new Swiper(sliderActive1, {
      slidesPerView: 1,
      loop: true,
      grabCursor: true,
      effect: "slide",
      speed: 800,
      autoplay: {
        delay: 5500,
      },
    });

    function animated_swiper(selector, init) {
      let animated = function animated() {
        $(selector + ' [data-animation]').each(function () {
          let anim = $(this).data('animation');
          let delay = $(this).data('delay');
          let duration = $(this).data('duration');
          $(this)
              .removeClass('anim' + anim)
              .addClass(anim + ' animated')
              .css({
                webkitAnimationDelay: delay,
                animationDelay: delay,
                webkitAnimationDuration: duration,
                animationDuration: duration,
              })
              .one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function () {
                $(this).removeClass(anim + ' animated');
              });
        });
      };
      animated();
      init.on('slideChange', function () {
        $(sliderActive1 + ' [data-animation]').removeClass('animated');
      });
      init.on('slideChange', animated);
    }

    animated_swiper(sliderActive1, sliderInit1);
  }
  /*========== scroll to top  ==========*/
  var scrollPath = document.querySelector('.scroll-up path');
  var pathLength = scrollPath.getTotalLength();
  scrollPath.style.transition = scrollPath.style.WebkitTransition = 'none';
  scrollPath.style.strokeDasharray = pathLength + ' ' + pathLength;
  scrollPath.style.strokeDashoffset = pathLength;
  scrollPath.getBoundingClientRect();
  scrollPath.style.transition = scrollPath.style.WebkitTransition = 'stroke-dashoffset 10ms linear';
  var updatescroll = function () {
    var scroll = $(window).scrollTop();
    var height = $(document).height() - $(window).height();
    var scroll = pathLength - (scroll * pathLength) / height;
    scrollPath.style.strokeDashoffset = scroll;
  };
  updatescroll();
  $(window).scroll(updatescroll);
  var offset = 50;
  var duration = 950;
  jQuery(window).on('scroll', function () {
    if (jQuery(this).scrollTop() > offset) {
      jQuery('.scroll-up').addClass('active-scroll');
    } else {
      jQuery('.scroll-up').removeClass('active-scroll');
    }
  });
  jQuery('.scroll-up').on('click', function (event) {
    event.preventDefault();
    jQuery('html, body').animate(
        {
          scrollTop: 0,
        },
        duration
    );
    return false;
  });
  if (document.querySelector('#id_guest_phone')) {
    $("#id_guest_phone").inputmask({"mask": "8 (999) 999-99-99"});
  }
  $('.message-block').on('click', () => {
    $('.message-block').remove()
  })
})(jQuery);

// Scroll Effects

new Skroll()
    .add('.scroll-effect', {
      delay: 120,
      duration: 600,
      animation: 'fadeInUp',
    })
    .add('.left-scroll-effect', {
      delay: 120,
      duration: 600,
      animation: 'fadeInRight',
    })
    .add('.right-scroll-effect', {
      delay: 120,
      duration: 600,
      animation: 'fadeInLeft',
    })
    .add('.down-scroll-effect', {
      delay: 120,
      duration: 1000,
      animation: 'fadeInDown',
    })
    .init();

function showRoomInfo(selectElement) {
  const roomId = selectElement.value;
  const roomInfoDiv = document.getElementById('room-info');

  const checkInInput = document.getElementById('id_check_in').value;
  const checkOutInput = document.getElementById('id_check_out').value;

  if (checkInInput && checkOutInput && roomId) {
    updateBtnStatus(roomId, checkInInput, checkOutInput)
  }

  if (roomId && roomInfoDiv) {
    const roomUrl = `/rooms/room_info/${roomId}/`;

    fetch(roomUrl)
      .then(response => response.json())
      .then(data => {
        const html = `
          <h2><a href="/rooms/${data.slug}">${data.name}</a></h2> 
          <div class="d-flex align-items-center justify-content-start gap-4">
            <span><i class="fal fa-users me-2" style="color: var(--primary-color)"></i>${data.max_adults} взр.</span>
            <span><i class="fal fa-users me-2" style="color: var(--primary-color)"></i>${data.max_children} дет.</span>
            <div class="ms-auto">
              <small>Стоимость за ночь:</small>
              <p class="h2 fw-bold" style="color: var(--primary-color)">${data.price} ₽</p>
            </div>
          </div>
          <p class="mb-3">${data.description}</p>
          <img src="${data.image_url}" alt="Room Image" class="img-fluid w-100 mb-4 shadow">
          <h3 class="mb-3">Включённые услуги:</h3>
          <div class="row mb-2">
            ${data.services.map(service => `
              <div class="col-md-4 col-sm-6 mb-35">
                <div class="room__details-right-list-item">
                  <div class="room__details-right-list-item-icon">
                    <img src="/upload/${service.image}" alt="">
                  </div>
                  <div class="room__details-right-list-item-title">
                    <span>${service.title}</span>
                  </div>
                </div>
              </div>
            `).join('')}
          </div>
          `;
        roomInfoDiv.innerHTML = html;
        updateBtnStatus(roomId, checkInInput, checkOutInput)
      });
  } else {
    roomInfoDiv.innerHTML = '';
  }
}

let messageBlock = document.getElementById('check-message')
let priceCounterBlock = document.getElementById('price-counter')

function updateBtnStatus(roomId, checkInInput, checkOutInput) {
  const availabilityUrl = `/rooms/check_availability/?room_id=${roomId}&check_in=${checkInInput}&check_out=${checkOutInput}`;

  fetch(availabilityUrl)
    .then(response => response.json())
    .then(data => {
      console.log(data)
      btn = document.querySelector('[type="submit"]')
      if (data.availability === false) {
        btn.setAttribute('disabled', 'true')
        btn.classList.add('disabled-btn')
        messageBlock.innerHTML = `Выбранный номер будет доступен <b>до ${data.room_check_in}</b> и <b>после ${data.room_check_out}</b>`
        priceCounterBlock.innerHTML = ''
      } else {
        btn.removeAttribute('disabled')
        btn.classList.remove('disabled-btn')
        messageBlock.innerHTML = ''
        const html = `
          <div>
            <small class="fw-semibold">Стоимость проживания (${data.nights_count} ночей):</small>
            <p class="h2 fw-bold" style="color: var(--primary-color)">${data.price} ₽</p>
          </div>
        `
        priceCounterBlock.innerHTML = html;
      }
    });
}


const checkInInput = document.getElementById('id_check_in');
const checkOutInput = document.getElementById('id_check_out')
if (checkInInput && checkOutInput) {
  checkInInput.addEventListener('change', () => {
    checkOutInput.min = checkInInput.value;
    if (checkOutInput.value < checkInInput.value) {
      checkOutInput.value = checkInInput.value;
    }
    showRoomInfo(document.querySelector('[name="room_choice"]'))
  });
  checkOutInput.addEventListener('change', () => {
    checkOutInput.min = checkInInput.value;
    if (checkOutInput.value < checkInInput.value) {
      checkOutInput.value = checkInInput.value;
    }
    showRoomInfo(document.querySelector('[name="room_choice"]'))
  })
}

new Splide('.splide', {
  type: 'loop',
  perPage: 2,
  height: '350px',
  gap: 35
}).mount();