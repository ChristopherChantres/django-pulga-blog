function goToCreate() {
  window.location.href = "/create";
}

document.getElementById("create-post").addEventListener("click", goToCreate);

setTimeout(function() {
  $('.success-alert').fadeOut('slow');
}, 5000);