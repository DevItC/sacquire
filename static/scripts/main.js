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
      url: '/enqueue',
      data: formdata,
      type: 'POST',
      dataType: 'JSON'
    }
  )
  .done((res) => {
    getStatus(res.data.task_id)
  })
  .fail((err) => {
    console.log(err)
  })
})

function getStatus(taskID) {
  $.ajax({
    url: `/tasks/${taskID}`,
    method: 'GET'
  })
  .done((res) => {
    const taskStatus = res.data.task_status;

    if (taskStatus === 'finished' || taskStatus === 'failed') {
      console.log('Completion check')
      var elem = document.querySelector('#link_im')
      elem.setAttribute("href", res.data.link);
      elem = document.querySelector('#img_src')
      elem.setAttribute("src", res.data.preview_link);
      
      // elem.innerHTML.innerHTML.src = res.data.preview_link;
      elem = document.querySelector('#image')
      
      elem.style.display = "Block";
      console.log('JQuery set check.')
      elem = document.getElementById("image")
      window.history.replaceState({}, "", window.location.href);

      l.stop();
      return false;
    }
    setTimeout(function() {
      getStatus(res.data.task_id);
    }, 1000)
 ; })
  .fail((err) => {
    console.log(err)
  })
}

function updateQuery(key, value){
  url = window.location.href

}

function updateQueryStringParam(key, value) {
  param = location.protocol
  baseUrl = [location.protocol, '//', location.host, location.pathname].join('');
  console.log(baseUrl)
  urlQueryString = document.location.search;
  var newParam = key + '=' + value,
  params = '?' + newParam;

  // If the "search" string exists, then build params from it
  if (urlQueryString) {
    keyRegex = new RegExp('([\?&])' + key + '[^&]*');
    // If param exists already, update it
    if (urlQueryString.match(keyRegex) !== null) {
      params = urlQueryString.replace(keyRegex, "$1" + newParam);
    } else { // Otherwise, add it to end of query string
      params = urlQueryString + '&' + newParam;
    }
  }
  window.history.replaceState({}, "", baseUrl + params);
}
