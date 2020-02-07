let box = $('#block')

$(function () {
	$('[data-toggle="tooltip"]').tooltip()
})

if ($('#id_short_url').val() === '') {
	box.hide()
} else {
	box.show()
}

$('#copy').click(function() {
	let value = $('#id_short_url')
	value.select()
	document.execCommand('copy')
	$(this).attr('data-original-title', 'Copied!').tooltip('show')
	$(this).mouseleave(function() {
		$(this).attr('data-original-title', 'Copy to Clipboard!')
	})
})

$('#form').submit(function () {
	$('#block').hide();

	// ajax
	$.ajax({
		url: '/ajax/',
		type: 'POST',
		data: $(this).serialize(),
		cache: false,
		success: function (data) {
			console.log(data)
			let originUrl = $('#id_url').val()
			$('#id_url').val('')
			$('#id_short_url').val(data['short_url'])
			$('#block').show()
			$('.toast').toast('show')
			// let calloutBody = document.createElement("div")
			// calloutBody.className = "bs-callout bs-callout-success"
			// let calloutTitle = document.createElement("h4")
			// calloutTitle.innerText = originUrl
			// let calloutText = document.createTextNode($('#id_short_url').val())
		
			// calloutBody.appendChild(calloutTitle)
			// console.log(calloutBody)
			// calloutBody.innerText = $('#id_short_url').val()
			// $('#history').append(calloutBody)

			// console.log(calloutBody)
			// let historyPanel = document.getElementsByClassName('history').append(calloutBody)
			// console.log(historyPanel)
			// historyPanel
		},
		error: function(data) { 
			console.log("Ajax Error.")
		}
	});


	return false;

	
	// history

});