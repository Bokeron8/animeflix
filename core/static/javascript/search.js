var w = $(window).width();
var h = $(window).height();

if (w < 500 && h < 1000){
  $('.animes-found').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 3,
    prevArrow: 'c',
    nextArrow: 'c',
  });
} 
else{
  $('.animes-found').slick({
    infinite: true,
    slidesToShow: Math.min($(".animes-found").children().length, 5),
    slidesToScroll: Math.min($(".animes-found").children().length, 5),
    prevArrow: 'c',
    nextArrow: 'c',
  });
}

