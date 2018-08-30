// custom javascript

$(document).ready(() => {
  console.log('Sanity Check!');
});

var l = Ladda.create( document.querySelector( 'button' ) );

$('form').submit(function(event) {
  var formdata = $(this).serializeObject();
  event.preventDefault();
  l.start();

  $.ajax(
    {
      url: '/api',
      data: formdata,
      type: 'POST',
      dataType: 'JSON'
    }
  )
  .done((res) => {
    console.log('Completion check')
    var elem = document.querySelector('#link_im')
    elem.setAttribute("href", res.media_url);
    elem = document.querySelector('#img_src')
    elem.setAttribute("src", res.media_preview);
    elem = document.querySelector('#image')    
    elem.style.display = "Block";
    console.log('JQuery set check.')
    elem = document.getElementById("image")
    window.history.replaceState({}, "", window.location.href);

    l.stop();
    return false;
  })
  .fail((err) => {
    console.log(err)
  })
})
