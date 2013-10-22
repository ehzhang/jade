/**
  
  Custom site-wide javascript for TEMPEST.
  
  JADE 2013

**/

var mailto_link = "mailto:?Subject=Help me brainstorm on Tempest%21&body=Follow this link: " + encodeURIComponent(location.href);

$('#email_button').click(function() {window.location = mailto_link;});

$('#share_button').popup('setting', 'transition', 'fade up');

$('#share_button').click(show_share_modal);

$('#poll_url').focus(function() {$(this).select()}).mouseup(function (e) {e.preventDefault(); });

function show_share_modal(){
  $('#share_link').val(location.href);
  $('#share_modal').modal('show');
}