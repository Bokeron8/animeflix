
var w = $(window).width();
var h = $(window).height();

if (w < 500 && h < 1000){
  console.log('a')
  $('.episodes').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 3,
    prevArrow: 'c',
    nextArrow: 'c',
  });
} 
else{
  $('.episodes').slick({
    infinite: true,
    slidesToShow: 5,
    slidesToScroll: 5,
    prevArrow: 'c',
    nextArrow: 'c',
  });
}

