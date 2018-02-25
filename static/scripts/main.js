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
      window.location.assign(`/download/${taskID}`);
      l.stop();
      return false;
    }
    setTimeout(function() {
      getStatus(res.data.task_id);
    }, 1000);
  })
  .fail((err) => {
    console.log(err)
  })
}
